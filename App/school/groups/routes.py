from school.models import Group
from flask import Blueprint, request, jsonify, render_template, session
from school.groups.utils import *
import json


groups = Blueprint('groups', __name__)


@groups.route('/getGroup', methods=['GET', 'POST'])
def getGroupDB() -> dict[str, str]:
    '''This endpoint returns a group from the database'''
    if request.method == 'GET':
        data: list[dict[str, str]] = []
        response: dict[str, str] = {}
        error, code = None, None
        data = [getGroup(group.id, 2) for group in Group.query.all()]
        message, code = f'Group found', 1
    else:
        error, code = 'Invalid method', 4

    response.update({'sucess': True, 'message': message, 'Group': data, 'status_code': 200, 'error': error, 'code': code} if data and data != [] and data != [None] else {
        'sucess': False,  'message': 'Could not get content', 'status_code': 400, 'error': f'{error}', 'code': code})
    return jsonify(response)
