--
-- Author: Cyril GENISSON
-- Created: 29/01/2024
-- Updated: 29/01/2024
--
-- filename: job05.sql
-- Description: 
--

USE LaPlateforme;

INSERT INTO etudiant(nom,prenom,email,age)
VALUES
('Spaghetty','Betty','betty.Spaghetti@laplateforme.io',23);
('Steack','Chuck','chuck.steack@laplateforme.io',45),
('Doe','John','john.doe@laplateforme.io',18),
('Barnes','Binkie','binkie.barnes@laplateforme.io',16),
('Dupuis','Gertrude','gertrude.dupuis@laplateforme.io',20);

SELECT * FROM etudiant;
