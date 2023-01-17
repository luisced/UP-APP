DROP TABLE IF EXISTS `Days`;

CREATE TABLE
    `Days` (
        `ID` int(11) NOT NULL AUTO_INCREMENT,
        `Day` text NOT NULL,
        PRIMARY KEY (`ID`)
    ) ENGINE = InnoDB DEFAULT CHARSET = latin1;

INSERT INTO
    `Days` (`ID`, `Day`)
VALUES (1, 'Lunes'), (2, 'Martes'), (7, 'Miércoles'), (8, 'Jueves'), (9, 'Viernes'), (10, 'Sábado'), (11, 'Domingo');