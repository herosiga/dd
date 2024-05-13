import requests
import os
import subprocess
import random
import re
import threading
import urllib.request
import argparse
import sys
from colorama import Fore, Back, Style, init
from time import time

init(autoreset=True)

output_file = 'proxy.txt'
os.system('cls' if os.name == 'nt' else 'clear')

if os.path.isfile(output_file):
    os.remove(output_file)
    print(f"{Fore.RED}'proxy.txt' telah dihapus.{Fore.RESET}")

print(f"{Fore.YELLOW}Otw Download\n")

proxy_urls = [
'https://proxylist.geonode.com/api/proxy-list?anonymityLevel=elite&protocols=http%2Chttps%2Csocks4%2Csocks5&speed=fast&limit=500&page=1&sort_by=lastChecked&sort_type=desc',
'https://proxylist.geonode.com/api/proxy-list?anonymityLevel=elite&protocols=http%2Chttps%2Csocks4%2Csocks5&speed=fast&limit=500&page=2&sort_by=lastChecked&sort_type=desc',
'https://proxylist.geonode.com/api/proxy-list?anonymityLevel=elite&protocols=http%2Chttps%2Csocks4%2Csocks5&speed=fast&limit=500&page=3&sort_by=lastChecked&sort_type=desc',
'https://proxylist.geonode.com/api/proxy-list?anonymityLevel=elite&protocols=http%2Chttps%2Csocks4%2Csocks5&speed=fast&limit=500&page=4&sort_by=lastChecked&sort_type=desc',
'https://proxylist.geonode.com/api/proxy-list?anonymityLevel=elite&protocols=http%2Chttps%2Csocks4%2Csocks5&speed=fast&limit=500&page=5&sort_by=lastChecked&sort_type=desc',
'https://proxylist.geonode.com/api/proxy-list?anonymityLevel=elite&protocols=http%2Chttps%2Csocks4%2Csocks5&speed=fast&limit=500&page=6&sort_by=lastChecked&sort_type=desc',
'https://proxylist.geonode.com/api/proxy-list?anonymityLevel=elite&protocols=http%2Chttps%2Csocks4%2Csocks5&speed=fast&limit=500&page=7&sort_by=lastChecked&sort_type=desc',
'https://proxylist.geonode.com/api/proxy-list?anonymityLevel=elite&protocols=http%2Chttps%2Csocks4%2Csocks5&speed=fast&limit=500&page=8&sort_by=lastChecked&sort_type=desc',
'https://proxylist.geonode.com/api/proxy-list?anonymityLevel=elite&protocols=http%2Chttps%2Csocks4%2Csocks5&speed=fast&limit=500&page=9&sort_by=lastChecked&sort_type=desc',
'https://proxylist.geonode.com/api/proxy-list?anonymityLevel=elite&protocols=http%2Chttps%2Csocks4%2Csocks5&speed=fast&limit=500&page=10&sort_by=lastChecked&sort_type=desc',
'https://proxylist.geonode.com/api/proxy-list?anonymityLevel=elite&protocols=http%2Chttps%2Csocks4%2Csocks5&speed=fast&limit=500&page=11&sort_by=lastChecked&sort_type=desc',
'https://proxylist.geonode.com/api/proxy-list?anonymityLevel=elite&protocols=http%2Chttps%2Csocks4%2Csocks5&speed=fast&limit=500&page=12&sort_by=lastChecked&sort_type=desc',
'https://proxylist.geonode.com/api/proxy-list?anonymityLevel=elite&protocols=http%2Chttps%2Csocks4%2Csocks5&speed=fast&limit=500&page=13&sort_by=lastChecked&sort_type=desc',
'https://proxylist.geonode.com/api/proxy-list?anonymityLevel=elite&protocols=http%2Chttps%2Csocks4%2Csocks5&speed=fast&limit=500&page=14&sort_by=lastChecked&sort_type=desc',
'https://proxylist.geonode.com/api/proxy-list?anonymityLevel=elite&protocols=http%2Chttps%2Csocks4%2Csocks5&speed=fast&limit=500&page=15&sort_by=lastChecked&sort_type=desc',
'https://proxylist.geonode.com/api/proxy-list?anonymityLevel=elite&protocols=http%2Chttps%2Csocks4%2Csocks5&speed=fast&limit=500&page=16&sort_by=lastChecked&sort_type=desc',
'https://proxylist.geonode.com/api/proxy-list?anonymityLevel=elite&protocols=http%2Chttps%2Csocks4%2Csocks5&speed=fast&limit=500&page=17&sort_by=lastChecked&sort_type=desc',
'https://proxylist.geonode.com/api/proxy-list?anonymityLevel=elite&protocols=http%2Chttps%2Csocks4%2Csocks5&speed=fast&limit=500&page=18&sort_by=lastChecked&sort_type=desc',
'https://proxylist.geonode.com/api/proxy-list?anonymityLevel=elite&protocols=http%2Chttps%2Csocks4%2Csocks5&speed=fast&limit=500&page=19&sort_by=lastChecked&sort_type=desc',
'https://proxylist.geonode.com/api/proxy-list?anonymityLevel=elite&protocols=http%2Chttps%2Csocks4%2Csocks5&speed=fast&limit=500&page=20&sort_by=lastChecked&sort_type=desc',
'https://proxylist.geonode.com/api/proxy-list?anonymityLevel=elite&protocols=http%2Chttps%2Csocks4%2Csocks5&speed=fast&limit=500&page=21&sort_by=lastChecked&sort_type=desc',
'https://proxylist.geonode.com/api/proxy-list?anonymityLevel=elite&protocols=http%2Chttps%2Csocks4%2Csocks5&speed=fast&limit=500&page=22&sort_by=lastChecked&sort_type=desc',
'https://proxylist.geonode.com/api/proxy-list?anonymityLevel=elite&protocols=http%2Chttps%2Csocks4%2Csocks5&speed=fast&limit=500&page=23&sort_by=lastChecked&sort_type=desc',
'https://proxylist.geonode.com/api/proxy-list?anonymityLevel=elite&protocols=http%2Chttps%2Csocks4%2Csocks5&speed=fast&limit=500&page=24&sort_by=lastChecked&sort_type=desc',
'https://proxylist.geonode.com/api/proxy-list?anonymityLevel=elite&protocols=http%2Chttps%2Csocks4%2Csocks5&speed=fast&limit=500&page=25&sort_by=lastChecked&sort_type=desc',
'https://proxylist.geonode.com/api/proxy-list?anonymityLevel=elite&protocols=http%2Chttps%2Csocks4%2Csocks5&speed=fast&limit=500&page=26&sort_by=lastChecked&sort_type=desc',
'https://proxylist.geonode.com/api/proxy-list?anonymityLevel=elite&protocols=http%2Chttps%2Csocks4%2Csocks5&speed=fast&limit=500&page=27&sort_by=lastChecked&sort_type=desc',
'https://proxylist.geonode.com/api/proxy-list?anonymityLevel=elite&protocols=http%2Chttps%2Csocks4%2Csocks5&speed=fast&limit=500&page=28&sort_by=lastChecked&sort_type=desc',
'https://proxylist.geonode.com/api/proxy-list?anonymityLevel=elite&protocols=http%2Chttps%2Csocks4%2Csocks5&speed=fast&limit=500&page=29&sort_by=lastChecked&sort_type=desc',
'https://proxylist.geonode.com/api/proxy-list?anonymityLevel=elite&protocols=http%2Chttps%2Csocks4%2Csocks5&speed=fast&limit=500&page=30&sort_by=lastChecked&sort_type=desc',
'https://proxylist.geonode.com/api/proxy-list?anonymityLevel=elite&protocols=http%2Chttps%2Csocks4%2Csocks5&speed=fast&limit=500&page=31&sort_by=lastChecked&sort_type=desc',
'https://proxylist.geonode.com/api/proxy-list?anonymityLevel=elite&protocols=http%2Chttps%2Csocks4%2Csocks5&speed=fast&limit=500&page=32&sort_by=lastChecked&sort_type=desc',
'https://proxylist.geonode.com/api/proxy-list?anonymityLevel=elite&protocols=http%2Chttps%2Csocks4%2Csocks5&speed=fast&limit=500&page=33&sort_by=lastChecked&sort_type=desc',
'https://proxylist.geonode.com/api/proxy-list?anonymityLevel=elite&protocols=http%2Chttps%2Csocks4%2Csocks5&speed=fast&limit=500&page=34&sort_by=lastChecked&sort_type=desc',
'https://proxylist.geonode.com/api/proxy-list?anonymityLevel=elite&protocols=http%2Chttps%2Csocks4%2Csocks5&speed=fast&limit=500&page=35&sort_by=lastChecked&sort_type=desc',
'https://proxylist.geonode.com/api/proxy-list?anonymityLevel=elite&protocols=http%2Chttps%2Csocks4%2Csocks5&speed=fast&limit=500&page=36&sort_by=lastChecked&sort_type=desc',
'https://proxylist.geonode.com/api/proxy-list?anonymityLevel=elite&protocols=http%2Chttps%2Csocks4%2Csocks5&speed=fast&limit=500&page=37&sort_by=lastChecked&sort_type=desc',
'https://proxylist.geonode.com/api/proxy-list?anonymityLevel=elite&protocols=http%2Chttps%2Csocks4%2Csocks5&speed=fast&limit=500&page=38&sort_by=lastChecked&sort_type=desc',
'https://proxylist.geonode.com/api/proxy-list?anonymityLevel=elite&protocols=http%2Chttps%2Csocks4%2Csocks5&speed=fast&limit=500&page=39&sort_by=lastChecked&sort_type=desc',
'https://proxylist.geonode.com/api/proxy-list?anonymityLevel=elite&protocols=http%2Chttps%2Csocks4%2Csocks5&speed=fast&limit=500&page=40&sort_by=lastChecked&sort_type=desc',
'https://proxylist.geonode.com/api/proxy-list?anonymityLevel=elite&protocols=http%2Chttps%2Csocks4%2Csocks5&speed=fast&limit=500&page=41&sort_by=lastChecked&sort_type=desc',
'https://proxylist.geonode.com/api/proxy-list?anonymityLevel=elite&protocols=http%2Chttps%2Csocks4%2Csocks5&speed=fast&limit=500&page=42&sort_by=lastChecked&sort_type=desc',
'https://proxylist.geonode.com/api/proxy-list?anonymityLevel=elite&protocols=http%2Chttps%2Csocks4%2Csocks5&speed=fast&limit=500&page=43&sort_by=lastChecked&sort_type=desc',
'https://proxylist.geonode.com/api/proxy-list?anonymityLevel=elite&protocols=http%2Chttps%2Csocks4%2Csocks5&speed=fast&limit=500&page=44&sort_by=lastChecked&sort_type=desc',
'https://proxylist.geonode.com/api/proxy-list?anonymityLevel=elite&protocols=http%2Chttps%2Csocks4%2Csocks5&speed=fast&limit=500&page=45&sort_by=lastChecked&sort_type=desc',
'https://proxylist.geonode.com/api/proxy-list?anonymityLevel=elite&protocols=http%2Chttps%2Csocks4%2Csocks5&speed=fast&limit=500&page=46&sort_by=lastChecked&sort_type=desc',
'https://hidemy.io/en/proxy-list/?start=64#list',
'https://hidemy.io/en/proxy-list/?start=128#list',
'https://spys.one/free-proxy-list/ID/',
'https://proxyhub.me/sn/id-free-proxy-list.html',
'https://www.freeproxy.world/?type=&anonymity=4&country=&speed=&port=&page=1',
'https://www.freeproxy.world/?type=&anonymity=4&country=&speed=&port=&page=2',
'https://www.freeproxy.world/?type=&anonymity=4&country=&speed=&port=&page=3',
'https://www.freeproxy.world/?type=&anonymity=4&country=&speed=&port=&page=4',
'https://www.freeproxy.world/?type=&anonymity=4&country=&speed=&port=&page=5',
'https://www.freeproxy.world/?type=&anonymity=4&country=&speed=&port=&page=6',
'https://www.freeproxy.world/?type=&anonymity=4&country=&speed=&port=&page=7',
'https://www.freeproxy.world/?type=&anonymity=4&country=&speed=&port=&page=8',
'https://www.freeproxy.world/?type=&anonymity=4&country=&speed=&port=&page=9',
'https://www.freeproxy.world/?type=&anonymity=4&country=&speed=&port=&page=10',
'https://www.freeproxy.world/?type=&anonymity=4&country=&speed=&port=&page=11',
'https://www.freeproxy.world/?type=&anonymity=4&country=&speed=&port=&page=12',
'https://www.freeproxy.world/?type=&anonymity=4&country=&speed=&port=&page=13',
'https://www.freeproxy.world/?type=&anonymity=4&country=&speed=&port=&page=14',
'https://www.freeproxy.world/?type=&anonymity=4&country=&speed=&port=&page=15',
'https://www.freeproxy.world/?type=&anonymity=4&country=&speed=&port=&page=16',
'https://www.freeproxy.world/?type=&anonymity=4&country=&speed=&port=&page=17',
'https://www.freeproxy.world/?type=&anonymity=4&country=&speed=&port=&page=18',
'https://www.freeproxy.world/?type=&anonymity=4&country=&speed=&port=&page=19',
'https://www.freeproxy.world/?type=&anonymity=4&country=&speed=&port=&page=20',
'https://www.freeproxy.world/?type=&anonymity=4&country=&speed=&port=&page=21',
'https://www.freeproxy.world/?type=&anonymity=4&country=&speed=&port=&page=22',
'https://www.freeproxy.world/?type=&anonymity=4&country=&speed=&port=&page=23',
'https://www.freeproxy.world/?type=&anonymity=4&country=&speed=&port=&page=24',
'https://www.freeproxy.world/?type=&anonymity=4&country=&speed=&port=&page=25',
'https://www.freeproxy.world/?type=&anonymity=4&country=&speed=&port=&page=26',
'https://www.freeproxy.world/?type=&anonymity=4&country=&speed=&port=&page=27',
'https://www.freeproxy.world/?type=&anonymity=4&country=&speed=&port=&page=28',
'https://www.freeproxy.world/?type=&anonymity=4&country=&speed=&port=&page=29',
'https://www.freeproxy.world/?type=&anonymity=4&country=&speed=&port=&page=30',
'https://www.freeproxy.world/?type=&anonymity=4&country=&speed=&port=&page=31',
'https://proxy-tools.com/proxy/id',
'https://proxy-tools.com/proxy/id?page=2',
'https://proxy-tools.com/proxy/id?page=3',
'https://www.ditatompel.com/proxy/anonymity/elite',
'https://www.ditatompel.com/proxy/country/id',
'https://www.ditatompel.com/proxy/anonymity/anon',
'https://www.ditatompel.com/proxy/anonymity/trans',
'http://free-proxy.cz/en/proxylist/country/ID/all/ping/all',
'http://free-proxy.cz/en/proxylist/country/ID/all/ping/all/2',
'http://free-proxy.cz/en/proxylist/country/ID/all/ping/all/3',
'http://free-proxy.cz/en/proxylist/country/ID/all/ping/all/4',
'http://free-proxy.cz/en/proxylist/country/ID/all/ping/all/5',
'http://free-proxy.cz/en/proxylist/country/US/all/ping/all',
'http://free-proxy.cz/en/proxylist/country/US/all/ping/all/2',
'http://free-proxy.cz/en/proxylist/country/US/all/ping/all/3',
'http://free-proxy.cz/en/proxylist/country/US/all/ping/all/4',
'http://free-proxy.cz/en/proxylist/country/US/all/ping/all/5',
'https://www.proxynova.com/proxy-server-list/elite-proxies/',
'https://www.proxynova.com/proxy-server-list/country-id/',
'https://www.proxynova.com/proxy-server-list/country-cn/',
'https://www.proxynova.com/proxy-server-list/country-us/',
'https://api.lumiproxy.com/web_v1/free-proxy/list?page_size=60&page=1&country_code=id&language=en-us',
'https://api.lumiproxy.com/web_v1/free-proxy/list?page_size=60&page=1&anonymity=2&language=en-us',
'https://api.lumiproxy.com/web_v1/free-proxy/list?page_size=60&page=2&anonymity=2&language=en-us',
'https://api.lumiproxy.com/web_v1/free-proxy/list?page_size=60&page=3&anonymity=2&language=en-us',
'https://api.lumiproxy.com/web_v1/free-proxy/list?page_size=60&page=4&anonymity=2&language=en-us',
'https://api.lumiproxy.com/web_v1/free-proxy/list?page_size=60&page=5&anonymity=2&language=en-us',
'https://api.lumiproxy.com/web_v1/free-proxy/list?page_size=60&page=6&anonymity=2&language=en-us',
'https://api.lumiproxy.com/web_v1/free-proxy/list?page_size=60&page=7&anonymity=2&language=en-us',
'https://api.lumiproxy.com/web_v1/free-proxy/list?page_size=60&page=8&anonymity=2&language=en-us',
'https://api.lumiproxy.com/web_v1/free-proxy/list?page_size=60&page=9&anonymity=2&language=en-us',
'https://api.lumiproxy.com/web_v1/free-proxy/list?page_size=60&page=10&anonymity=2&language=en-us',
'https://api.lumiproxy.com/web_v1/free-proxy/list?page_size=60&page=11&anonymity=2&language=en-us',
'https://api.lumiproxy.com/web_v1/free-proxy/list?page_size=60&page=12&anonymity=2&language=en-us',
'https://api.lumiproxy.com/web_v1/free-proxy/list?page_size=60&page=13&anonymity=2&language=en-us',
'https://api.lumiproxy.com/web_v1/free-proxy/list?page_size=60&page=14&anonymity=2&language=en-us',
'https://api.lumiproxy.com/web_v1/free-proxy/list?page_size=60&page=15&anonymity=2&language=en-us',
'https://api.lumiproxy.com/web_v1/free-proxy/list?page_size=60&page=16&anonymity=2&language=en-us',
'https://api.lumiproxy.com/web_v1/free-proxy/list?page_size=60&page=17&anonymity=2&language=en-us',
'https://api.lumiproxy.com/web_v1/free-proxy/list?page_size=60&page=18&anonymity=2&language=en-us',
'https://api.lumiproxy.com/web_v1/free-proxy/list?page_size=60&page=19&anonymity=2&language=en-us',
'https://api.lumiproxy.com/web_v1/free-proxy/list?page_size=60&page=20&anonymity=2&language=en-us',
'https://api.lumiproxy.com/web_v1/free-proxy/list?page_size=60&page=21&anonymity=2&language=en-us',
'https://api.lumiproxy.com/web_v1/free-proxy/list?page_size=60&page=22&anonymity=2&language=en-us',
'https://api.lumiproxy.com/web_v1/free-proxy/list?page_size=60&page=23&anonymity=2&language=en-us',
'https://api.lumiproxy.com/web_v1/free-proxy/list?page_size=60&page=24&anonymity=2&language=en-us',
'https://api.lumiproxy.com/web_v1/free-proxy/list?page_size=60&page=25&anonymity=2&language=en-us',
'https://api.lumiproxy.com/web_v1/free-proxy/list?page_size=60&page=26&anonymity=2&language=en-us',
'https://api.lumiproxy.com/web_v1/free-proxy/list?page_size=60&page=27&anonymity=2&language=en-us',
'https://api.lumiproxy.com/web_v1/free-proxy/list?page_size=60&page=28&anonymity=2&language=en-us',
'https://api.lumiproxy.com/web_v1/free-proxy/list?page_size=60&page=29&anonymity=2&language=en-us',
'https://api.lumiproxy.com/web_v1/free-proxy/list?page_size=60&page=30&anonymity=2&language=en-us',
'https://checkerproxy.net/archive/2024-03-27',
'https://checkerproxy.net/archive/2024-03-26',
'https://checkerproxy.net/archive/2024-03-25',
'https://checkerproxy.net/archive/2024-03-24',
'https://checkerproxy.net/archive/2024-03-23',
'https://checkerproxy.net/archive/2024-03-22',
'https://checkerproxy.net/archive/2024-03-21',
'https://checkerproxy.net/archive/2024-03-20',
'https://checkerproxy.net/archive/2024-03-19',
'https://checkerproxy.net/archive/2024-03-18',
'https://checkerproxy.net/archive/2024-03-17',
'https://checkerproxy.net/archive/2024-03-16',
'https://checkerproxy.net/archive/2024-03-15',
'https://checkerproxy.net/archive/2024-03-14',
'https://checkerproxy.net/archive/2024-03-13',
'https://checkerproxy.net/archive/2024-03-12',
'https://checkerproxy.net/archive/2024-03-11',
'https://checkerproxy.net/archive/2024-03-10',
'https://checkerproxy.net/archive/2024-03-9',
'https://checkerproxy.net/archive/2024-03-8',
'https://checkerproxy.net/archive/2024-03-7',
'https://checkerproxy.net/archive/2024-03-6',
'https://checkerproxy.net/archive/2024-03-5',
'https://checkerproxy.net/archive/2024-03-4',
'https://checkerproxy.net/archive/2024-03-3',
'https://checkerproxy.net/archive/2024-03-2',
'https://checkerproxy.net/archive/2024-03-1',
'https://checkerproxy.net/archive/2024-02-29',
'https://checkerproxy.net/archive/2024-02-28',
'https://checkerproxy.net/archive/2024-02-27',
'https://checkerproxy.net/archive/2024-02-26',
'https://checkerproxy.net/archive/2024-02-25',
'https://checkerproxy.net/archive/2024-02-24',
'https://checkerproxy.net/archive/2024-02-23',
'https://checkerproxy.net/archive/2024-02-22',
'https://checkerproxy.net/archive/2024-02-21',
'https://checkerproxy.net/archive/2024-02-20',
'https://checkerproxy.net/archive/2024-02-19',
'https://checkerproxy.net/archive/2024-02-18',
'https://checkerproxy.net/archive/2024-02-17',
'https://checkerproxy.net/archive/2024-02-16',
'https://checkerproxy.net/archive/2024-02-15',
'https://checkerproxy.net/archive/2024-02-14',
'https://checkerproxy.net/archive/2024-02-13',
'https://checkerproxy.net/archive/2024-02-12',
'https://checkerproxy.net/archive/2024-02-11',
'https://checkerproxy.net/archive/2024-02-10',
'https://checkerproxy.net/archive/2024-02-9',
'https://checkerproxy.net/archive/2024-02-8',
'https://checkerproxy.net/archive/2024-02-7',
'https://checkerproxy.net/archive/2024-02-6',
'https://checkerproxy.net/archive/2024-02-5',
'https://checkerproxy.net/archive/2024-02-4',
'https://checkerproxy.net/archive/2024-02-3',
'https://checkerproxy.net/archive/2024-02-2',
'https://checkerproxy.net/archive/2024-02-1',
'https://checkerproxy.net/archive/2024-01-29',
'https://checkerproxy.net/archive/2024-01-28',
'https://checkerproxy.net/archive/2024-01-27',
'https://checkerproxy.net/archive/2024-01-26',
'https://checkerproxy.net/archive/2024-01-25',
'https://checkerproxy.net/archive/2024-01-24',
'https://checkerproxy.net/archive/2024-01-23',
'https://checkerproxy.net/archive/2024-01-22',
'https://checkerproxy.net/archive/2024-01-21',
'https://checkerproxy.net/archive/2024-01-20',
'https://checkerproxy.net/archive/2024-01-19',
'https://checkerproxy.net/archive/2024-01-18',
'https://checkerproxy.net/archive/2024-01-17',
'https://checkerproxy.net/archive/2024-01-16',
'https://checkerproxy.net/archive/2024-01-15',
'https://checkerproxy.net/archive/2024-01-14',
'https://checkerproxy.net/archive/2024-01-13',
'https://checkerproxy.net/archive/2024-01-12',
'https://checkerproxy.net/archive/2024-01-11',
'https://checkerproxy.net/archive/2024-01-10',
'https://checkerproxy.net/archive/2024-01-9',
'https://checkerproxy.net/archive/2024-01-8',
'https://checkerproxy.net/archive/2024-01-7',
'https://checkerproxy.net/archive/2024-01-6',
'https://checkerproxy.net/archive/2024-01-5',
'https://checkerproxy.net/archive/2024-01-4',
'https://checkerproxy.net/archive/2024-01-3',
'https://checkerproxy.net/archive/2024-01-2',
'https://checkerproxy.net/archive/2024-01-1',
'https://checkerproxy.net/archive/2023-12-29',
'https://checkerproxy.net/archive/2023-12-28',
'https://checkerproxy.net/archive/2023-12-27',
'https://checkerproxy.net/archive/2023-12-26',
'https://checkerproxy.net/archive/2023-12-25',
'https://checkerproxy.net/archive/2023-12-24',
'https://checkerproxy.net/archive/2023-12-23',
'https://checkerproxy.net/archive/2023-12-22',
'https://checkerproxy.net/archive/2023-12-21',
'https://checkerproxy.net/archive/2023-12-20',
'https://checkerproxy.net/archive/2023-12-19',
'https://checkerproxy.net/archive/2023-12-18',
'https://checkerproxy.net/archive/2023-12-17',
'https://checkerproxy.net/archive/2023-12-16',
'https://checkerproxy.net/archive/2023-12-15',
'https://checkerproxy.net/archive/2023-12-14',
'https://checkerproxy.net/archive/2023-12-13',
'https://checkerproxy.net/archive/2023-12-12',
'https://checkerproxy.net/archive/2023-12-11',
'https://checkerproxy.net/archive/2023-12-10',
'https://checkerproxy.net/archive/2023-12-9',
'https://checkerproxy.net/archive/2023-12-8',
'https://checkerproxy.net/archive/2023-12-7',
'https://checkerproxy.net/archive/2023-12-6',
'https://checkerproxy.net/archive/2023-12-5',
'https://checkerproxy.net/archive/2023-12-4',
'https://checkerproxy.net/archive/2023-12-3',
'https://checkerproxy.net/archive/2023-12-2',
'https://checkerproxy.net/archive/2023-12-1',
'https://checkerproxy.net/archive/2023-11-29',
'https://checkerproxy.net/archive/2023-11-28',
'https://checkerproxy.net/archive/2023-11-27',
'https://checkerproxy.net/archive/2023-11-26',
'https://checkerproxy.net/archive/2023-11-25',
'https://checkerproxy.net/archive/2023-11-24',
'https://checkerproxy.net/archive/2023-11-23',
'https://checkerproxy.net/archive/2023-11-22',
'https://checkerproxy.net/archive/2023-11-21',
'https://checkerproxy.net/archive/2023-11-20',
'https://checkerproxy.net/archive/2023-11-19',
'https://checkerproxy.net/archive/2023-11-18',
'https://checkerproxy.net/archive/2023-11-17',
'https://checkerproxy.net/archive/2023-11-16',
'https://checkerproxy.net/archive/2023-11-15',
'https://checkerproxy.net/archive/2023-11-14',
'https://checkerproxy.net/archive/2023-11-13',
'https://checkerproxy.net/archive/2023-11-12',
'https://checkerproxy.net/archive/2023-11-11',
'https://checkerproxy.net/archive/2023-11-10',
'https://checkerproxy.net/archive/2023-11-9',
'https://checkerproxy.net/archive/2023-11-8',
'https://checkerproxy.net/archive/2023-11-7',
'https://checkerproxy.net/archive/2023-11-6',
'https://checkerproxy.net/archive/2023-11-5',
'https://checkerproxy.net/archive/2023-11-4',
'https://checkerproxy.net/archive/2023-11-3',
'https://checkerproxy.net/archive/2023-11-2',
'https://checkerproxy.net/archive/2023-11-1',
'https://checkerproxy.net/archive/2023-10-29',
'https://checkerproxy.net/archive/2023-10-28',
'https://checkerproxy.net/archive/2023-10-27',
'https://checkerproxy.net/archive/2023-10-26',
'https://checkerproxy.net/archive/2023-10-25',
'https://checkerproxy.net/archive/2023-10-24',
'https://checkerproxy.net/archive/2023-10-23',
'https://checkerproxy.net/archive/2023-10-22',
'https://checkerproxy.net/archive/2023-10-21',
'https://checkerproxy.net/archive/2023-10-20',
'https://checkerproxy.net/archive/2023-10-19',
'https://checkerproxy.net/archive/2023-10-18',
'https://checkerproxy.net/archive/2023-10-17',
'https://checkerproxy.net/archive/2023-10-16',
'https://checkerproxy.net/archive/2023-10-15',
'https://checkerproxy.net/archive/2023-10-14',
'https://checkerproxy.net/archive/2023-10-13',
'https://checkerproxy.net/archive/2023-10-12',
'https://checkerproxy.net/archive/2023-10-11',
'https://checkerproxy.net/archive/2023-10-10',
'https://checkerproxy.net/archive/2023-10-9',
'https://checkerproxy.net/archive/2023-10-8',
'https://checkerproxy.net/archive/2023-10-7',
'https://checkerproxy.net/archive/2023-10-6',
'https://checkerproxy.net/archive/2023-10-5',
'https://checkerproxy.net/archive/2023-10-4',
'https://checkerproxy.net/archive/2023-10-3',
'https://checkerproxy.net/archive/2023-10-2',
'https://checkerproxy.net/archive/2023-10-1',
'https://checkerproxy.net/archive/2023-09-29',
'https://checkerproxy.net/archive/2023-09-28',
'https://checkerproxy.net/archive/2023-09-27',
'https://checkerproxy.net/archive/2023-09-26',
'https://checkerproxy.net/archive/2023-09-25',
'https://checkerproxy.net/archive/2023-09-24',
'https://checkerproxy.net/archive/2023-09-23',
'https://checkerproxy.net/archive/2023-09-22',
'https://checkerproxy.net/archive/2023-09-21',
'https://checkerproxy.net/archive/2023-09-20',
'https://checkerproxy.net/archive/2023-09-19',
'https://checkerproxy.net/archive/2023-09-18',
'https://checkerproxy.net/archive/2023-09-17',
'https://checkerproxy.net/archive/2023-09-16',
'https://checkerproxy.net/archive/2023-09-15',
'https://checkerproxy.net/archive/2023-09-14',
'https://checkerproxy.net/archive/2023-09-13',
'https://checkerproxy.net/archive/2023-09-12',
'https://checkerproxy.net/archive/2023-09-11',
'https://checkerproxy.net/archive/2023-09-10',
'https://checkerproxy.net/archive/2023-09-9',
'https://checkerproxy.net/archive/2023-09-8',
'https://checkerproxy.net/archive/2023-09-7',
'https://checkerproxy.net/archive/2023-09-6',
'https://checkerproxy.net/archive/2023-09-5',
'https://checkerproxy.net/archive/2023-09-4',
'https://checkerproxy.net/archive/2023-09-3',
'https://checkerproxy.net/archive/2023-09-2',
'https://checkerproxy.net/archive/2023-09-1',
'https://checkerproxy.net/archive/2023-08-29',
'https://checkerproxy.net/archive/2023-08-28',
'https://checkerproxy.net/archive/2023-08-27',
'https://checkerproxy.net/archive/2023-08-26',
'https://checkerproxy.net/archive/2023-08-25',
'https://checkerproxy.net/archive/2023-08-24',
'https://checkerproxy.net/archive/2023-08-23',
'https://checkerproxy.net/archive/2023-08-22',
'https://checkerproxy.net/archive/2023-08-21',
'https://checkerproxy.net/archive/2023-08-20',
'https://checkerproxy.net/archive/2023-08-19',
'https://checkerproxy.net/archive/2023-08-18',
'https://checkerproxy.net/archive/2023-08-17',
'https://checkerproxy.net/archive/2023-08-16',
'https://checkerproxy.net/archive/2023-08-15',
'https://checkerproxy.net/archive/2023-08-14',
'https://checkerproxy.net/archive/2023-08-13',
'https://checkerproxy.net/archive/2023-08-12',
'https://checkerproxy.net/archive/2023-08-11',
'https://checkerproxy.net/archive/2023-08-10',
'https://checkerproxy.net/archive/2023-08-9',
'https://checkerproxy.net/archive/2023-08-8',
'https://checkerproxy.net/archive/2023-08-7',
'https://checkerproxy.net/archive/2023-08-6',
'https://checkerproxy.net/archive/2023-08-5',
'https://checkerproxy.net/archive/2023-08-4',
'https://checkerproxy.net/archive/2023-08-3',
'https://checkerproxy.net/archive/2023-08-2',
'https://checkerproxy.net/archive/2023-08-1',
'https://checkerproxy.net/archive/2023-07-29',
'https://checkerproxy.net/archive/2023-07-28',
'https://checkerproxy.net/archive/2023-07-27',
'https://checkerproxy.net/archive/2023-07-26',
'https://checkerproxy.net/archive/2023-07-25',
'https://checkerproxy.net/archive/2023-07-24',
'https://checkerproxy.net/archive/2023-07-23',
'https://checkerproxy.net/archive/2023-07-22',
'https://checkerproxy.net/archive/2023-07-21',
'https://checkerproxy.net/archive/2023-07-20',
'https://checkerproxy.net/archive/2023-07-19',
'https://checkerproxy.net/archive/2023-07-18',
'https://checkerproxy.net/archive/2023-07-17',
'https://checkerproxy.net/archive/2023-07-16',
'https://checkerproxy.net/archive/2023-07-15',
'https://checkerproxy.net/archive/2023-07-14',
'https://checkerproxy.net/archive/2023-07-13',
'https://checkerproxy.net/archive/2023-07-12',
'https://checkerproxy.net/archive/2023-07-11',
'https://checkerproxy.net/archive/2023-07-10',
'https://checkerproxy.net/archive/2023-07-9',
'https://checkerproxy.net/archive/2023-07-8',
'https://checkerproxy.net/archive/2023-07-7',
'https://checkerproxy.net/archive/2023-07-6',
'https://checkerproxy.net/archive/2023-07-5',
'https://checkerproxy.net/archive/2023-07-4',
'https://checkerproxy.net/archive/2023-07-3',
'https://checkerproxy.net/archive/2023-07-2',
'https://checkerproxy.net/archive/2023-07-1',
'https://advanced.name/freeproxy/661bf8a762494',
'https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/master/http.txt',
'https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/master/https.txt',
'https://raw.githubusercontent.com/mmpx12/proxy-list/master/https.txt',
'https://raw.githubusercontent.com/proxy4parsing/proxy-list/main/http.txt',
'https://raw.githubusercontent.com/Anonym0usWork1221/Free-Proxies/main/proxy_files/http_proxies.txt',
'https://raw.githubusercontent.com/Anonym0usWork1221/Free-Proxies/main/proxy_files/https_proxies.txt',
'https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt',
'https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/proxies.txt',
'https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/proxy.txt',
'http://freeproxylist-daily.blogspot.com/2013/05/usa-proxy-list-2013-05-15-0111-am-gmt8.html',
'http://freeproxylist-daily.blogspot.com/2013/05/usa-proxy-list-2013-05-13-812-gmt7.html',
'http://www.cybersyndrome.net/pla5.html',
'http://vipprox.blogspot.com/2013_06_01_archive.html',
'http://vipprox.blogspot.com/2013/05/us-proxy-servers-74_24.html',
'http://vipprox.blogspot.com/p/blog-page_7.html',
'http://vipprox.blogspot.com/2013/05/us-proxy-servers-199_20.html',
'http://vipprox.blogspot.com/2013_02_01_archive.html',
'http://alexa.lr2b.com/proxylist.txt',
'http://vipprox.blogspot.com/2013_03_01_archive.html',
'http://browse.feedreader.com/c/Proxy_Server_List-1/449196260',
'http://browse.feedreader.com/c/Proxy_Server_List-1/449196258',
'http://sock5us.blogspot.com/2013/06/01-07-13-free-proxy-server-list.html',
'http://browse.feedreader.com/c/Proxy_Server_List-1/449196251',
'http://free-ssh.blogspot.com/feeds/posts/default',
'http://browse.feedreader.com/c/Proxy_Server_List-1/449196259',
'http://sockproxy.blogspot.com/2013/04/11-04-13-socks-45.html',
'http://proxyfirenet.blogspot.com/',
'https://www.javatpoint.com/proxy-server-list',
'https://openproxy.space/list/http',
'http://proxydb.net/',
'http://olaf4snow.com/public/proxy.txt',
'http://westdollar.narod.ru/proxy.htm',
'https://openproxy.space/list/socks4',
'https://openproxy.space/list/socks5',
'http://tomoney.narod.ru/help/proxi.htm',
'http://sergei-m.narod.ru/proxy.htm',
'http://rammstein.narod.ru/proxy.html',
'http://greenrain.bos.ru/R_Stuff/Proxy.htm',
'http://inav.chat.ru/ftp/proxy.txt',
'http://johnstudio0.tripod.com/index1.htm',
'http://atomintersoft.com/transparent_proxy_list',
'http://atomintersoft.com/anonymous_proxy_list',
'http://atomintersoft.com/high_anonymity_elite_proxy_list',
'https://proxyspace.pro/http.txt',
'https://api.proxyscrape.com/?request=displayproxies&proxytype=http',
'https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt',
'http://worm.rip/http.txt',
'http://worm.rip/https.txt',
'http://alexa.lr2b.com/proxylist.txt',
'https://api.openproxylist.xyz/http.txt',
'http://rootjazz.com/proxies/proxies.txt',
'https://multiproxy.org/txt_all/proxy.txt',
'https://proxy-spider.com/api/proxies.example.txt',
'https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all',
'https://www.proxydocker.com/en/proxylist/download?email=noshare&country=all&city=all&port=all&type=all&anonymity=all&state=all&need=all',
'https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=anonymous'
'https://api.proxyscrape.com/v2/?request=displayproxies',
'https://proxyspace.pro/http.txt',
'https://api.proxyscrape.com/?request=displayproxies&proxytype=http',
'http://worm.rip/http.txt',
'https://api.openproxylist.xyz/http.txt',
'https://api.proxyscrape.com/v2/?request=displayproxies',
'https://api.proxyscrape.com/?request=displayproxies&proxytype=http',
'https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all',
'https://www.proxydocker.com/en/proxylist/download?email=noshare&country=all&city=all&port=all&type=all&anonymity=all&state=all&need=all',
'https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=anonymous',
'http://worm.rip/https.txt',
'http://alexa.lr2b.com/proxylist.txt',
'https://api.openproxylist.xyz/http.txt',
'http://rootjazz.com/proxies/proxies.txt',
'https://multiproxy.org/txt_all/proxy.txt',
'https://proxy-spider.com/api/proxies.example.txt',
'https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all',
'https://www.proxydocker.com/en/proxylist/download?email=noshare&country=all&city=all&port=all&type=all&anonymity=all&state=all&need=all',
'https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=anonymous',
]

def download_and_save_proxies(url, output_file):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            with open(output_file, 'a') as file:
                file.write(response.text)
                print(f"{Fore.GREEN}Collect {Fore.WHITE}{url} {Fore.GREEN}")
        else:
            print(f"{Fore.RED}Gagal {url}{Fore.RESET}")
    except Exception as e:
        print(f"{Fore.RED}Gagal {url}{Fore.RESET}")

open(output_file, 'w').close()

class Proxy:
    def __init__(self, method, proxy):
        if method.lower() not in ["http", "https"]:
            raise NotImplementedError("Only HTTP and HTTPS are supported")
        self.method = method.lower()
        self.proxy = proxy

    def is_valid(self):
        return re.match(r"\d{1,3}(?:\.\d{1,3}){3}(?::\d{1,5})?$", self.proxy)

    def check(self, site, timeout, user_agent):
        url = self.method + "://" + self.proxy
        proxy_support = urllib.request.ProxyHandler({self.method: url})
        opener = urllib.request.build_opener(proxy_support)
        urllib.request.install_opener(opener)
        req = urllib.request.Request(self.method + "://" + site)
        req.add_header("User-Agent", user_agent)
        try:
            start_time = time()
            urllib.request.urlopen(req, timeout=timeout)
            end_time = time()
            time_taken = end_time - start_time
            return True, time_taken, None
        except Exception as e:
            return False, 0, e

    def __str__(self):
        return self.proxy

def verbose_print(verbose, message):
    if verbose:
        print(message)

def check(file, timeout, method, site, verbose, random_user_agent):
    proxies = []
    with open(file, "r") as f:
        for line in f:
            proxies.append(Proxy(method, line.replace("\n", "")))

    print(f"{Fore.GREEN}Checking {Fore.YELLOW}{len(proxies)} {Fore.GREEN}Proxy")
    proxies = filter(lambda x: x.is_valid(), proxies)
    valid_proxies = []
    user_agent = random.choice(user_agents)

    def check_proxy(proxy, user_agent):
        new_user_agent = user_agent
        if random_user_agent:
            new_user_agent = random.choice(user_agents)
        valid, time_taken, error = proxy.check(site, timeout, new_user_agent)
        message = {
            True: f"{proxy} is valid, took {time_taken} seconds",
            False: f"{proxy} is invalid: {repr(error)}",
        }[valid]
        verbose_print(verbose, message)
        valid_proxies.extend([proxy] if valid else [])

    threads = []
    for proxy in proxies:
        t = threading.Thread(target=check_proxy, args=(proxy, user_agent))
        threads.append(t)

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    with open(file, "w") as f:
        for proxy in valid_proxies:
            f.write(str(proxy) + "\n")

    print(f"{Fore.GREEN}Found {Fore.YELLOW}{len(valid_proxies)} {Fore.GREEN}valid proxies")


def verbose_print(verbose, message):
    if verbose:
        print(message)

for url in proxy_urls:
    download_and_save_proxies(url, output_file)
    
with open('proxy.txt', 'r') as ceki:
    jumlh = sum(1 for line in ceki)
    
print(f"\n{Fore.WHITE}( {Fore.YELLOW}{jumlh} {Fore.WHITE}) {Fore.GREEN}Proxy Sudah Di Unduh, Mau Check? {Fore.WHITE}({Fore.GREEN}Y{Fore.WHITE}/{Fore.RED}N{Fore.WHITE}): ", end="")
choice = input().strip().lower()

if choice == 'y' or choice == 'Y':
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Safari/605.1.15",
    ]
    
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--timeout", type=int, default=20, help="Dismiss the proxy after -t seconds")
    parser.add_argument("-p", "--proxy", default="http", help="Check HTTPS or HTTP proxies")
    parser.add_argument("-s", "--site", default="https://google.com/", help="Check with specific website like google.com")
    parser.add_argument("-v", "--verbose", action="store_true", help="Increase output verbosity")
    parser.add_argument("-r", "--random_agent", action="store_true", help="Use a random user agent per proxy")
    
    args = parser.parse_args()
    check(file=output_file, timeout=args.timeout, method=args.proxy, site=args.site, verbose=args.verbose, random_user_agent=args.random_agent)
    sys.exit(0)
else:
    print(f"{Fore.YELLOW}Terima Kasih, Telah Menggunakan Script Saya!.\n")
