--
-- Author: Cyril GENISSON
-- Created: 29/01/2024
-- Updated: 29/01/2024
--
-- filename: job22.sql
-- Description: 
--

USE LaPlateforme;

SELECT nom, prenom, email, MIN(age) FROM etudiant;

