from queue import Queue
import random

proxies = [
    {"ip": "207.244.217.165:6712", "username": "bchcorqb", "password": "iqvp6jozfsf9"},
    {"ip": "107.172.163.27:6543", "username": "bchcorqb", "password": "iqvp6jozfsf9"},
    {"ip": "64.137.42.112:5157", "username": "bchcorqb", "password": "iqvp6jozfsf9"},
    {"ip": "173.211.0.148:6641", "username": "bchcorqb", "password": "iqvp6jozfsf9"},
    {"ip": "161.123.152.115:6360", "username": "bchcorqb", "password": "iqvp6jozfsf9"},
    {"ip": "167.160.180.203:6754", "username": "bchcorqb", "password": "iqvp6jozfsf9"},
    {"ip": "154.36.110.199:6853", "username": "bchcorqb", "password": "iqvp6jozfsf9"},
    {"ip": "173.0.9.70:5653", "username": "bchcorqb", "password": "iqvp6jozfsf9"},
    {"ip": "173.0.9.209:5792", "username": "bchcorqb", "password": "iqvp6jozfsf9"}
]

available_proxies = Queue(maxsize=len(proxies))

def get_random_proxy():
    return random.choice(proxies)

for proxy in proxies:
    available_proxies.put(proxy)