--
-- Author: Cyril GENISSON
-- Created: 29/01/2024
-- Updated: 29/01/2024
--
-- filename: job03.sql
-- Description: 
--

USE LaPlateforme;

CREATE TABLE etudiant (
    id INT AUTO_INCREMENT,
    nom VARCHAR(255) NOT NULL,
    prenom VARCHAR(255) NOT NULL,
    age INT NOT NULL,
    email VARCHAR(255) NOT NULL,
    PRIMARY KEY (id)
);

SHOW TABLES;

SHOW COLUMNS FROM etudiant;

