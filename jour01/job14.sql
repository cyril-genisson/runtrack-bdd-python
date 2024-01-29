--
-- Author: Cyril GENISSON
-- Created: 29/01/2024
-- Updated: 29/01/2024
--
-- filename: job14.sql
-- Description: 
--

USE LaPlateforme;

SELECT * FROM etudiant 
WHERE age < 26  AND age > 17
ORDER BY age; 
