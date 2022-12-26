from school.models import Student
from school.schedule.utils import getSubject, getStudentData
from flask import Blueprint, request, jsonify, render_template
from school.scrapper.utils import *
import time

scrapper = Blueprint('scrapper', __name__)


@scrapper.route('/scrapper_up4u', methods=['GET', 'POST'])
def scrapp_up4u() -> dict[str, str]:
    '''
    This endpoint returns the schedule of a student in a json format
    '''
    if request.method == 'GET':
        json_data = request.get_json()
        data: list[dict[str, str]] = []
        response: dict[str, str] = {}
        error, message, code = False, '', ''
        if json_data and all(json_data.values()):
            if ['id', 'password'] == list(json_data.keys()):
                student = Student.query.filter_by(
                    studentID=json_data['id']).first()
                if not student:
                    schedule = extractUP4USchedule(
                        json_data['id'], json_data['password'])
                    data = [subject for subject in schedule]
                else:
                    # startTime = time.perf_counter()
                    # data = [getSubject(subject)for subject in student.subjects]
                    data = [getStudentData(student)]
                    # endTime = time.perf_counter()
                    # print(f'Execution time: {endTime - startTime}')
                message, code = f'Data extracted', 1
            else:
                error, code = 'Missing fields', 2
        else:
            error, code = 'No data received', 3
    else:
        error, code = 'Invalid method', 4

    response.update({'sucess': True, 'message': message, 'Schedule': data, 'status_code': 200, 'error': None, 'code': code} if data and data != [] and data != [None] else {
        'sucess': False,  'message': 'Could not get content', 'status_code': 400, 'error': f'{error}', 'code': code})
    return jsonify(response, response['status_code'])
