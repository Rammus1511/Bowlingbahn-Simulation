DROP DATABASE IF EXISTS bowling;
CREATE DATABASE bowling
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;
USE bowling;
CREATE TABLE spieler (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE
);
CREATE TABLE bahnen (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(20) NOT NULL UNIQUE
);
CREATE TABLE turn_ergebnisse (
    id INT AUTO_INCREMENT PRIMARY KEY,
    bahn_id INT NOT NULL,
    spieler_id INT NOT NULL,
    turn_nr INT NOT NULL CHECK (turn_nr BETWEEN 1 AND 10),
    wurf1 INT NOT NULL CHECK (wurf1 BETWEEN 0 AND 10),
    wurf2 INT NOT NULL CHECK (wurf2 BETWEEN 0 AND 10),
    datum DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (bahn_id) REFERENCES bahnen(id),
    FOREIGN KEY (spieler_id) REFERENCES spieler(id)
);
INSERT INTO spieler (name) VALUES
('Spieler 1'),
('Spieler 2'),
('Spieler 3'),
('Spieler 4'),
('Spieler 5'),
('Spieler 6'),
('Spieler 7'),
('Spieler 8');
INSERT INTO bahnen (name) VALUES
('Bahn 1'),
('Bahn 2'),
('Bahn 3'),
('Bahn 4'),
('Bahn 5'),
('Bahn 6'),
('Bahn 7'),
('Bahn 8'),
('Bahn 9'),
('Bahn 10'),
('Bahn 11'),
('Bahn 12');
