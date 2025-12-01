import tkinter as tk

frame = tk.Tk()
frame.title("Bowling Scoreboard")
frame.geometry("960x540+960+0")  # oben rechts, halbe FullHD-Größe

players = ["Anna", "Ben", "Chris", "Dana"]
runden = list(range(1, 11))

# Kopfzeile
tk.Label(frame, text="Spieler", borderwidth=2, relief="ridge", width=10, anchor="center").grid(row=0, column=0, sticky="nsew")
for c, r in enumerate(runden, start=1):
    tk.Label(frame, text=f"Runde {r}", borderwidth=2, relief="ridge", width=10, anchor="center").grid(row=0, column=c, sticky="nsew")
tk.Label(frame, text="Gesamt", borderwidth=2, relief="ridge", width=10, anchor="center").grid(row=0, column=len(runden)+1, sticky="nsew")

# Beispielwerte: ((wurf1, wurf2), punkte)
scores = [
    [(("2","3"), 5), (("X",""), 10), (("9","/"), 15), (("7","2"), 9), (("X",""), 10),
     (("8","1"), 9), (("9","/"), 15), (("X",""), 10), (("7","2"), 9), (("X",""), 10)],  # Anna
    [(("8","1"), 9), (("9","/"), 15), (("X",""), 10), (("7","2"), 9), (("X",""), 10),
     (("8","1"), 9), (("9","/"), 15), (("X",""), 10), (("7","2"), 9), (("X",""), 10)],  # Ben
    [(("7","2"), 9), (("8","1"), 9), (("X",""), 10), (("9","/"), 15), (("X",""), 10),
     (("7","2"), 9), (("8","1"), 9), (("X",""), 10), (("9","/"), 15), (("X",""), 10)],  # Chris
    [(("9","/"), 15), (("X",""), 10), (("7","2"), 9), (("8","1"), 9), (("X",""), 10),
     (("9","/"), 15), (("X",""), 10), (("7","2"), 9), (("8","1"), 9), (("X",""), 10)]   # Dana
]

# Tabelle füllen
for r, player in enumerate(players, start=1):
    tk.Label(frame, text=player, borderwidth=2, relief="ridge", anchor="center").grid(row=r, column=0, sticky="nsew")

    total = 0
    for c, val in enumerate(scores[r-1], start=1):
        (wurf1, wurf2), punkte = val
        total += punkte

        # Hauptzelle
        cell = tk.Frame(frame, borderwidth=2, relief="ridge")
        cell.grid(row=r, column=c, padx=1, pady=1, sticky="nsew")

        # Oberer Bereich mit zwei kleinen Kästchen nebeneinander
        top_box = tk.Frame(cell)
        top_box.pack(fill="x")
        tk.Label(top_box, text=wurf1, font=("Arial", 8), borderwidth=2, relief="ridge", width=3).pack(side="left", fill="x", expand=True)
        tk.Label(top_box, text=wurf2, font=("Arial", 8), borderwidth=2, relief="ridge", width=3).pack(side="left", fill="x", expand=True)

        # Unterer Bereich für akkumulierte Punkte
        bottom_box = tk.Frame(cell, borderwidth=2, relief="ridge")
        bottom_box.pack(fill="both", expand=True)
        tk.Label(bottom_box, text=total, font=("Arial", 12, "bold"), anchor="center").pack(fill="both", expand=True)

    # Gesamtscore rechts
    tk.Label(frame, text=total, borderwidth=2, relief="ridge", anchor="center", font=("Arial", 12, "bold")).grid(row=r, column=len(runden)+1, sticky="nsew")

# Grid skalierbar machen
total_rows = 1 + len(players)
total_cols = 1 + len(runden) + 1
for i in range(total_rows):
    frame.rowconfigure(i, weight=1)
for j in range(total_cols):
    frame.columnconfigure(j, weight=1)

frame.mainloop()
