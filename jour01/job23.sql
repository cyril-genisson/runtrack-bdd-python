--
-- Author: Cyril GENISSON
-- Created: 29/01/2024
-- Updated: 29/01/2024
--
-- filename: job23.sql
-- Description: 
--

USE LaPlateforme;

SELECT nom, prenom, email, MAX(age) FROM etudiant;

