#!/usr/bin/python3
import json
import os

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
        admin_json[admin] = {'identity': admin, 'flags': ['@css/root', '@pugsharp/matchadmin']}
    admin_json = json.dumps(admin_json, indent=4)

    print(admin_json)


if __name__ == '__main__':
    generate_admins()
