"""
Tic Tac Toe (4x4, drei in einer Reihe gewinnt) als Browser-Version.

Das ist eine Kopie von adtictactoe_local.py (tkinter) in pygame-ce,
damit das Spiel mit pygbag als WebAssembly-Seite auf GitHub Pages laeuft.
Die Spiellogik (Gewinnpruefung, Punktestand, Runden) ist unveraendert.

Wichtig fuer pygbag:
  * die Datei heisst main.py
  * der Loop steckt in async def main()
  * im Loop steht await asyncio.sleep(0)
  * am Ende steht asyncio.run(main())
"""

import asyncio

import pygame

# --------------------------------------------------------------- Konstanten ---
BREITE = 800
HOEHE = 600

SCHWARZ = (0, 0, 0)
WEISS = (255, 255, 255)
GRAU = (90, 90, 90)
DUNKELGRAU = (35, 35, 35)
GRUEN = (0, 150, 60)

FELDGROESSE = 130
FELD_ABSTAND = 10
FELD_X = 25
FELD_Y = 25

INFO_X = 600
INFO_BREITE = 175
INFO_MITTE = INFO_X + INFO_BREITE // 2

SZENE_NAMEN = "namen"
SZENE_SPIEL = "spiel"
SZENE_ERGEBNIS = "ergebnis"

MAX_NAME = 14

# ------------------------------------------------------------- Spielzustand ---
szene = SZENE_NAMEN
aktueller_spieler = "X"
punkte_x = 0
punkte_o = 0
name_x = ""
name_o = ""
txt_x = ""
txt_o = ""
aktives_feld = "x"
felder = [[" " for _ in range(4)] for _ in range(4)]
gewinner_felder = []
runde_entschieden = False
dran_text = "Am Zug: X"

_font_cache = {}


# ------------------------------------------------------------------ Logik ----
def leeres_feld():
    return [[" " for _ in range(4)] for _ in range(4)]


def drei_gleich(a, b, c):
    return a == b and b == c and a != " "


def gewinner_pruefen():
    # Waagerecht
    for zeile in range(4):
        if drei_gleich(felder[zeile][0], felder[zeile][1], felder[zeile][2]):
            return [(zeile, 0), (zeile, 1), (zeile, 2)]
        if drei_gleich(felder[zeile][1], felder[zeile][2], felder[zeile][3]):
            return [(zeile, 1), (zeile, 2), (zeile, 3)]

    # Senkrecht
    for spalte in range(4):
        if drei_gleich(felder[0][spalte], felder[1][spalte], felder[2][spalte]):
            return [(0, spalte), (1, spalte), (2, spalte)]
        if drei_gleich(felder[1][spalte], felder[2][spalte], felder[3][spalte]):
            return [(1, spalte), (2, spalte), (3, spalte)]

    # Diagonal von links oben nach rechts unten
    if drei_gleich(felder[0][0], felder[1][1], felder[2][2]):
        return [(0, 0), (1, 1), (2, 2)]
    if drei_gleich(felder[1][1], felder[2][2], felder[3][3]):
        return [(1, 1), (2, 2), (3, 3)]
    if drei_gleich(felder[0][1], felder[1][2], felder[2][3]):
        return [(0, 1), (1, 2), (2, 3)]
    if drei_gleich(felder[1][0], felder[2][1], felder[3][2]):
        return [(1, 0), (2, 1), (3, 2)]

    # Diagonal von rechts oben nach links unten
    if drei_gleich(felder[0][2], felder[1][1], felder[2][0]):
        return [(0, 2), (1, 1), (2, 0)]
    if drei_gleich(felder[1][3], felder[2][2], felder[3][1]):
        return [(1, 3), (2, 2), (3, 1)]
    if drei_gleich(felder[0][3], felder[1][2], felder[2][1]):
        return [(0, 3), (1, 2), (2, 1)]
    if drei_gleich(felder[1][2], felder[2][1], felder[3][0]):
        return [(1, 2), (2, 1), (3, 0)]

    return None


def alle_felder_voll():
    for zeile in range(4):
        for spalte in range(4):
            if felder[zeile][spalte] == " ":
                return False
    return True


def spiel_beenden(tripel):
    global punkte_x, punkte_o, gewinner_felder, runde_entschieden, dran_text
    gewinner = felder[tripel[0][0]][tripel[0][1]]
    if gewinner == "X":
        punkte_x = punkte_x + 1
    else:
        punkte_o = punkte_o + 1
    dran_text = f"Gewinner: {gewinner}!"
    gewinner_felder = tripel
    runde_entschieden = True


def unentschieden():
    global dran_text, runde_entschieden
    dran_text = "Unentschieden!"
    runde_entschieden = True


def anzeige_aktualisieren():
    global dran_text
    dran_text = f"Am Zug: {aktueller_spieler}"
    gewinner = gewinner_pruefen()
    if gewinner:
        spiel_beenden(gewinner)
    elif alle_felder_voll():
        unentschieden()


def neue_runde():
    global felder, aktueller_spieler, gewinner_felder, runde_entschieden, dran_text
    aktueller_spieler = "X"
    felder = leeres_feld()
    gewinner_felder = []
    runde_entschieden = False
    dran_text = "Am Zug: X"


def spielstand_zuruecksetzen():
    global punkte_x, punkte_o
    punkte_x = 0
    punkte_o = 0
    neue_runde()


def klick_auf_feld(zeile, spalte):
    global aktueller_spieler
    if runde_entschieden:
        return
    if felder[zeile][spalte] != " ":
        return
    felder[zeile][spalte] = aktueller_spieler
    if aktueller_spieler == "X":
        aktueller_spieler = "O"
    else:
        aktueller_spieler = "X"
    anzeige_aktualisieren()


def spiel_starten():
    global name_x, name_o, szene
    name_x = txt_x.strip()
    name_o = txt_o.strip()
    if name_x == "":
        name_x = "Spieler 1"
    if name_o == "":
        name_o = "Spieler 2"
    neue_runde()
    szene = SZENE_SPIEL


def ergebnis_text():
    if punkte_x > punkte_o:
        return f"{name_x} hat gewonnen!"
    if punkte_o > punkte_x:
        return f"{name_o} hat gewonnen!"
    return "Unentschieden!"


def tippe(text):
    global txt_x, txt_o
    if not text.isprintable():
        return
    if aktives_feld == "x":
        if len(txt_x) < MAX_NAME:
            txt_x = txt_x + text
    else:
        if len(txt_o) < MAX_NAME:
            txt_o = txt_o + text


def loesche():
    global txt_x, txt_o
    if aktives_feld == "x":
        txt_x = txt_x[:-1]
    else:
        txt_o = txt_o[:-1]


# -------------------------------------------------------------------- Layout --
def feld_rect(zeile, spalte):
    x = FELD_X + spalte * (FELDGROESSE + FELD_ABSTAND)
    y = FELD_Y + zeile * (FELDGROESSE + FELD_ABSTAND)
    return pygame.Rect(x, y, FELDGROESSE, FELDGROESSE)


def hole_buttons():
    if szene == SZENE_NAMEN:
        return [("start", "Spiel starten", pygame.Rect(290, 420, 220, 60))]
    if szene == SZENE_SPIEL:
        return [
            ("weiter", "Weiter", pygame.Rect(INFO_X, 380, INFO_BREITE, 52)),
            ("reset", "Spielstand zurücksetzen", pygame.Rect(INFO_X, 445, INFO_BREITE, 52)),
            ("beenden", "Spiel beenden", pygame.Rect(INFO_X, 510, INFO_BREITE, 52)),
        ]
    return [
        ("neues_spiel", "Neues Spiel", pygame.Rect(230, 420, 160, 60)),
        ("ende", "Beenden", pygame.Rect(410, 420, 160, 60)),
    ]


def hole_eingabefelder():
    return [
        ("x", pygame.Rect(250, 195, 300, 48)),
        ("o", pygame.Rect(250, 305, 300, 48)),
    ]


# ------------------------------------------------------------------ Zeichnen --
def hole_font(groesse):
    if groesse not in _font_cache:
        _font_cache[groesse] = pygame.font.Font(None, groesse)
    return _font_cache[groesse]


def schreibe(flaeche, text, x, y, groesse, farbe=WEISS, mitte=True, max_breite=None):
    font = hole_font(groesse)
    if max_breite is not None:
        while font.size(text)[0] > max_breite and groesse > 12:
            groesse = groesse - 1
            font = hole_font(groesse)
    bild = font.render(text, True, farbe)
    rect = bild.get_rect()
    if mitte:
        rect.center = (x, y)
    else:
        rect.midleft = (x, y)
    flaeche.blit(bild, rect)


def zeichne_button(flaeche, rect, beschriftung):
    pygame.draw.rect(flaeche, DUNKELGRAU, rect)
    pygame.draw.rect(flaeche, GRAU, rect, 2)
    schreibe(flaeche, beschriftung, rect.centerx, rect.centery, 26, WEISS, True, rect.width - 12)


def zeichne_namen(flaeche):
    schreibe(flaeche, "Tic Tac Toe", 400, 90, 64)
    schreibe(flaeche, "4x4 - drei in einer Reihe gewinnt", 400, 135, 24, GRAU)
    schreibe(flaeche, "Name Spieler 1 (X):", 400, 170, 26)
    schreibe(flaeche, "Name Spieler 2 (O):", 400, 280, 26)

    for kid, rect in hole_eingabefelder():
        pygame.draw.rect(flaeche, SCHWARZ, rect)
        pygame.draw.rect(flaeche, WEISS if kid == aktives_feld else GRAU, rect, 2)
        if kid == "x":
            inhalt = txt_x
        else:
            inhalt = txt_o
        if inhalt == "":
            schreibe(flaeche, "Name eingeben ...", rect.x + 10, rect.centery, 26, GRAU, False)
        else:
            schreibe(flaeche, inhalt, rect.x + 10, rect.centery, 28, WEISS, False, rect.width - 20)

    for kid, beschriftung, rect in hole_buttons():
        zeichne_button(flaeche, rect, beschriftung)

    schreibe(flaeche, "Ins Feld klicken, tippen, mit Enter starten", 400, 530, 22, GRAU)


def zeichne_spiel(flaeche):
    for zeile in range(4):
        for spalte in range(4):
            rect = feld_rect(zeile, spalte)
            if (zeile, spalte) in gewinner_felder:
                pygame.draw.rect(flaeche, GRUEN, rect)
            else:
                pygame.draw.rect(flaeche, SCHWARZ, rect)
            pygame.draw.rect(flaeche, GRAU, rect, 2)
            wert = felder[zeile][spalte]
            if wert != " ":
                schreibe(flaeche, wert, rect.centerx, rect.centery, 96)

    pygame.draw.line(flaeche, GRAU, (INFO_X - 15, 10), (INFO_X - 15, HOEHE - 10), 2)

    schreibe(flaeche, dran_text, INFO_MITTE, 60, 30, WEISS, True, INFO_BREITE - 4)
    schreibe(flaeche, f"{name_x}: X", INFO_MITTE, 150, 26, WEISS, True, INFO_BREITE)
    schreibe(flaeche, f"{name_o}: O", INFO_MITTE, 182, 26, WEISS, True, INFO_BREITE)
    schreibe(flaeche, "Punkte", INFO_MITTE, 250, 26)
    schreibe(flaeche, f"X: {punkte_x}    O: {punkte_o}", INFO_MITTE, 285, 30, WEISS, True, INFO_BREITE)

    for kid, beschriftung, rect in hole_buttons():
        zeichne_button(flaeche, rect, beschriftung)


def zeichne_ergebnis(flaeche):
    schreibe(flaeche, "Ergebnis", 400, 90, 56)
    schreibe(flaeche, ergebnis_text(), 400, 200, 44, WEISS, True, 700)
    schreibe(flaeche, f"X: {punkte_x}    O: {punkte_o}", 400, 280, 34)
    schreibe(flaeche, f"{name_x} (X)  -  {name_o} (O)", 400, 330, 24, GRAU, True, 700)

    for kid, beschriftung, rect in hole_buttons():
        zeichne_button(flaeche, rect, beschriftung)


def zeichne(flaeche):
    flaeche.fill(SCHWARZ)
    if szene == SZENE_NAMEN:
        zeichne_namen(flaeche)
    elif szene == SZENE_SPIEL:
        zeichne_spiel(flaeche)
    else:
        zeichne_ergebnis(flaeche)


# -------------------------------------------------------------------- Klicks --
def button_klick(kid):
    global szene, punkte_x, punkte_o, txt_x, txt_o, aktives_feld
    if kid == "start":
        spiel_starten()
    elif kid == "weiter":
        neue_runde()
    elif kid == "reset":
        spielstand_zuruecksetzen()
    elif kid == "beenden":
        szene = SZENE_ERGEBNIS
    elif kid == "neues_spiel":
        punkte_x = 0
        punkte_o = 0
        txt_x = ""
        txt_o = ""
        aktives_feld = "x"
        neue_runde()
        szene = SZENE_NAMEN
    elif kid == "ende":
        return False
    return True


def maus_klick(pos):
    global aktives_feld
    for kid, beschriftung, rect in hole_buttons():
        if rect.collidepoint(pos):
            return button_klick(kid)

    if szene == SZENE_NAMEN:
        for kid, rect in hole_eingabefelder():
            if rect.collidepoint(pos):
                aktives_feld = kid
    elif szene == SZENE_SPIEL and not runde_entschieden:
        for zeile in range(4):
            for spalte in range(4):
                if feld_rect(zeile, spalte).collidepoint(pos):
                    klick_auf_feld(zeile, spalte)
    return True


# --------------------------------------------------------------- Hauptschleife -
async def main():
    global szene, aktueller_spieler, punkte_x, punkte_o, name_x, name_o
    global txt_x, txt_o, aktives_feld, felder, gewinner_felder
    global runde_entschieden, dran_text

    pygame.init()
    pygame.display.set_mode((BREITE, HOEHE))
    pygame.display.set_caption("Tic Tac Toe")
    flaeche = pygame.display.get_surface()
    uhr = pygame.time.Clock()
    pygame.key.start_text_input()

    # Startzustand bewusst am Anfang setzen (hilft pygbag beim Kompilieren).
    szene = SZENE_NAMEN
    aktueller_spieler = "X"
    punkte_x = 0
    punkte_o = 0
    name_x = ""
    name_o = ""
    txt_x = ""
    txt_o = ""
    aktives_feld = "x"
    felder = leeres_feld()
    gewinner_felder = []
    runde_entschieden = False
    dran_text = "Am Zug: X"

    laeuft = True
    while laeuft:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                laeuft = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                laeuft = maus_klick(event.pos)
            elif event.type == pygame.TEXTINPUT and szene == SZENE_NAMEN:
                tippe(event.text)
            elif event.type == pygame.KEYDOWN and szene == SZENE_NAMEN:
                if event.key == pygame.K_BACKSPACE:
                    loesche()
                elif event.key in (pygame.K_RETURN, pygame.K_KP_ENTER):
                    spiel_starten()
                elif event.key == pygame.K_TAB:
                    if aktives_feld == "x":
                        aktives_feld = "o"
                    else:
                        aktives_feld = "x"

        zeichne(flaeche)
        pygame.display.flip()
        uhr.tick(60)
        await asyncio.sleep(0)


asyncio.run(main())
