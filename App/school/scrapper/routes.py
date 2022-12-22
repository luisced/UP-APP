from flask import Blueprint, request, jsonify, render_template
from school.scrapper.utils import *


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
                data.append(extractUP4USchedule())
                print(data)
                message, code = 'Data extracted', 1
            else:
                error, code = 'Missing fields', 2
        else:
            error, code = 'No data received', 3
    else:
        error, code = 'Invalid method', 4

    response.update({'sucess': True, 'message': message, 'data': data, 'status_code': 200, 'error': None, 'code': f'{code}'} if data and data != {{}} else {
        'sucess': False,  'message': 'Could not get content', 'status_code': 400, 'error': f'{error}', 'code': f'{code}'})
    return jsonify(response, response['status_code'])
