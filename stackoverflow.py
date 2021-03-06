import requests
from datetime import datetime


class StackOverflow:
    """
    Class for fetching StackOverflow queries
    """
    def _get_param(self):
        """
        Constructs parameters for a request

        :return: dict with parameters
        """
        current_date = int(datetime.utcnow().timestamp())
        date_two_days = current_date - (86400 * 2)
        param = {
            'fromdate': date_two_days,
            'todate': current_date,
            'order': 'desc',
            'sort': 'creation',
            'tagged': 'python',
            'site': 'stackoverflow'
        }
        return param

    def _get_response(self):
        """
        Requests StackOverflow API for all questions regarding Python in two-day time span

        :return: dict with questions
        """
        url = 'https://api.stackexchange.com/2.3/questions'
        headers = {'Content-Type': 'application/json'}
        params = self._get_param()
        response = requests.get(url=url, headers=headers, params=params)
        return response.json()

    def get_questions(self):
        """
        Makes a request to API and returns titles and links

        :return: dict with titles and links
        """
        response_dump = self._get_response()
        questions_dict = dict()
        for query in response_dump['items']:
            questions_dict[query['title']] = query['link']
        return questions_dict

