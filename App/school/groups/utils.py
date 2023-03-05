from school import db
from school.models import Group, Schedule
from school.relations import RelationGroupSchedule
from school.schedule.utils import getSchedule
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


def getGroup(groupID: int, type: int) -> Group:
    '''Returns a list with the group data by passing an ID
       type: 1 = list
             2 = dict
    '''
    try:

        group = Group.query.filter_by(id=groupID).first()
        if group:

            group.schedules = db.session.query(Schedule)\
                .join(RelationGroupSchedule)\
                .filter(RelationGroupSchedule.c.groupId == groupID)\
                .all()
            match type:
                case 1:
                    groupData = group
                case 2:
                    groupData = group.toDict()
                    groupData['Schedules'] = list(map(
                        lambda schedule: getSchedule(schedule), group.schedules))
                case _:
                    raise Exception(f'{color(3,"Type not found")}')

            logging.info(f"{color(2,'Group found:')} ✅")

        else:
            raise Exception(f'{color(3,"Group not found")}')

    except Exception as e:
        logging.error(
            f'{color(1,"Couldnt get group")} ❌: {e} {traceback.format_exc().splitlines()[-3]}')
        groupData = None

    return groupData


# def filterGroups(filterGroup: str) -> list[dict]:
#     '''Returns a list with the group data by passing an ID'''
#     try:

#     except Exception as e:
#         logging.error(
#             f'{color(1,"Couldnt get groups")} ❌: {e} {traceback.format_exc().splitlines()[-3]}')
#         groupsData = None

#     return groupsData
