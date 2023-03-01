SET NAMES utf8;

DROP TABLE IF EXISTS `Days`;

CREATE TABLE
    `Days` (
        `ID` int(11) NOT NULL AUTO_INCREMENT,
        `Day` text NOT NULL,
        PRIMARY KEY (`ID`)
    ) ENGINE = InnoDB DEFAULT CHARSET = latin1;

INSERT INTO
    `Days` (`ID`, `Day`)
VALUES (1, 'Lunes'), (2, 'Martes'), (3, 'Miércoles'), (4, 'Jueves'), (5, 'Viernes'), (6, 'Sábado'), (7, 'Domingo');