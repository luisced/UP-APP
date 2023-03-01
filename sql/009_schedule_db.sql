SET NAMES utf8;

SET time_zone = '+00:00';

SET foreign_key_checks = 0;

SET sql_mode = 'NO_AUTO_VALUE_ON_ZERO';

SET NAMES utf8;

SET time_zone = '+00:00';

SET foreign_key_checks = 0;

SET sql_mode = 'NO_AUTO_VALUE_ON_ZERO';

DROP TABLE IF EXISTS `Schedule`;

CREATE TABLE
    `Schedule` (
        `ID` int(11) NOT NULL AUTO_INCREMENT,
        `ClassroomID` int(11) NOT NULL,
        `DayID` int(11) NOT NULL,
        `StartTime` int(11) NOT NULL,
        `EndTime` int(11) NOT NULL,
        `Status` tinyint(4) NOT NULL,
        `CreationDate` date NOT NULL,
        `LastUpdate` timestamp NOT NULL,
        PRIMARY KEY (`ID`),
        KEY `ClassroomID` (`ClassroomID`),
        KEY `DayID` (`DayID`),
        KEY `StartTime` (`StartTime`),
        KEY `EndTime` (`EndTime`),
        CONSTRAINT `Schedule_ibfk_2` FOREIGN KEY (`ClassroomID`) REFERENCES `Classroom` (`ID`),
        CONSTRAINT `Schedule_ibfk_3` FOREIGN KEY (`DayID`) REFERENCES `Days` (`ID`),
        CONSTRAINT `Schedule_ibfk_4` FOREIGN KEY (`StartTime`) REFERENCES `Hours` (`id`),
        CONSTRAINT `Schedule_ibfk_5` FOREIGN KEY (`EndTime`) REFERENCES `Hours` (`id`)
    ) ENGINE = InnoDB DEFAULT CHARSET = latin1;