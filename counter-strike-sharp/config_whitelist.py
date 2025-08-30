#!/usr/bin/python3
import json
import os

def generate_whitelist():
    admin_list = []
    try:
        admin_steam_ids = os.environ['ADMIN_STEAM_IDS']
        admin_list = admin_steam_ids.rstrip(', ').split(",")
    except KeyError:
        pass

    print('\n'.join(admin_list))


if __name__ == '__main__':
    generate_whitelist()
