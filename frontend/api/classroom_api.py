import requests
from flask import session
from . import CLASSROOM_API_URL

class ClassroomClient:
    @staticmethod
    def create_classroom(form):
        api_key = None
        payload = {
            'teacher_id': session['user'].get("id"),
            'meeting_information':  form.get('meeting_information'),
            'duration': form.get('meeting_duration'),
            'date_of_booking': form.get('Meetingtime'),
            'invitees_id': form.get('studentids')
        }
        print(payload)
        url = CLASSROOM_API_URL + '/api/classroom/create'

        response = requests.post(url, data=payload)

        return response.json()