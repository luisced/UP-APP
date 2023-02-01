DROP TABLE IF EXISTS `Schedule`;

CREATE TABLE
    `Schedule` (
        `ID` int(11) NOT NULL AUTO_INCREMENT,
        `GroupID` int(11) NOT NULL,
        `DaysID` int(11) NOT NULL,
        `HoursID` int(11) NOT NULL,
        `Status` tinyint(4) NOT NULL,
        `CreationDate` datetime NOT NULL,
        `LastUpdate` timestamp NOT NULL,
        PRIMARY KEY (`ID`),
        KEY `GroupID` (`GroupID`),
        KEY `DaysID` (`DaysID`),
        KEY `HoursID` (`HoursID`),
        CONSTRAINT `Schedule_ibfk_1` FOREIGN KEY (`GroupID`) REFERENCES `Group` (`ID`),
        CONSTRAINT `Schedule_ibfk_2` FOREIGN KEY (`DaysID`) REFERENCES `Days` (`ID`),
        CONSTRAINT `Schedule_ibfk_3` FOREIGN KEY (`HoursID`) REFERENCES `Hours` (`id`)
    ) ENGINE = InnoDB DEFAULT CHARSET = latin1