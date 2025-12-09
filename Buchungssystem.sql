DROP DATABASE IF EXISTS bowling_reservierung;
CREATE DATABASE bowling_reservierung
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;
USE bowling_reservierung;

CREATE TABLE bahnen (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(20) NOT NULL UNIQUE
);

CREATE TABLE reservierungen (
    id INT AUTO_INCREMENT PRIMARY KEY,
    datum DATE NOT NULL,
    startzeit TIME NOT NULL,
    personen INT NOT NULL CHECK (personen BETWEEN 1 AND 8),
    bezahloption ENUM('Bargeld','Karte') NOT NULL,
    vorname VARCHAR(50) NOT NULL,
    nachname VARCHAR(50) NOT NULL,
    kunde VARCHAR(101),
    handynummer VARCHAR(20),
    email VARCHAR(100),
    notiz TEXT,
    erstellt_am DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE reservierung_bahnen (
    id INT AUTO_INCREMENT PRIMARY KEY,
    reservierung_id INT NOT NULL,
    bahn_id INT NOT NULL,
    FOREIGN KEY (reservierung_id) REFERENCES reservierungen(id),
    FOREIGN KEY (bahn_id) REFERENCES bahnen(id)
);

INSERT INTO bahnen (name) VALUES
('Bahn 1'),('Bahn 2'),('Bahn 3'),('Bahn 4'),
('Bahn 5'),('Bahn 6'),('Bahn 7'),('Bahn 8'),
('Bahn 9'),('Bahn 10'),('Bahn 11'),('Bahn 12');

DELIMITER $$
CREATE TRIGGER trg_set_kunde
BEFORE INSERT ON reservierungen
FOR EACH ROW
BEGIN
  SET NEW.kunde = TRIM(CONCAT(
    IFNULL(NEW.vorname, ''),
    ' ',
    IFNULL(NEW.nachname, '')
  ));
END $$
DELIMITER ;
