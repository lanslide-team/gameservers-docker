#!/usr/bin/python3
import json
import os

def commid_to_steamid(commid):
    steamid64ident = 76561197960265728
    steamid = []
    steamid.append('STEAM_0:')
    steamidacct = int(commid) - steamid64ident

    if steamidacct % 2 == 0:
        steamid.append('0:')
    else:
        steamid.append('1:')
  
    steamid.append(str(steamidacct // 2))

    return ''.join(steamid)

def generate_admins():
    admin_list = []
    try:
        admin_steam_ids = os.environ['ADMIN_STEAM_IDS']
        admin_list = admin_steam_ids.rstrip(', ').split(",")
    except KeyError:
        pass

    for admin in admin_list:
        steam_id = commid_to_steamid(admin)
        print(f'"{steam_id}" "99:z"')


if __name__ == '__main__':
    generate_admins()
