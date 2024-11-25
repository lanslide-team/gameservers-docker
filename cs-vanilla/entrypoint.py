#!/usr/bin/python3
import os
import subprocess

vars = os.environ

max_players = 5 if 'IS_WINGMAN' in vars and vars['IS_WINGMAN'] == '1' else 13

CONFIG_DIR = '/cs/cstrike'
base = ["./hlds_run", "-game cstrike", "-console", "-debug", "-usercon", "+ip 0.0.0.0"]

if not vars.get('SERVERCFGFILE'):
    vars['SERVERCFGFILE'] = 'server.cfg'

# Set server port
if vars.get('PORT'):
    base.append('-port {PORT}'.format(**vars))
    base.append('-hostport {PORT}'.format(**vars))

if vars.get('SV_LAN'):
    base.append('+sv_lan {SV_LAN}'.format(**vars))

# Set Tickrate
if vars.get('TICKRATE'):
    base.append('-tickrate {TICKRATE}'.format(**vars))

# Set GAME_TYPE
if vars.get('GAME_TYPE'):
    base.append('+game_type {GAME_TYPE}'.format(**vars))

# Set GAME_MODE
if vars.get('GAME_MODE'):
    base.append('+game_mode {GAME_MODE}'.format(**vars))

# Set RCON password
if vars.get('RCON_PASSWORD'):
    base.append('+rcon_password {RCON_PASSWORD}'.format(**vars))

# Set SV password
if vars.get('SV_PASSWORD'):
    f = open(f'{CONFIG_DIR}/' + vars['SERVERCFGFILE'], 'a')
    f.write('\nsv_password {SV_PASSWORD}'.format(**vars))
    f.close()
    base.append('+sv_password {SV_PASSWORD}'.format(**vars))

# Set Max Players
if vars.get('MAXPLAYERS_OVERRIDE'):
    base.append('+maxplayers {MAXPLAYERS_OVERRIDE}'.format(**vars))
    f = open(f'{CONFIG_DIR}/' + vars['SERVERCFGFILE'], 'a')
    f.write('\nsv_visiblemaxplayers {MAXPLAYERS_OVERRIDE}'.format(**vars))
    f.close()

# Set Map Group
if vars.get('MAP'):
   base.append('+map {MAP}'.format(**vars))

# Set Hostname
if vars.get('SERVER_NAME'):
    base.append('+hostname {SERVER_NAME}'.format(**vars))
elif vars.get('HOSTNAME'):
    base.append('+hostname {HOSTNAME}'.format(**vars))
    
    f = open(f'{CONFIG_DIR}/' + vars['SERVERCFGFILE'], 'a')
    f.write('\nhostname "{HOSTNAME}"'.format(**vars))
    f.close()


base.append('+servercfgfile {SERVERCFGFILE}'.format(**vars))

os.system("python3 config_admins.py > /cs/cstrike/addons/amxmodx/configs/users.ini")
os.system("python3 config_admins_mb.py >> /cs/cstrike/addons/matchbot/users.txt")

subprocess.call(base)

#while True:
#    time.sleep(1)
