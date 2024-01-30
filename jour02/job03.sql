--
-- Author: Cyril GENISSON
-- Created: 30/01/2024
-- Updated: 30/01/2024
--
-- filename: job03.sql
-- Description: 
--


USE LaPlateforme;

INSERT INTO etage(nom,numero,superficie)
VALUES
('RDC', 0, 500),
('R+1', 1, 500);

SELECT * FROM etage;

INSERT INTO salle(nom,id_etage,capacite)
VALUES
('Lounge', 1, 100),
('Studio son', 1, 5),
('Broadcasting', 2, 50),
('Bocal pPeda', 2, 4),
('Coworking',2, 80),
('Studio Vidéo', 2, 5);

SELECT * FROM salle;
