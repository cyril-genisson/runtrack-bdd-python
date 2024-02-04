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

CREATE TABLE service(
    id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    nom VARCHAR(255) NOT NULL
) ENGINE = InnoDB;

INSERT INTO service(nom) VALUES ('Unassigned');

CREATE TABLE employe(
    id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    nom VARCHAR(255) NOT NULL,
    prenom VARCHAR(255) NOT NULL,
    salaire DECIMAL(6, 2) DEFAULT 0.00, 
    id_service INT UNSIGNED DEFAULT 1,
    CONSTRAINT `fk_hook_service`
    FOREIGN KEY (id_service) REFERENCES service (id)
    ON DELETE CASCADE
    ON UPDATE RESTRICT
) ENGINE = InnoDB;

