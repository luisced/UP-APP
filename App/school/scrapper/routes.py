from flask import Blueprint, request, jsonify, render_template


scrapper = Blueprint('scrapper', __name__)


@scrapper.route('/scrapp_up4u', methods=['GET', 'POST'])
def scrapp_up4u():
    pass
