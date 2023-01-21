from school import db
from school.models import Group
import datetime
import logging
import traceback
from school.tools.utils import color


def createGroup(classNumber: int, group: str, subject: int, teacher: int, language: int, students: str, modality: str, description: str) -> Group:
    '''Creates a group in the database'''
    try:
        if not Group.query.filter_by(classNumber=classNumber).first():
            options = False if students.split(
                '/')[0] == students.split('/')[1] else True

            group = Group(
                classNumber=classNumber,
                group=group,
                subject=subject,
                teacher=teacher,
                language=language,
                students=students,
                modality=modality,
                description=description,
                options=options
            )
            db.session.add(group)
            db.session.commit()
            logging.info(f"{color(2,'Group created:')} ✅")
        else:
            raise Exception(f'{color(3,"Group already exists in database")}')

    except Exception as e:
        logging.error(
            f'{color(1,"Couldnt create group")} ❌: {e} {traceback.format_exc().splitlines()[-3]}')
        group = None

    return group


# win0divUP_DERIVED_IDM_UP_CLASS_LANG\$0 > div > img
# win0divUP_DERIVED_IDM_UP_CLASS_LANG\$0
