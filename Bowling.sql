DROP DATABASE IF EXISTS bowling;
CREATE DATABASE bowling
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;
USE bowling;
CREATE TABLE turn_ergebnisse (
    id INT AUTO_INCREMENT PRIMARY KEY,
    lane_id INT NOT NULL,
    player_id INT NOT NULL,
    frame INT NOT NULL CHECK (turn_nr BETWEEN 1 AND 10),
    throw1 INT NOT NULL CHECK (wurf1 BETWEEN 0 AND 10),
    throw2 INT NOT NULL CHECK (wurf2 BETWEEN 0 AND 10),
    frame_total INT NOT NULL,
    datum DATETIME DEFAULT CURRENT_TIMESTAMP,
);
