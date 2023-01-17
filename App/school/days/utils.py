def abreviatonToDay(abv: str) -> str:
    """Given an abreviation, it returns the day in DB"""
    days = {
        'Lun': 'Lunes',
        'Mart': 'Martes',
        'Mierc': 'Miércoles',
        'Jue': 'Jueves',
        'V': 'Viernes',
        'S': 'Sábado',
        'D': 'Domingo'
    }
    return days[abv]
