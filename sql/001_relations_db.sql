SET NAMES utf8;

SET time_zone = '+00:00';

SET foreign_key_checks = 0;

SET sql_mode = 'NO_AUTO_VALUE_ON_ZERO';

DROP TABLE IF EXISTS `RelationStudentSubjectTable`;

CREATE TABLE
    `RelationStudentSubjectTable` (
        `ID` int(11) NOT NULL AUTO_INCREMENT,
        `StudentID` int(11) NOT NULL,
        `SubjectID` int(11) NOT NULL,
        PRIMARY KEY (`ID`),
        KEY `StudentID` (`StudentID`),
        KEY `SubjectID` (`SubjectID`),
        CONSTRAINT `RelationStudentSubjectTable_ibfk_1` FOREIGN KEY (`StudentID`) REFERENCES `Student` (`ID`),
        CONSTRAINT `RelationStudentSubjectTable_ibfk_2` FOREIGN KEY (`SubjectID`) REFERENCES `Subject` (`ID`)
    ) ENGINE = InnoDB DEFAULT CHARSET = latin1;