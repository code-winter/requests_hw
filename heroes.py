import requests


class Heroes:
    """
    Describes methods for superheroes API, takes name for superhero to initialize

    """
    def __init__(self, name):
        self.name = name
        self.token = '2619421814940190'
        self.main_url = 'https://superheroapi.com/api/'

    def _get_hero_id(self):
        """
        Searches database for heroes' ID

        :return: hero ID
        """
        url = self.main_url + self.token + 'search/' + self.name.lower()
        res_dict = dict()
        res_dict = requests.get(url).json()
        hero_id = res_dict['results'][0]['id']
        return hero_id

    def _get_urls(self):
        url = self.main_url + self.token + self._get_hero_id() + '/powerstats/'
        return url

    def get_stats(self):
        """
        Makes a request to a database with specified URI, then writes intelligence stat with the hero name

        :return: tuple in format (name,intelligence)
        """
        url = self._get_urls()
        response = requests.get(url=url, timeout=10)
        temp_dict = response.json()
        int_stat = temp_dict['intelligence']
        return (self.name, int_stat)


def max_stats(hero_list):
    """
    Sorts heroes according their intelligence

    :param hero_list: list with tuples, containing hero names and their intelligence
    :return: nothing
    """
    hero_list.sort(key=lambda stat: stat[-1])
    print(f'Самый умный персонаж: {hero_list[0][0]} (интеллект равен {hero_list[0][1]})')
