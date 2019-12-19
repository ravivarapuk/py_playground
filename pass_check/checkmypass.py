import requests
import hashlib
import yaml
import sys
import os


root_dir = os.path.dirname(os.path.realpath(__file__))


def _get_data(query_char):
    url = "https://api.pwnedpasswords.com/range/" + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching: {res.status_code}, Check the api end-point')
    return res


def _get_pwd_leaks_cnt(hashes, hash_to_check):
    hashes = (line.split(:) for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0
