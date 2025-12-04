import mysql.connector

# Verbindung zur Datenbank
conn = mysql.connector.connect(
    host="localhost",
    user="dein_user",
    password="dein_passwort",
    database="meine_datenbank"
)

cursor = conn.cursor()

# Score einfügen
sql = "INSERT INTO bowling_scores (spieler_name, bahn_nummer, score) VALUES (%s, %s, %s)"
werte = ("Max Mustermann", 3, 245)

cursor.execute(sql, werte)
conn.commit()

print("Score gespeichert!")

cursor.close()
conn.close()
