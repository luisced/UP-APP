from school.models import Classroom
from school import db


def createClassroom(name: str) -> Classroom:
    '''Creates a classroom object'''

    # Check if classroom already exists in database
    if not Classroom.query.filter_by(name=name).first():
        # Create classroom object if it doesn't exist in database
        classroom = Classroom(name=name)
        # Add classroom to database
        db.session.add(classroom)
        db.session.commit()
    else:
        # Raise an error if classroom already exists in database
        raise ValueError(f'Classroom already exists in database')

    return classroom
