#!/usr/bin/python3
import os
import subprocess

vars = os.environ

CONFIG_DIR = '/css/cstrike/cfg'
base = ["./srcds_run", "-game cstrike", "-secure", "-console", "-dev", "-usercon", "+ip 0.0.0.0"]

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

if vars['TV_ENABLE'] == '1':
    base.append('+tv_enable 1')
    try:
        tv_name = vars['TV_NAME']
    except KeyError:
        tv_name = None

    if tv_name is None or tv_name == 'GOTV':
        tv_name = f"[TV] {vars['HOSTNAME']}"
    
    f = open(f'{CONFIG_DIR}/' + vars['SERVERCFGFILE'], 'a')
    f.write(f'\ntv_name "{tv_name}"')
    f.write(f'\ntv_title "{tv_name}"')
    f.close()


os.system("python3 /css/cstrike/config_admins.py >> /css/cstrike/addons/sourcemod/configs/admins_simple.ini && rm /css/cstrike/config_admins.py -f")

subprocess.call(base)

#while True:
#    time.sleep(1)
