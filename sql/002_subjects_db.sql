SET NAMES utf8;

DROP TABLE IF EXISTS `Subject`;

CREATE TABLE
    `Subject` (
        `ID` int(11) NOT NULL AUTO_INCREMENT,
        `Name` text NOT NULL,
        `Teacher` text NOT NULL,
        `Classroom` text NOT NULL,
        `Day` text NOT NULL,
        `StartTime` time NOT NULL,
        `EndTime` time NOT NULL,
        `StartDate` date NOT NULL,
        `EndDate` date NOT NULL,
        `Group` text NOT NULL,
        `Status` tinyint(4) NOT NULL,
        `CreationDate` datetime NOT NULL,
        `LastUpdate` timestamp NOT NULL,
        `Option` int(11) NOT NULL,
        PRIMARY KEY (`ID`)
    ) ENGINE = InnoDB DEFAULT CHARSET = utf8;