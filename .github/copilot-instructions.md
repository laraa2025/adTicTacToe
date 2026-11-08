# Projekt: adTicTacToe

Tic Tac Toe (4×4, drei in einer Reihe gewinnt) mit Spielernamen, Punktestand, Weiter/Reset und Ergebnisbildschirm.

Zwei Varianten im Repo:

| Pfad | Rolle |
|---|---|
| `adtictactoe_local.py`, `adtictactoe_local.md` | Original (tkinter, Desktop). **Nicht ändern.** |
| `web/main.py` | Web-Version (pygame-ce), wird auf GitHub Pages veröffentlicht |
| `docs/deploy.md` | Ausführliche Deployment-Doku |

## Harte Regeln

1. **`adtictactoe_local.py` und `adtictactoe_local.md` niemals verändern.** Änderungen für die Web-Version
   immer in `web/main.py` – dort ist die Spiellogik bereits 1:1 portiert (`drei_gleich`, `gewinner_pruefen`
   mit 24 Mustern, `alle_felder_voll`, `spiel_beenden`, `neues_runde`, `spielstand_zuruecksetzen`).
2. **Die Hauptschleife nie beenden.** Im Browser bleibt sonst ein eingefrorenes Canvas stehen und nichts
   reagiert mehr. Stattdessen eine Szene anzeigen (`SZENE_ENDE`). Nur `pygame.QUIT` darf die Schleife beenden.
3. **Dateien im Repo bleiben private:** `*.pdf` ist per `.gitignore` ausgeschlossen. Nicht committen.
4. pygbag-Vorgaben einhalten: Einstieg `web/main.py`, `async def main()`, `await asyncio.sleep(0)` in jeder
   Iteration, `asyncio.run(main())` am Dateiende, keine blockierenden Aufrufe (`input()`, `messagebox`,
   `pygame.event.wait`).
5. Szenen laufen über die globale Variable `szene`: `SZENE_NAMEN` → `SZENE_SPIEL` → `SZENE_ERGEBNIS` → `SZENE_ENDE`.
   Buttons werden ausschließlich über `hole_buttons()` definiert (Zeichnen *und* Klicken nutzen dieselben Rects).

## Deployment (automatisch)

Jeder Push auf `main` baut und veröffentlicht automatisch:

`.github/workflows/pygbag.yml` → `python -m pygbag --build web` → `.nojekyll` → Deploy `web/build/web`
nach Branch `gh-pages` (JamesIves/github-pages-deploy-action v4). GitHub Pages liefert `gh-pages` /(root) aus.

- **Live:** https://laraa2025.github.io/adTicTacToe/
- **Repo:** https://github.com/laraa2025/adTicTacToe

### Nach jeder Codeänderung – ohne Rückfrage ausführen

```powershell
# 1. Logik/Zeichnen headless prüfen (SDL_VIDEODRIVER=dummy, Quelle ohne letzte Zeile asyncio.run(main()) exec'en)
python web/main.py                 # optionaler Desktop-Sichtcheck

# 2. Build prüfen
python -m pygbag --build web       # muss web/build/web/index.html erzeugen

# 3. Veröffentlichen
git add web/main.py docs/deploy.md .github/copilot-instructions.md
git commit -m "<kurze Beschreibung>"
git push
```

Danach dem Nutzer melden: Action `pygbag_build` läuft ca. 2–4 Minuten, danach `Strg + F5` auf der Live-URL
nötig (WASM-Cache im Browser).

Wenn der Push an der Authentifizierung scheitert: `git config --global credential.helper manager` und
`cmdkey /delete:git:https://github.com`. Commits müssen die noreply-Adresse des Accounts verwenden
(Repo blockt Pushes mit privater E-Mail).

## Lokale Umgebung (Windows)

- Interpreter: `C:\Users\larak\AppData\Local\Programs\Python\Python312\python.exe`
- Pakete: `pygame-ce` (2.5.8), `pygbag` (0.9.3)
- Testserver: `python -m pygbag web` → http://localhost:8000

## Bekannte Stolperfallen

- pygbag 0.9.x erzeugt `index.html` + `favicon.png` + `web.apk`/`web.tar.gz` (App liegt im Archiv, nicht als
  einzelne `.wasm`).
- Im Testserver-Log erscheinen `browserfs.min.js` 404 und `PyMain: BrowserFS not found` – harmlos.
- Neue Buttons müssen in `hole_buttons()` **und** `button_klick()` ergänzt werden, sonst sind sie toter Klickraum.
- Text-Eingabe nach Szenenwechsel: `pygame.key.start_text_input()` erneut aufrufen (macht
  `zurueck_zur_namenseingabe()`).
