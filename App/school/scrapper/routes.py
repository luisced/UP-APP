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
            else:
                error, code = 'Missing fields', 4
        else:
            error, code = 'No data received', 5
    else:
        error, code = 'Invalid method', 6

    response.update({'sucess': True, 'message': message, 'message': f'{data}', 'status_code': 200, 'error': None, 'code': f'{code}'} if data and data != [{}]else {
        'sucess': False,  'message': 'Could not get content', 'status_code': 400, 'error': f'{error}', 'code': f'{code}'})
    return jsonify(response, response['status_code'])
