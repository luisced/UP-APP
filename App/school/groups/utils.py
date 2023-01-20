from school import db
from school.models import Group
import datetime
import logging
import traceback
from school.tools.utils import color


def createGroup(classNumber: int, group: str, subject: int, teacher: int, language: int, students: str, modality: str, description: str, startDate: datetime, endDate: datetime) -> Group:
    '''Creates a group in the database'''
    try:
        if not Group.query.filter_by(classNumber=classNumber, group=group, subject=subject, teacher=teacher).first():
            group = Group(
                classNumber=classNumber,
                group=group,
                subject=subject,
                teacher=teacher,
                language=language,
                students=students,
                modality=modality,
                description=description,
                startDate=startDate,
                endDate=endDate
            )
            db.session.add(group)
            db.session.commit()
            logging.info(f"{color(2,'Group created:')} ✅")
        else:
            raise Exception('Group already exists')
    except Exception as e:
        logging.error(
            f'{color(1,"Couldnt create group")} ❌: {e} {traceback.format_exc().splitlines()[-3]}')
        group = None

    return group
