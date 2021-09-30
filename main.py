import requests
from heroes import Heroes, max_stats
from pprint import pprint
from yandex import Yandex
from stackoverflow import StackOverflow


if __name__ == '__main__':
    Hulk = Heroes('Hulk')
    Cap_America = Heroes('Captain_America')
    Thanos = Heroes('Thanos')
    max_stats([Hulk.get_stats(), Cap_America.get_stats(), Thanos.get_stats()])
    # token_yandex = ''
    # yan = Yandex(token_yandex)
    # remote_path = '/API_test/my_file.txt'
    # local_filename = 'my_file.txt'
    # yan.upload_to_disk(remote_path, local_filename)
    stack = StackOverflow()
    pprint(stack.get_response())







