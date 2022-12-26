from school.models import Student
from school import db
from school.tools.utils import color
import logging
import traceback


def createStudent(studentID: str, password: str, name: str) -> Student:
    '''Creates a student object'''
    try:
        if not Student.query.filter_by(studentID=studentID).first():
            student = Student(
                studentID=studentID,
                password=password,
                name=name.split(' ')[0],
                lastName=' '.join(name.split(' ')[1:]),
                email=studentID+"@up.edu.mx"
            )
            db.session.add(student)
            db.session.commit()
            logging.info(f'{color(2,"Student created")} ✅')
        else:
            raise ValueError(
                f'{color(3,"Student already exists in database")}')
    except Exception as e:
        logging.error(
            f'{color(1,"Student not created")} ❌: {e}\n{traceback.format_exc().splitlines()[-3]}')
        student = None

    return student
