import tkinter as tk

frame = tk.Tk()
frame.title("Bowling Scoreboard")
frame.geometry("960x540+960+0")

players = ["Anna", "Ben", "Chris", "Dana"]
runden = list(range(1, 11))

tk.Label(frame, text="Spieler", borderwidth=2, relief="ridge", width=10, anchor="center").grid(row=0, column=0, sticky="nsew")
for c, r in enumerate(runden, start=1):
    tk.Label(frame, text=f"Runde {r}", borderwidth=2, relief="ridge", width=10, anchor="center").grid(row=0, column=c, sticky="nsew")
tk.Label(frame, text="Gesamt", borderwidth=2, relief="ridge", width=10, anchor="center").grid(row=0, column=len(runden)+1, sticky="nsew")

#ask SQL database for turn data
SQLThrow1 = 10
SQLThrow2 = 2
SQLTurn = 1
SQLPlayer = "Finn"

#Player decleration
Player1 = "Finn"
Player2 = "Thomas"
Player3 = "Null"
Player4 = "Null"

P1Turn1Throw1 = 0
P1Turn1Throw2 = 0
P1Turn1Sum = 0
P1Turn2Throw1 = 0
P1Turn2Throw2 = 0
P1Turn2Sum = 0
P1Turn3Throw1 = 0
P1Turn3Throw2 = 0
P1Turn3Sum = 0
P1Turn4Throw1 = 0
P1Turn4Throw2 = 0
P1Turn4Sum = 0
P1Turn5Throw1 = 0
P1Turn5Throw2 = 0
P1Turn5Sum = 0
P1Turn6Throw1 = 0
P1Turn6Throw2 = 0
P1Turn6Sum = 0
P1Turn7Throw1 = 0
P1Turn7Throw2 = 0
P1Turn7Sum = 0
P1Turn8Throw1 = 0
P1Turn8Throw2 = 0
P1Turn8Sum = 0
P1Turn9Throw1 = 0
P1Turn9Throw2 = 0
P1Turn9Sum = 0
P1Turn10Throw1 = 0
P1Turn10Throw2 = 0
P1Turn10Sum = 0

P2Turn1Throw1 = 0
P2Turn1Throw2 = 0
P2Turn1Sum = 0
P2Turn2Throw1 = 0
P2Turn2Throw2 = 0
P2Turn2Sum = 0
P2Turn3Throw1 = 0
P2Turn3Throw2 = 0
P2Turn3Sum = 0
P2Turn4Throw1 = 0
P2Turn4Throw2 = 0
P2Turn4Sum = 0
P2Turn5Throw1 = 0
P2Turn5Throw2 = 0
P2Turn5Sum = 0
P2Turn6Throw1 = 0
P2Turn6Throw2 = 0
P2Turn6Sum = 0
P2Turn7Throw1 = 0
P2Turn7Throw2 = 0
P2Turn7Sum = 0
P2Turn8Throw1 = 0
P2Turn8Throw2 = 0
P2Turn8Sum = 0
P2Turn9Throw1 = 0
P2Turn9Throw2 = 0
P2Turn9Sum = 0
P2Turn10Throw1 = 0
P2Turn10Throw2 = 0
P2Turn10Sum = 0

P3Turn1Throw1 = 0
P3Turn1Throw2 = 0
P3Turn1Sum = 0
P3Turn2Throw1 = 0
P3Turn2Throw2 = 0
P3Turn2Sum = 0
P3Turn3Throw1 = 0
P3Turn3Throw2 = 0
P3Turn3Sum = 0
P3Turn4Throw1 = 0
P3Turn4Throw2 = 0
P3Turn4Sum = 0
P3Turn5Throw1 = 0
P3Turn5Throw2 = 0
P3Turn5Sum = 0
P3Turn6Throw1 = 0
P3Turn6Throw2 = 0
P3Turn6Sum = 0
P3Turn7Throw1 = 0
P3Turn7Throw2 = 0
P3Turn7Sum = 0
P3Turn8Throw1 = 0
P3Turn8Throw2 = 0
P3Turn8Sum = 0
P3Turn9Throw1 = 0
P3Turn9Throw2 = 0
P3Turn9Sum = 0
P3Turn10Throw1 = 0
P3Turn10Throw2 = 0
P3Turn10Sum = 0

P4Turn1Throw1 = 0
P4Turn1Throw2 = 0
P4Turn1Sum = 0
P4Turn2Throw1 = 0
P4Turn2Throw2 = 0
P4Turn2Sum = 0
P4Turn3Throw1 = 0
P4Turn3Throw2 = 0
P4Turn3Sum = 0
P4Turn4Throw1 = 0
P4Turn4Throw2 = 0
P4Turn4Sum = 0
P4Turn5Throw1 = 0
P4Turn5Throw2 = 0
P4Turn5Sum = 0
P4Turn6Throw1 = 0
P4Turn6Throw2 = 0
P4Turn6Sum = 0
P4Turn7Throw1 = 0
P4Turn7Throw2 = 0
P4Turn7Sum = 0
P4Turn8Throw1 = 0
P4Turn8Throw2 = 0
P4Turn8Sum = 0
P4Turn9Throw1 = 0
P4Turn9Throw2 = 0
P4Turn9Sum = 0
P4Turn10Throw1 = 0
P4Turn10Throw2 = 0
P4Turn10Sum = 0

match SQLTurn:
    #Turn1
    case "1":
        if(SQLPlayer == Player1):
            P1Turn1Throw1 = SQLThrow1
            P1Turn1Throw2 = SQLThrow2
            P1Turn1Sum = P1Turn1Throw1 + P1Turn1Throw2
        elif(SQLPlayer == Player2):
            P2Turn1Throw1 = SQLThrow1
            P2Turn1Throw2 = SQLThrow2
            P2Turn1Sum = P2Turn1Throw1 + P2Turn1Throw2
        elif(SQLPlayer == Player3):
            P3Turn1Throw1 = SQLThrow1
            P3Turn1Throw2 = SQLThrow2
            P3Turn1Sum = P3Turn1Throw1 + P3Turn1Throw2
        elif(SQLPlayer == Player4):
            P4Turn1Throw1 = SQLThrow1
            P4Turn1Throw2 = SQLThrow2
            P4Turn1Sum = P4Turn1Throw1 + P4Turn1Throw2
    #Turn2
    case "2":
        if(SQLPlayer == Player1):
            P1Turn2Throw1 = SQLThrow1
            P1Turn2Throw2 = SQLThrow2
            P1Turn2Sum = P1Turn2Throw1 + P1Turn2Throw2 + P1Turn1Sum
        elif(SQLPlayer == Player2):
            P2Turn2Throw1 = SQLThrow1
            P2Turn2Throw2 = SQLThrow2
            P2Turn2Sum = P2Turn2Throw1 + P2Turn2Throw2 + P2Turn1Sum
        elif(SQLPlayer == Player3):
            P3Turn2Throw1 = SQLThrow1
            P3Turn2Throw2 = SQLThrow2
            P3Turn2Sum = P3Turn2Throw1 + P3Turn2Throw2 + P3Turn1Sum
        elif(SQLPlayer == Player4):
            P4Turn2Throw1 = SQLThrow1
            P4Turn2Throw2 = SQLThrow2
            P4Turn2Sum = P4Turn2Throw1 + P4Turn2Throw2 + P4Turn1Sum
    #Turn3
    case "3":
        if(SQLPlayer == Player1):
            P1Turn3Throw1 = SQLThrow1
            P1Turn3Throw2 = SQLThrow2
            P1Turn3Sum = P1Turn3Throw1 + P1Turn3Throw2 + P1Turn2Sum
        elif(SQLPlayer == Player2):
            P2Turn3Throw1 = SQLThrow1
            P2Turn3Throw2 = SQLThrow2
            P2Turn3Sum = P2Turn3Throw1 + P2Turn3Throw2 + P2Turn2Sum
        elif(SQLPlayer == Player3):
            P3Turn3Throw1 = SQLThrow1
            P3Turn3Throw2 = SQLThrow2
            P3Turn3Sum = P3Turn3Throw1 + P3Turn3Throw2 + P3Turn2Sum
        elif(SQLPlayer == Player4):
            P4Turn3Throw1 = SQLThrow1
            P4Turn3Throw2 = SQLThrow2
            P4Turn3Sum = P4Turn3Throw1 + P4Turn3Throw2 + P4Turn2Sum
    #Turn4
    case "4":
        if(SQLPlayer == Player1):
            P1Turn4Throw1 = SQLThrow1
            P1Turn4Throw2 = SQLThrow2
            P1Turn4Sum = P1Turn4Throw1 + P1Turn4Throw2 + P1Turn3Sum
        elif(SQLPlayer == Player2):
            P2Turn4Throw1 = SQLThrow1
            P2Turn4Throw2 = SQLThrow2
            P2Turn4Sum = P2Turn4Throw1 + P2Turn4Throw2 + P2Turn3Sum
        elif(SQLPlayer == Player3):
            P3Turn4Throw1 = SQLThrow1
            P3Turn4Throw2 = SQLThrow2
            P3Turn4Sum = P3Turn4Throw1 + P3Turn4Throw2 + P3Turn3Sum
        elif(SQLPlayer == Player4):
            P4Turn4Throw1 = SQLThrow1
            P4Turn4Throw2 = SQLThrow2
            P4Turn4Sum = P4Turn4Throw1 + P4Turn4Throw2 + P4Turn3Sum
    #Turn5
    case "5":
        if(SQLPlayer == Player1):
            P1Turn5Throw1 = SQLThrow1
            P1Turn5Throw2 = SQLThrow2
            P1Turn5Sum = P1Turn5Throw1 + P1Turn5Throw2 + P1Turn4Sum
        elif(SQLPlayer == Player2):
            P2Turn5Throw1 = SQLThrow1
            P2Turn5Throw2 = SQLThrow2
            P2Turn5Sum = P2Turn5Throw1 + P2Turn5Throw2 + P2Turn4Sum
        elif(SQLPlayer == Player3):
            P3Turn5Throw1 = SQLThrow1
            P3Turn5Throw2 = SQLThrow2
            P3Turn5Sum = P3Turn5Throw1 + P3Turn5Throw2 + P3Turn4Sum
        elif(SQLPlayer == Player4):
            P4Turn5Throw1 = SQLThrow1
            P4Turn5Throw2 = SQLThrow2
            P4Turn5Sum = P4Turn5Throw1 + P4Turn5Throw2 + P4Turn4Sum
    #Turn6
    case "6":
        if(SQLPlayer == Player1):
            P1Turn6Throw1 = SQLThrow1
            P1Turn6Throw2 = SQLThrow2
            P1Turn6Sum = P1Turn6Throw1 + P1Turn6Throw2 + P1Turn5Sum
        elif(SQLPlayer == Player2):
            P2Turn6Throw1 = SQLThrow1
            P2Turn6Throw2 = SQLThrow2
            P2Turn6Sum = P2Turn6Throw1 + P2Turn6Throw2 + P2Turn5Sum
        elif(SQLPlayer == Player3):
            P3Turn6Throw1 = SQLThrow1
            P3Turn6Throw2 = SQLThrow2
            P3Turn6Sum = P3Turn6Throw1 + P3Turn6Throw2 + P3Turn5Sum
        elif(SQLPlayer == Player4):
            P4Turn6Throw1 = SQLThrow1
            P4Turn6Throw2 = SQLThrow2
            P4Turn6Sum = P4Turn6Throw1 + P4Turn6Throw2 + P4Turn5Sum 
    #Turn7
    case "7":
        if(SQLPlayer == Player1):
            P1Turn7Throw1 = SQLThrow1
            P1Turn7Throw2 = SQLThrow2
            P1Turn7Sum = P1Turn7Throw1 + P1Turn7Throw2 + P1Turn6Sum
        elif(SQLPlayer == Player2):
            P2Turn7Throw1 = SQLThrow1
            P2Turn7Throw2 = SQLThrow2
            P2Turn7Sum = P2Turn7Throw1 + P2Turn7Throw2 + P2Turn6Sum
        elif(SQLPlayer == Player3):
            P3Turn7Throw1 = SQLThrow1
            P3Turn7Throw2 = SQLThrow2
            P3Turn7Sum = P3Turn7Throw1 + P3Turn7Throw2 + P3Turn6Sum
        elif(SQLPlayer == Player4):
            P4Turn7Throw1 = SQLThrow1
            P4Turn7Throw2 = SQLThrow2
            P4Turn7Sum = P4Turn7Throw1 + P4Turn7Throw2 + P4Turn6Sum
    #Turn8
    case "8":
        if(SQLPlayer == Player1):
            P1Turn8Throw1 = SQLThrow1
            P1Turn8Throw2 = SQLThrow2
            P1Turn8Sum = P1Turn8Throw1 + P1Turn8Throw2 + P1Turn7Sum
        elif(SQLPlayer == Player2):
            P2Turn8Throw1 = SQLThrow1
            P2Turn8Throw2 = SQLThrow2
            P2Turn8Sum = P2Turn8Throw1 + P2Turn8Throw2 + P2Turn7Sum
        elif(SQLPlayer == Player3):
            P3Turn8Throw1 = SQLThrow1
            P3Turn8Throw2 = SQLThrow2
            P3Turn8Sum = P3Turn8Throw1 + P3Turn8Throw2 + P3Turn7Sum
        elif(SQLPlayer == Player4):
            P4Turn8Throw1 = SQLThrow1
            P4Turn8Throw2 = SQLThrow2
            P4Turn8Sum = P4Turn8Throw1 + P4Turn8Throw2 + P4Turn7Sum
    #Turn9
    case "9":
        if(SQLPlayer == Player1):
            P1Turn9Throw1 = SQLThrow1
            P1Turn9Throw2 = SQLThrow2
            P1Turn9Sum = P1Turn9Throw1 + P1Turn9Throw2 + P1Turn8Sum
        elif(SQLPlayer == Player2):
            P2Turn9Throw1 = SQLThrow1
            P2Turn9Throw2 = SQLThrow2
            P2Turn9Sum = P2Turn9Throw1 + P2Turn9Throw2 + P2Turn8Sum
        elif(SQLPlayer == Player3):
            P3Turn9Throw1 = SQLThrow1
            P3Turn9Throw2 = SQLThrow2
            P3Turn9Sum = P3Turn9Throw1 + P3Turn9Throw2 + P3Turn8Sum
        elif(SQLPlayer == Player4):
            P4Turn9Throw1 = SQLThrow1
            P4Turn9Throw2 = SQLThrow2
            P4Turn9Sum = P4Turn9Throw1 + P4Turn9Throw2 + P4Turn8Sum
    #Turn10
    case "10":
        if(SQLPlayer == Player1):
            P1Turn10Throw1 = SQLThrow1
            P1Turn10Throw2 = SQLThrow2
            P1Turn10Sum = P1Turn10Throw1 + P1Turn10Throw2 + P1Turn9Sum
        elif(SQLPlayer == Player2):
            P2Turn10Throw1 = SQLThrow1
            P2Turn10Throw2 = SQLThrow2
            P2Turn10Sum = P2Turn10Throw1 + P2Turn10Throw2 + P2Turn9Sum
        elif(SQLPlayer == Player3):
            P3Turn10Throw1 = SQLThrow1
            P3Turn10Throw2 = SQLThrow2
            P3Turn10Sum = P3Turn10Throw1 + P3Turn10Throw2 + P3Turn9Sum
        elif(SQLPlayer == Player4):
            P4Turn10Throw1 = SQLThrow1
            P4Turn10Throw2 = SQLThrow2
            P4Turn10Sum = P4Turn10Throw1 + P4Turn10Throw2 + P4Turn9Sum

scores = [
    #Player1
    [((P1Turn1Throw1, P1Turn1Throw2), P1Turn1Sum), ((P1Turn2Throw1, P1Turn2Throw2), P1Turn2Sum),
     ((P1Turn3Throw1, P1Turn3Throw2), P1Turn3Sum), ((P1Turn4Throw1, P1Turn4Throw2), P1Turn4Sum), 
     ((P1Turn5Throw1, P1Turn5Throw2), P1Turn5Sum), ((P1Turn6Throw1, P1Turn6Throw2), P1Turn6Sum), 
     ((P1Turn7Throw1, P1Turn7Throw2), P1Turn7Sum), ((P1Turn8Throw1, P1Turn8Throw2), P1Turn8Sum), 
     ((P1Turn9Throw1, P1Turn9Throw2), P1Turn9Sum), ((P1Turn10Throw1,P1Turn10Throw2), P1Turn10Sum)],
    
    #Player2
    [((P2Turn1Throw1, P2Turn1Throw2), P2Turn1Sum), ((P2Turn2Throw1, P2Turn2Throw2), P2Turn2Sum),
     ((P2Turn3Throw1, P2Turn3Throw2), P2Turn3Sum), ((P2Turn4Throw1, P2Turn4Throw2), P2Turn4Sum), 
     ((P2Turn5Throw1, P2Turn5Throw2), P2Turn5Sum), ((P2Turn6Throw1, P2Turn6Throw2), P2Turn6Sum), 
     ((P2Turn7Throw1, P2Turn7Throw2), P2Turn7Sum), ((P2Turn8Throw1, P2Turn8Throw2), P2Turn8Sum), 
     ((P2Turn9Throw1, P2Turn9Throw2), P2Turn9Sum), ((P2Turn10Throw1,P2Turn10Throw2), P2Turn10Sum)],

    #Player3
    [((P3Turn1Throw1, P3Turn1Throw2), P3Turn1Sum), ((P3Turn2Throw1, P3Turn2Throw2), P3Turn2Sum),
     ((P3Turn3Throw1, P3Turn3Throw2), P3Turn3Sum), ((P3Turn4Throw1, P3Turn4Throw2), P3Turn4Sum), 
     ((P3Turn5Throw1, P3Turn5Throw2), P3Turn5Sum), ((P3Turn6Throw1, P3Turn6Throw2), P3Turn6Sum), 
     ((P3Turn7Throw1, P3Turn7Throw2), P3Turn7Sum), ((P3Turn8Throw1, P3Turn8Throw2), P3Turn8Sum), 
     ((P3Turn9Throw1, P3Turn9Throw2), P3Turn9Sum), ((P3Turn10Throw1,P3Turn10Throw2), P3Turn10Sum)],

    #Player4
    [((P4Turn1Throw1, P4Turn1Throw2), P4Turn1Sum), ((P4Turn2Throw1, P4Turn2Throw2), P4Turn2Sum),
     ((P4Turn3Throw1, P4Turn3Throw2), P4Turn3Sum), ((P4Turn4Throw1, P4Turn4Throw2), P4Turn4Sum), 
     ((P4Turn5Throw1, P4Turn5Throw2), P4Turn5Sum), ((P4Turn6Throw1, P4Turn6Throw2), P4Turn6Sum), 
     ((P4Turn7Throw1, P4Turn7Throw2), P4Turn7Sum), ((P4Turn8Throw1, P4Turn8Throw2), P4Turn8Sum), 
     ((P4Turn9Throw1, P4Turn9Throw2), P4Turn9Sum), ((P4Turn10Throw1,P4Turn10Throw2), P4Turn10Sum)]
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
