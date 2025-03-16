from flask import Blueprint, request, jsonify
from backend import db

timetable_routes = Blueprint('timetable_routes', __name__)

@timetable_routes.route('/generate', methods=['POST'])
def generate_timetable():
    data = request.json
    subjects = data.get('subjects')
    hours = data.get('hours')

    # Simple logic for timetable generation
    timetable = {}
    remaining_hours = hours
    for subject in subjects:
        hours_per_subject = remaining_hours // len(subjects)
        timetable[subject] = hours_per_subject
        remaining_hours -= hours_per_subject

    return jsonify({'timetable': timetable}), 200