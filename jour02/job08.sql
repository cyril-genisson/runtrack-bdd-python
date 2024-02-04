--
-- Author: Cyril GENISSON
-- Created: 30/01/2024
-- Updated: 30/01/2024
--
-- filename: job08.sql
-- Description: 
--

DROP DATABASE IF EXISTS zoo;
CREATE DATABASE zoo;

USE zoo;

CREATE TABLE box(
    id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    area INT UNSIGNED DEFAULT 0,
    capacity INT UNSIGNED DEFAULT 0
) ENGINE = InnoDB;

INSERT INTO box(area, capacity) VALUES (0, 0);
INSERT INTO box(area, capacity) VALUES (3, 5);
INSERT INTO box(area, capacity) VALUES (3, 3);
INSERT INTO box(area, capacity) VALUES (9, 10);
INSERT INTO box(area, capacity) VALUES (8, 4);
INSERT INTO box(area, capacity) VALUES (9, 1);

CREATE TABLE animal(
    id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    breed VARCHAR(266) NOT NULL,
    id_box INT UNSIGNED DEFAULT 1,
    birth DATE DEFAULT '0000-00-00',
    country CHAR(3) DEFAULT 'FR',
    CONSTRAINT `fk_hook_box`
    FOREIGN KEY (id_box) REFERENCES box (id)
    ON UPDATE RESTRICT
) ENGINE = InnoDB;

