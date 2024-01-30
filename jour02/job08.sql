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

CREATE TABLE animal(
    id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    breed VARCHAR(266) NOT NULL,
    id_box INT UNSIGNED,
    birth DATE,
    country CHAR(3)
);

CREATE TABLE box(
    id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    area INT UNSIGNED NOT NULL,
    capacity INT UNSIGNED NOT NULL
);

ALTER TABLE animal
ADD CONSTRAINT fk_box_id
FOREIGN KEY (id_box)
REFERENCES box (id);

