from school.models import Student
from flask_bcrypt import generate_password_hash
from school.tools.utils import color
import logging
import traceback


def createStudent(studentId: str, password: str, name: str, lastName: str) -> Student:
    '''Creates a student object'''
    try:
        if not Student.query.filter_by(studentId=studentId).first():
            student = Student(
                studentId=studentId,
                password=generate_password_hash(password).decode('utf-8'),
                name=name,
                lastName=lastName,
                email=studentId+"@up.edu.mx"
            )
            logging.info(f'{color(2,"Student created")} ✅')
        else:
            raise ValueError(
                f'{color(3,"Student already exists in database")}')
    except Exception as e:
        logging.error(
            f'{color(1,"Student not created")} ❌: {e}\n{traceback.format_exc().splitlines()[-3]}')
        student = None

    return student
