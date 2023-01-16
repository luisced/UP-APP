from school.models import *
from school import db

RelationStudentSubjectTable = db.Table('RelationStudentSubjectTable',
                                       db.Column('studentId', db.Integer,
                                                 db.ForeignKey('Student.id')),
                                       db.Column('subjectId', db.Integer, db.ForeignKey('Subject.id')),)

RelationClassroomSubjectTable = db.Table('RelationClassroomSubjectTable',
                                         db.Column(
                                             'subjectId', db.Integer, db.ForeignKey('Subject.id')),
                                         db.Column('classroomId', db.Integer, db.ForeignKey('Classroom.id')),)
