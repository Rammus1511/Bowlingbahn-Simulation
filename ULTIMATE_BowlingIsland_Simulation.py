import tkinter as tk
import random
import math
import os
import pyodbc

window = tk.Tk()
window.title("Bowling Simulation")
window.geometry("1920x1080")
window.iconbitmap("bowling_island.ico")
backgroundColor = "burlywood3"
foregroundColor = "black"
window.config(bg=backgroundColor)

welcomeLabel = tk.Label(window, text="Willkommen zur Bowling-Simulation der Bowling Island GmbH!", font=("Arial", 20, "bold"), fg=foregroundColor, bg=backgroundColor, pady=20)
welcomeLabel.pack(side="top", anchor="w", pady=5)

bahnLabel = tk.Label(window, text="Welche Bahnnumer?", bg=backgroundColor)
bahnLabel.pack(side="top", anchor="w", pady=5)

bahnSchieberegler = tk.Scale(window, from_=1, to=12, activebackground="turquoise4", troughcolor="LightCyan3", cursor="hand2", bg=backgroundColor, orient=tk.HORIZONTAL)
bahnSchieberegler.pack(side="top", anchor="w", pady=5)

playerLabel = tk.Label(window, text="Wie viele COM-Spieler sollen simuliert werden?", bg=backgroundColor)
playerLabel.pack(side="top", anchor="w", pady=5)

playerSchieberegler = tk.Scale(window, from_=2, to=4, activebackground="turquoise4", troughcolor="LightCyan3", cursor="hand2", bg=backgroundColor, orient=tk.HORIZONTAL)
playerSchieberegler.pack(side="top", anchor="w", pady=5)

namenFrame = tk.Frame(window)
namenFrame.pack(side="top", anchor="w", pady=5)

playerEntries = []
playerNames = []

#legt fest wie er sich zur SQL-Datenbank verbindet
def get_sqlserver_conn():
    conn_str = (
        "DRIVER={ODBC Driver 18 for SQL Server};"
        f"SERVER={os.getenv('DB_HOST', 'localhost')},{os.getenv('DB_PORT', '1433')};"
        f"DATABASE={os.getenv('DB_NAME', 'bowling')};"
        f"UID={os.getenv('DB_USER', 'appuser')};"
        f"PWD={os.getenv('DB_PASSWORD', 'Pa$$w0rd')};"
        "Encrypt=yes;TrustServerCertificate=yes;"
    )

def update_name_fields(val):
    for widget in namenFrame.winfo_children():
        widget.destroy()
    playerEntries.clear()
    for i in range(int(val)):
        tk.Label(namenFrame, text=f"Name von Spieler {i+1}:       ", bg=backgroundColor).pack(anchor="w")
        entry = tk.Entry(namenFrame, bg="LightCyan3", width=21)
        entry.pack(anchor="w", pady=2)
        playerEntries.append(entry)


playerSchieberegler.config(command=update_name_fields)
update_name_fields(playerSchieberegler.get())

startButton = tk.Button(window, text="Simulation starten", activebackground="turquoise4", cursor="hand2")
startButton.pack(side="top", anchor="w", pady=5)

activePlayerLabel = tk.Label(window, text="Geben Sie die Spielernamen ein um fortzufahren.", font=("Arial", 15, "bold"), fg=foregroundColor, bg=backgroundColor)
activePlayerLabel.pack(side="top", anchor="n")

# Canvas – Bowlingbahn
canvas = tk.Canvas(window, width=600, height=600, bg="burlywood3", highlightthickness=5, highlightbackground="sienna4")
canvas.pack(side="left", padx=20)

# Bahnbegrenzung
canvas.create_rectangle(0,0,50,600, fill="tan3", outline="sienna4", width=5)
canvas.create_rectangle(559,0,609,600, fill="tan3", outline="sienna4", width=5)

#########################################
#  SCOREBOARD – KLASSISCHER LOOK
#########################################

scoreboardFrame = tk.Frame(window, bg="white", bd=4, relief="solid")
scoreboardFrame.pack(side="right", fill="y", padx=20, pady=20)

scoreboard_labels = []
player_scores = []
frames_per_player = 10


def build_scoreboard():
    """Erzeugt ein klassisches Bowlingcenter-Scoreboard."""
    for widget in scoreboardFrame.winfo_children():
        widget.destroy()

    # Titel
    title = tk.Label(scoreboardFrame, text="SCOREBOARD", font=("Arial", 18, "bold"), fg="black", bg="white")
    title.grid(row=0, column=0, columnspan=frames_per_player + 1, pady=10)

    # Frame-Nummern
    tk.Label(scoreboardFrame, text="Spieler", font=("Arial", 12, "bold"), bg="white", bd=2, relief="solid", width=10).grid(row=1, column=0)

    for f in range(frames_per_player):
        tk.Label(scoreboardFrame, text=f"Runde {f+1}",
                 font=("Arial", 10, "bold"), bg="white",
                 bd=2, relief="solid", width=12).grid(row=1, column=f + 1)

    # Spielerzeilen
    scoreboard_labels.clear()
    for p, name in enumerate(playerNames):
        row_labels = []

        nameLabel = tk.Label(scoreboardFrame, text=name, font=("Arial", 12, "bold"), bg="white", bd=2, relief="solid", width=10)
        nameLabel.grid(row=p + 2, column=0)

        for f in range(frames_per_player):
            frameBox = tk.Frame(scoreboardFrame, bg="white", bd=2, relief="solid")
            frameBox.grid(row=p + 2, column=f + 1, padx=1, pady=1)

            t1 = tk.Label(frameBox, text="", font=("Arial", 10), width=4, bg="white")
            t2 = tk.Label(frameBox, text="", font=("Arial", 10), width=4, bg="white")
            s = tk.Label(frameBox, text="", font=("Arial", 10, "bold"), bg="white")

            t1.grid(row=0, column=0)
            t2.grid(row=0, column=1)
            s.grid(row=1, column=0, columnspan=2)

            row_labels.append({"t1": t1, "t2": t2, "sum": s})

        scoreboard_labels.append(row_labels)


def reset_scores():
    global player_scores
    player_scores = []
    for _ in playerNames:
        player_scores.append([[None, None, 0] for _ in range(frames_per_player)])

def upsert_frame_score(player_name: str, lane: int, frame: int, throw1: int, throw2: int, frame_total: int):
    sql = """
        MERGE dbo.turn_ergebnisse AS target
        USING (VALUES (?, ?, ?, ?, ?, ?)) AS src (player_id, lane_id, frame, throw1, throw2, frame_total)
        ON target.player_id = src.player_id
        AND target.lane_id = src.lane_id
        AND target.frame = src.frame
        WHEN MATCHED THEN
        UPDATE SET
        target.throw1 = src.throw1
        target.throw2 = src.throw2
        target.frame_total = src.frame_total
        WHEN NOT MATCHED THEN
        INSERT (player_id, lane_id, frame, throw1, throw2, frame_total)
        VALUES (src.player_id, src.lane_id, src.frame, src.throw1, src.throw2, src.frame_total);
        """
    conn = None
    try:
        conn = get_sqlserver_conn()
        cur = conn.cursor()
        cur.execute(sql, (lane, player_name, frame, throw1, throw2, frame_total))
        conn.commit()
    except Exception:
        if conn:
            conn.rollback()
        raise
    finally:
        if conn:
            conn.close()

def update_scoreboard(player, frame, throw_index, fallen_pins):
    frame_data = player_scores[player][frame]
    frame_data[throw_index] = fallen_pins

    total = 0
    for i in range(frames_per_player):
        f0 = player_scores[player][i][0] or 0
        f1 = player_scores[player][i][1] or 0
        total += f0 + f1
        #TODO here sql logic for saving data (Player, Bahn, Frame, Throw1, Throw2, Zwischenergebnis)
        
        if i == frame:
            throw1 = frame_data[0] or 0 
            throw2 = frame_data[1] or 0
            break
        
        upsert_frame_score(player, bahnSchieberegler.get, frame, throw1, throw2, total)
        break
        

    frame_data[2] = total

    labels = scoreboard_labels[player][frame]
    labels["t1"].config(text=str(frame_data[0] or 0))
    labels["t2"].config(text=str(frame_data[1] or 0))
    labels["sum"].config(text=str(total))


#########################################
#  BOWLING-FUNKTIONEN
#########################################

pins = []
ball_x, ball_y = 300, 500
ball_radius = 20
ball_dx, ball_dy = 0, 0

Colors = ["turquoise3", "firebrick3", "SpringGreen3", "goldenrod1"]
OutlineColors = ["turquoise4", "firebrick4", "SpringGreen4", "goldenrod4"]

currentPlayer = 0
currentThrow = 1
pins_hit_this_throw = 0

ball = canvas.create_oval(ball_x - ball_radius, ball_y - ball_radius, ball_x + ball_radius, ball_y + ball_radius, fill=Colors[currentPlayer], outline=OutlineColors[currentPlayer], width=5)

throws_done = []
players_active = []

pause_between_throws_ms = 800
total_throws_per_player = 20


def draw_pins():
    global pins
    for (pid, _, _, _) in pins:
        canvas.delete(pid)
    pins.clear()

    r = 12
    x_start = 300
    y_start = 300

    formation = [
        [(0, 0)],
        [(-30, -60), (30, -60)],
        [(-60, -120), (0, -120), (60, -120)],
        [(-90, -180), (-30, -180), (30, -180), (90, -180)],
    ]

    for row in formation:
        for dx, dy in row:
            x = x_start + dx
            y = y_start + dy
            pin_id = canvas.create_oval(x - r, y - r, x + r, y + r, fill="white", outline="red", width=3)
            pins.append((pin_id, x, y, r))


draw_pins()


def update_active_player_label():
    if playerNames:
        activePlayerLabel.config(text=f"{playerNames[currentPlayer]} | {currentThrow}. Wurf ({throws_done[currentPlayer]}/{total_throws_per_player})")
    else:
        activePlayerLabel.config(text="Noch keine Spielernamen eingegeben...", fg=foregroundColor)


def check_collision():
    global pins, pins_hit_this_throw, scores
    hit = []

    for (pid, px, py, pr) in pins:
        if math.hypot(ball_x - px, ball_y - py) < ball_radius + pr:
            hit.append(pid)

    if hit:
        for pid in hit:
            canvas.delete(pid)
        pins_hit_this_throw += len(hit)
        pins = [p for p in pins if p[0] not in hit]

def move_ball():
    global ball_x, ball_y, ball_dx, ball_dy

    if ball_dx == 0 and ball_dy == 0:
        window.after(10, move_ball)
        return

    ball_x += ball_dx
    ball_y += ball_dy

    canvas.move(ball, ball_dx, ball_dy)

    check_collision()

    if ball_y < -50:
        ball_dx = ball_dy = 0
        canvas.coords(ball, 300 - ball_radius, 500 - ball_radius, 300 + ball_radius, 500 + ball_radius)
        window.after(pause_between_throws_ms, handle_end_of_throw)

    window.after(10, move_ball)


def handle_end_of_throw():
    global currentThrow, pins_hit_this_throw, throws_done

    throws_done[currentPlayer] += 1

    frame = (throws_done[currentPlayer] - 1) // 2
    throw_index = 0 if currentThrow == 1 else 1

    update_scoreboard(currentPlayer, frame, throw_index, pins_hit_this_throw)

    pins_hit_this_throw = 0

    if currentThrow == 2:
        draw_pins()
        currentThrow = 1
        next_player()
    else:
        currentThrow = 2

    update_active_player_label()
    prepare_throw()

def next_player():
    global currentPlayer
    currentPlayer = (currentPlayer + 1) % len(playerNames)


def prepare_throw():
    global ball_x, ball_y, ball_dx, ball_dy

    ball_x, ball_y = 300, 500
    canvas.coords(ball, ball_x - ball_radius, ball_y - ball_radius, ball_x + ball_radius, ball_y + ball_radius)
    canvas.itemconfig(ball, fill=Colors[currentPlayer], outline=OutlineColors[currentPlayer])

    ball_dx = random.uniform(-2, 2)
    ball_dy = -7


def start_simulation():
    global button_not_pressed_before, playerNames, currentPlayer, currentThrow, ball_dx, ball_dy, throws_done, players_active, scores
    # Nur wenn der Startbutton noch nicht zuvor gedrückt wurde
    if button_not_pressed_before == True:
        button_not_pressed_before = False

        n = playerSchieberegler.get()
        playerNames[:] = [
            (playerEntries[i].get().strip() or f"Spieler {i+1}")
            for i in range(n)
        ]

        throws_done = [0] * n
        players_active = [True] * n

        build_scoreboard()
        reset_scores()

        draw_pins()
        prepare_throw()
        update_active_player_label()
        move_ball()

button_not_pressed_before = True
startButton.config(command=start_simulation)

window.mainloop()



