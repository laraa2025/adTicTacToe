import tkinter as tk

aktueller_spieler = "X"
punkte_x = 0
punkte_o = 0
name_x = ""
name_o = ""

fenster = tk.Tk()
fenster.title("Tic Tac Toe")
fenster.geometry("800x600")
fenster.configure(bg="black")
fenster.withdraw()

# Startfenster für die Namens-Eingabe
startfenster = tk.Toplevel(fenster)
startfenster.title("Spieler wählen")
startfenster.geometry("320x280")
startfenster.configure(bg="black")

name_x_label = tk.Label(startfenster, text="Name Spieler 1 (X):", bg="black", fg="white", font=("Arial", 12))
name_x_label.pack(pady=(20, 0))

name_x_entry = tk.Entry(startfenster, font=("Arial", 12))
name_x_entry.pack(pady=5)

name_o_label = tk.Label(startfenster, text="Name Spieler 2 (O):", bg="black", fg="white", font=("Arial", 12))
name_o_label.pack(pady=(20, 0))

name_o_entry = tk.Entry(startfenster, font=("Arial", 12))
name_o_entry.pack(pady=5)

def spiel_starten():
    global name_x, name_o
    name_x = name_x_entry.get()
    name_o = name_o_entry.get()
    if name_x == "":
        name_x = "Spieler 1"
    if name_o == "":
        name_o = "Spieler 2"
    spieler_label.config(text=f"{name_x}: X\n{name_o}: O")
    startfenster.destroy()
    fenster.deiconify()
    anzeige_aktualisieren()

start_button = tk.Button(startfenster, text="Spiel starten", bg="black", fg="white", font=("Arial", 14), command=spiel_starten)
start_button.pack(pady=20)

spielfeld_frame = tk.Frame(fenster, bg="black")
spielfeld_frame.pack(side="left", expand=True, fill="both")

info_frame = tk.Frame(fenster, bg="black", width=200)
info_frame.pack(side="right", fill="y")

dran_label = tk.Label(info_frame, text="", bg="black", fg="white", font=("Arial", 16))
dran_label.pack(pady=10)

spieler_label = tk.Label(info_frame, text="Spieler 1: X\nSpieler 2: O", bg="black", fg="white", font=("Arial", 14))
spieler_label.pack(pady=10)

punkte_label = tk.Label(info_frame, text="", bg="black", fg="white", font=("Arial", 14))
punkte_label.pack(pady=10)

def anzeige_aktualisieren():
    dran_label.config(text=f"Am Zug:\n{aktueller_spieler}")
    punkte_label.config(text=f"Punkte:\nX: {punkte_x}   O: {punkte_o}")
    gewinner = gewinner_pruefen()
    if gewinner is not None:
        spiel_beenden(gewinner)
    elif alle_felder_voll():
        unentschieden()

def klick1():
    global aktueller_spieler
    button1.config(text=aktueller_spieler, state="disabled")
    if aktueller_spieler == "X":
        aktueller_spieler = "O"
    else:
        aktueller_spieler = "X"
    anzeige_aktualisieren()

def klick2():
    global aktueller_spieler
    button2.config(text=aktueller_spieler, state="disabled")
    if aktueller_spieler == "X":
        aktueller_spieler = "O"
    else:
        aktueller_spieler = "X"
    anzeige_aktualisieren()

def klick3():
    global aktueller_spieler
    button3.config(text=aktueller_spieler, state="disabled")
    if aktueller_spieler == "X":
        aktueller_spieler = "O"
    else:
        aktueller_spieler = "X"
    anzeige_aktualisieren()

def klick4():
    global aktueller_spieler
    button4.config(text=aktueller_spieler, state="disabled")
    if aktueller_spieler == "X":
        aktueller_spieler = "O"
    else:
        aktueller_spieler = "X"
    anzeige_aktualisieren()

def klick5():
    global aktueller_spieler
    button5.config(text=aktueller_spieler, state="disabled")
    if aktueller_spieler == "X":
        aktueller_spieler = "O"
    else:
        aktueller_spieler = "X"
    anzeige_aktualisieren()

def klick6():
    global aktueller_spieler
    button6.config(text=aktueller_spieler, state="disabled")
    if aktueller_spieler == "X":
        aktueller_spieler = "O"
    else:
        aktueller_spieler = "X"
    anzeige_aktualisieren()

def klick7():
    global aktueller_spieler
    button7.config(text=aktueller_spieler, state="disabled")
    if aktueller_spieler == "X":
        aktueller_spieler = "O"
    else:
        aktueller_spieler = "X"
    anzeige_aktualisieren()

def klick8():
    global aktueller_spieler
    button8.config(text=aktueller_spieler, state="disabled")
    if aktueller_spieler == "X":
        aktueller_spieler = "O"
    else:
        aktueller_spieler = "X"
    anzeige_aktualisieren()

def klick9():
    global aktueller_spieler
    button9.config(text=aktueller_spieler, state="disabled")
    if aktueller_spieler == "X":
        aktueller_spieler = "O"
    else:
        aktueller_spieler = "X"
    anzeige_aktualisieren()

def klick10():
    global aktueller_spieler
    button10.config(text=aktueller_spieler, state="disabled")
    if aktueller_spieler == "X":
        aktueller_spieler = "O"
    else:
        aktueller_spieler = "X"
    anzeige_aktualisieren()

def klick11():
    global aktueller_spieler
    button11.config(text=aktueller_spieler, state="disabled")
    if aktueller_spieler == "X":
        aktueller_spieler = "O"
    else:
        aktueller_spieler = "X"
    anzeige_aktualisieren()

def klick12():
    global aktueller_spieler
    button12.config(text=aktueller_spieler, state="disabled")
    if aktueller_spieler == "X":
        aktueller_spieler = "O"
    else:
        aktueller_spieler = "X"
    anzeige_aktualisieren()

def klick13():
    global aktueller_spieler
    button13.config(text=aktueller_spieler, state="disabled")
    if aktueller_spieler == "X":
        aktueller_spieler = "O"
    else:
        aktueller_spieler = "X"
    anzeige_aktualisieren()

def klick14():
    global aktueller_spieler
    button14.config(text=aktueller_spieler, state="disabled")
    if aktueller_spieler == "X":
        aktueller_spieler = "O"
    else:
        aktueller_spieler = "X"
    anzeige_aktualisieren()

def klick15():
    global aktueller_spieler
    button15.config(text=aktueller_spieler, state="disabled")
    if aktueller_spieler == "X":
        aktueller_spieler = "O"
    else:
        aktueller_spieler = "X"
    anzeige_aktualisieren()

def klick16():
    global aktueller_spieler
    button16.config(text=aktueller_spieler, state="disabled")
    if aktueller_spieler == "X":
        aktueller_spieler = "O"
    else:
        aktueller_spieler = "X"
    anzeige_aktualisieren()

button1 = tk.Button(spielfeld_frame, text=" ", font=("Arial", 24), bg="black", fg="white", command=klick1)
button1.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

button2 = tk.Button(spielfeld_frame, text=" ", font=("Arial", 24), bg="black", fg="white", command=klick2)
button2.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)

button3 = tk.Button(spielfeld_frame, text=" ", font=("Arial", 24), bg="black", fg="white", command=klick3)
button3.grid(row=0, column=2, sticky="nsew", padx=5, pady=5)

button4 = tk.Button(spielfeld_frame, text=" ", font=("Arial", 24), bg="black", fg="white", command=klick4)
button4.grid(row=0, column=3, sticky="nsew", padx=5, pady=5)

button5 = tk.Button(spielfeld_frame, text=" ", font=("Arial", 24), bg="black", fg="white", command=klick5)
button5.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)

button6 = tk.Button(spielfeld_frame, text=" ", font=("Arial", 24), bg="black", fg="white", command=klick6)
button6.grid(row=1, column=1, sticky="nsew", padx=5, pady=5)

button7 = tk.Button(spielfeld_frame, text=" ", font=("Arial", 24), bg="black", fg="white", command=klick7)
button7.grid(row=1, column=2, sticky="nsew", padx=5, pady=5)

button8 = tk.Button(spielfeld_frame, text=" ", font=("Arial", 24), bg="black", fg="white", command=klick8)
button8.grid(row=1, column=3, sticky="nsew", padx=5, pady=5)

button9 = tk.Button(spielfeld_frame, text=" ", font=("Arial", 24), bg="black", fg="white", command=klick9)
button9.grid(row=2, column=0, sticky="nsew", padx=5, pady=5)

button10 = tk.Button(spielfeld_frame, text=" ", font=("Arial", 24), bg="black", fg="white", command=klick10)
button10.grid(row=2, column=1, sticky="nsew", padx=5, pady=5)

button11 = tk.Button(spielfeld_frame, text=" ", font=("Arial", 24), bg="black", fg="white", command=klick11)
button11.grid(row=2, column=2, sticky="nsew", padx=5, pady=5)

button12 = tk.Button(spielfeld_frame, text=" ", font=("Arial", 24), bg="black", fg="white", command=klick12)
button12.grid(row=2, column=3, sticky="nsew", padx=5, pady=5)

button13 = tk.Button(spielfeld_frame, text=" ", font=("Arial", 24), bg="black", fg="white", command=klick13)
button13.grid(row=3, column=0, sticky="nsew", padx=5, pady=5)

button14 = tk.Button(spielfeld_frame, text=" ", font=("Arial", 24), bg="black", fg="white", command=klick14)
button14.grid(row=3, column=1, sticky="nsew", padx=5, pady=5)

button15 = tk.Button(spielfeld_frame, text=" ", font=("Arial", 24), bg="black", fg="white", command=klick15)
button15.grid(row=3, column=2, sticky="nsew", padx=5, pady=5)

button16 = tk.Button(spielfeld_frame, text=" ", font=("Arial", 24), bg="black", fg="white", command=klick16)
button16.grid(row=3, column=3, sticky="nsew", padx=5, pady=5)

for i in range(4):
    spielfeld_frame.grid_rowconfigure(i, weight=1)
    spielfeld_frame.grid_columnconfigure(i, weight=1)

buttons = [
    [button1, button2, button3, button4],
    [button5, button6, button7, button8],
    [button9, button10, button11, button12],
    [button13, button14, button15, button16]
]

def drei_gleich(b1, b2, b3):
    return b1["text"] == b2["text"] and b2["text"] == b3["text"] and b1["text"] != " "

def gewinner_pruefen():
    # Waagerecht
    for zeile in range(4):
        if drei_gleich(buttons[zeile][0], buttons[zeile][1], buttons[zeile][2]):
            return [buttons[zeile][0], buttons[zeile][1], buttons[zeile][2]]
        if drei_gleich(buttons[zeile][1], buttons[zeile][2], buttons[zeile][3]):
            return [buttons[zeile][1], buttons[zeile][2], buttons[zeile][3]]

    # Senkrecht
    for spalte in range(4):
        if drei_gleich(buttons[0][spalte], buttons[1][spalte], buttons[2][spalte]):
            return [buttons[0][spalte], buttons[1][spalte], buttons[2][spalte]]
        if drei_gleich(buttons[1][spalte], buttons[2][spalte], buttons[3][spalte]):
            return [buttons[1][spalte], buttons[2][spalte], buttons[3][spalte]]

    # Diagonal von links oben nach rechts unten
    if drei_gleich(buttons[0][0], buttons[1][1], buttons[2][2]):
        return [buttons[0][0], buttons[1][1], buttons[2][2]]
    if drei_gleich(buttons[1][1], buttons[2][2], buttons[3][3]):
        return [buttons[1][1], buttons[2][2], buttons[3][3]]
    if drei_gleich(buttons[0][1], buttons[1][2], buttons[2][3]):
        return [buttons[0][1], buttons[1][2], buttons[2][3]]
    if drei_gleich(buttons[1][0], buttons[2][1], buttons[3][2]):
        return [buttons[1][0], buttons[2][1], buttons[3][2]]

    # Diagonal von rechts oben nach links unten
    if drei_gleich(buttons[0][2], buttons[1][1], buttons[2][0]):
        return [buttons[0][2], buttons[1][1], buttons[2][0]]
    if drei_gleich(buttons[1][3], buttons[2][2], buttons[3][1]):
        return [buttons[1][3], buttons[2][2], buttons[3][1]]
    if drei_gleich(buttons[0][3], buttons[1][2], buttons[2][1]):
        return [buttons[0][3], buttons[1][2], buttons[2][1]]
    if drei_gleich(buttons[1][2], buttons[2][1], buttons[3][0]):
        return [buttons[1][2], buttons[2][1], buttons[3][0]]

    return None

def spiel_beenden(gewinner_buttons):
    global punkte_x, punkte_o
    gewinner = gewinner_buttons[0]["text"]
    if gewinner == "X":
        punkte_x = punkte_x + 1
    else:
        punkte_o = punkte_o + 1
    dran_label.config(text=f"Gewinner: {gewinner}!")
    punkte_label.config(text=f"Punkte:\nX: {punkte_x}   O: {punkte_o}")
    for b in gewinner_buttons:
        b.config(bg="green")
    for zeile in range(4):
        for spalte in range(4):
            buttons[zeile][spalte].config(state="disabled")

def alle_felder_voll():
    for zeile in range(4):
        for spalte in range(4):
            if buttons[zeile][spalte]["text"] == " ":
                return False
    return True

def unentschieden():
    dran_label.config(text="Unentschieden!")
    for zeile in range(4):
        for spalte in range(4):
            buttons[zeile][spalte].config(state="disabled")

def neue_runde():
    global aktueller_spieler
    aktueller_spieler = "X"
    for zeile in range(4):
        for spalte in range(4):
            buttons[zeile][spalte].config(text=" ", state="normal", bg="black")
    anzeige_aktualisieren()

def spielstand_zuruecksetzen():
    global punkte_x, punkte_o
    punkte_x = 0
    punkte_o = 0
    neue_runde()

def programm_beenden():
    fenster.withdraw()
    ergebnis_fenster = tk.Toplevel(fenster)
    ergebnis_fenster.title("Ergebnis")
    ergebnis_fenster.geometry("400x300")
    ergebnis_fenster.configure(bg="black")

    if punkte_x > punkte_o:
        ergebnis_text = f"{name_x} hat gewonnen!"
    elif punkte_o > punkte_x:
        ergebnis_text = f"{name_o} hat gewonnen!"
    else:
        ergebnis_text = "Unentschieden!"

    ergebnis_label = tk.Label(ergebnis_fenster, text=ergebnis_text, bg="black", fg="white", font=("Arial", 28))
    ergebnis_label.pack(pady=30)

    punkte_anzeige_label = tk.Label(ergebnis_fenster, text=f"X: {punkte_x}   O: {punkte_o}", bg="black", fg="white", font=("Arial", 18))
    punkte_anzeige_label.pack(pady=10)

    beenden_button = tk.Button(ergebnis_fenster, text="Beenden", bg="black", fg="white", font=("Arial", 16), command=wirklich_beenden)
    beenden_button.pack(pady=30)

def wirklich_beenden():
    fenster.destroy()

weiter_button = tk.Button(info_frame, text="Weiter", bg="black", fg="white", font=("Arial", 14), command=neue_runde)
weiter_button.pack(pady=10)

reset_button = tk.Button(info_frame, text="Spielstand zurücksetzen", bg="black", fg="white", font=("Arial", 14), command=spielstand_zuruecksetzen)
reset_button.pack(pady=10)

ende_button = tk.Button(info_frame, text="Spiel beenden", bg="black", fg="white", font=("Arial", 14), command=programm_beenden)
ende_button.pack(pady=10)

fenster.mainloop()