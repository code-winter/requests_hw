import requests


class Heroes:
    def __init__(self, name):
        self.name = name
        self.token = '2619421814940190'
        self.main_url = 'https://superheroapi.com/api/2619421814940190/'

    def _get_hero_id(self):
        url = self.main_url + 'search/' + self.name.lower()
        res_dict = dict()
        res_dict = requests.get(url).json()
        hero_id = res_dict['results'][0]['id']
        return hero_id

    def _get_urls(self):
        url = self.main_url + self._get_hero_id() + '/powerstats/'
        return url

    def get_stats(self):
        url = self._get_urls()
        response = requests.get(url=url, timeout=10)
        temp_dict = response.json()
        int_stat = temp_dict['intelligence']
        return (self.name, int_stat)


def max_stats(hero_list):
    hero_list.sort(key=lambda stat: stat[-1])
    print(f'Самый умный персонаж: {hero_list[0][0]} (интеллект равен {hero_list[0][1]})')
