import requests
from heroes import Heroes, max_stats
from pprint import pprint


if __name__ == '__main__':
    Hulk = Heroes('Hulk')
    Cap_America = Heroes('Captain_America')
    Thanos = Heroes('Thanos')
    max_stats([Hulk.get_stats(), Cap_America.get_stats(), Thanos.get_stats()])




