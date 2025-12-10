import tkinter as tk
import random

window = tk.Tk()
window.title("Linientest")

# Canvas erstellen
canvas = tk.Canvas(window, width=400, height=300, bg="white")
canvas.pack()

# Linie zeichnen: (x1, y1, x2, y2)
# Outline des Spielfelds
canvas.create_line(0, 300, 150, 100, 250, 100, 400, 300, fill="black", width=3)
# hintere Gestrichelte Linie 
canvas.create_line(90, 200, 200, 185, 310, 200, fill="black", dash=(5, 5))
# vordere Gestrichelte Linie 
canvas.create_line(50, 250, 350, 250, fill="black", dash=(7, 1))

# Kegel

pin4L = canvas.create_oval(160, 75, 165, 110, fill="white", tags="leftPins") # 4. Reihe (links)          # ganz hinten
pin4R = canvas.create_oval(235, 75, 240, 110, fill="white", tags="rightPins") # 4. Reihe (rechts)

pin3L = canvas.create_oval(165, 75, 175, 115, fill="white", tags="leftPins") # 3. Reihe (links)
pin3R = canvas.create_oval(225, 75, 235, 115, fill="white", tags="rightPins") # 3. Reihe (rechts)

pin2L = canvas.create_oval(175, 75, 190, 120, fill="white", tags="leftPins") # 2. Reihe (links)
pin2R = canvas.create_oval(210, 75, 225, 120, fill="white", tags="rightPins") # 2. Reihe (rechts)

pin1 = canvas.create_oval(190, 75, 210, 125, fill="white", tags="rightPins") # 1. Kegel ganz vorne

# Bowlingkugel
ball = canvas.create_oval(150, 200, 250, 300, fill="white")

# Startwerte
ball_y = 200
shF = 0   # shortening factor: Kugelgröße verkleinert sich mit der Distanz

def animate_ball():
    global ball_y, shF

    if ball_y > 30: # solange Kugel noch nicht oben
        ball_y -= 10      # Schritt nach oben
        shF += 2         # Kugel kleiner machen
        
        # neue Koordinaten berechnen
        canvas.coords(ball, 150 + shF, ball_y + shF, 250 - shF, ball_y + 100 - shF)
        
        # nächsten Frame planen
        window.after(50, animate_ball)

pin1_X, pin1_Y = random.randint(-50, 50), random.randint(-10, -1)
pin2L_X, pin2L_Y = random.randint(-50, 50), random.randint(-10, -1)
pin2R_X, pin2R_Y = random.randint(-50, 50), random.randint(-10, -1)
pin3L_X, pin3L_Y = random.randint(-50, 50), random.randint(-10, -1)
pin3R_X, pin3R_Y = random.randint(-50, 50), random.randint(-10, -1)
pin4L_X, pin4L_Y = random.randint(-50, 50), random.randint(-10, -1)
pin4R_X, pin4R_Y = random.randint(-50, 50), random.randint(-10, -1)


def animate_pins():  # fertig machen

    canvas.move(pin1, pin1_X, pin1_Y)
    canvas.move(pin2L, pin2L_X, pin2L_Y)
    canvas.move(pin2R, pin2R_X, pin2R_Y)
    canvas.move(pin3L, pin3L_X, pin3L_Y)
    canvas.move(pin3R, pin3R_X, pin3R_Y)
    canvas.move(pin4L, pin4L_X, pin4L_Y)
    canvas.move(pin4R, pin4R_X, pin4R_Y)

    # nächsten Frame planen
    window.after(30, animate_pins)

def show_strike_label():
    tk.Label(window, text="S T R I K E !", fg="red", font=("Arial Black", 40, "bold")).pack()

def move_ball(event):
    if event.keysym == "Up":
        animate_ball()
        window.after(800, animate_pins)
        window.after(800, show_strike_label)

window.bind("<Up>", move_ball) 

window.mainloop()