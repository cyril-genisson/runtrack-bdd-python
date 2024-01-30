--
-- Author: Cyril GENISSON
-- Created: 30/01/2024
-- Updated: 30/01/2024
--
-- filename: job07.sql
-- Description: 
--

DROP DATABASE IF EXISTS enterprise;
CREATE DATABASE enterprise;

USE enterprise;

CREATE TABLE IF NOT EXISTS employe(
    id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    nom VARCHAR(255) NOT NULL,
    prenom VARCHAR(255) NOT NULL,
    salaire DECIMAL NOT NULL, 
    id_service INT UNSIGNED
);

CREATE TABLE IF NOT EXISTS service(
    id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    nom VARCHAR(255) NOT NULL
);

ALTER TABLE employe
ADD CONSTRAINT fk_service_id
FOREIGN KEY (id_service)
REFERENCES service (id);

