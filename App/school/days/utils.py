from school import db
from school.models import Days
from school.tools.utils import color
import logging
import traceback


def getDays() -> list[Days]:
    '''Returns the days of the week stored in the database'''
    days = Days.query.all()
    if days:
        return days
    else:
        logging.warning(f'{color(3,"No days found in database")}')
        return []


def abreviatonToDay(abv: str) -> str:
    """Given an abreviation, it returns the day in DB"""
    days = {
        'Lun': 'Lunes',
        'Mart': 'Martes',
        'Miérc': 'Miércoles',
        'Jue': 'Jueves',
        'V': 'Viernes',
        'S': 'Sábado',
        'D': 'Domingo'
    }
    return days[abv]
