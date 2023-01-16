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

DROP TABLE IF EXISTS `RelationSubjectClassroomTable`;

CREATE TABLE
    `RelationSubjectClassroomTable` (
        `ID` int(11) NOT NULL AUTO_INCREMENT,
        `SubjectID` int(11) NOT NULL,
        `ClassroomID` int(11) NOT NULL,
        PRIMARY KEY (`ID`),
        KEY `SubjectID` (`SubjectID`),
        KEY `ClassroomID` (`ClassroomID`),
        CONSTRAINT `RelationSubjectClassroomTable_ibfk_1` FOREIGN KEY (`SubjectID`) REFERENCES `Subject` (`ID`),
        CONSTRAINT `RelationSubjectClassroomTable_ibfk_2` FOREIGN KEY (`ClassroomID`) REFERENCES `Classroom` (`ID`)
    ) ENGINE = InnoDB DEFAULT CHARSET = latin1;