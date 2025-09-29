#!/usr/bin/python3
import json
import os
import sys

def generate_admins():
    admin_list = []
    try:
        admin_steam_ids = os.environ['ADMIN_STEAM_IDS']
        admin_list = admin_steam_ids.rstrip(', ').split(",")
    except KeyError:
        pass

    admin_json = {}
    for admin in admin_list:
        admin = admin.strip()
        if len(sys.argv) > 1 and sys.argv[1] == 'simple':
            admin_json[admin] = 'root'
        else:
            admin_json[admin] = {'identity': admin, 'flags': ['@css/root']}
    admin_json = json.dumps(admin_json, indent=4)

    print(admin_json)


if __name__ == '__main__':
    generate_admins()

