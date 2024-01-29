--
-- Author: Cyril GENISSON
-- Created: 29/01/2024
-- Updated: 29/01/2024
--
-- filename: job12.sql
-- Description: 
--

USE LaPlateforme;

INSERT INTO etudiant(nom,prenom,email,age)
VALUES
('Dupuis','Martin','martin.dupuis@laplateforme.io',18);

SELECT * FROM etudiant
WHERE nom IN (
SELECT nom FROM etudiant
GROUP BY nom
HAVING COUNT(nom) > 1);

