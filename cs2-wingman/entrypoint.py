#!/usr/bin/python3
import os
import subprocess
import configparser


base = ["./game/bin/linuxsteamrt64/cs2", "-dedicated", "-console", "-usercon", "+ip 0.0.0.0"]

vars = {}

# Read defaultenv config
configpaser = configparser.ConfigParser()
configpaser.read('defaultenv.ini')
config = configpaser['env']
CONFIG_DIR = '/cs2/game/csgo/cfg'

# Add default envvars into vars variable
for k, v in config.items():
    try:
	# Since the value from configparser will be a string, match "None" and set Nonetype
        if v == 'None':
            vars[str(k).upper()] = ''
        else:
            vars[str(k).upper()] = v
    except KeyError:
        continue

# For each envvar stored, check to see if one was set in ENV and set it
for k, v in vars.items():
    try:
        vars[k] = os.environ[k]
    except KeyError:
        continue

if not vars.get('SERVERCFGFILE'):
    vars['SERVERCFGFILE'] = 'server.cfg'

# Set server port
if vars.get('PORT'):
    base.append('-port {PORT}'.format(**vars))

if vars.get('SV_LAN'):
    base.append('-sv_lan {SV_LAN}'.format(**vars))

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
#    base.append('-sv_visiblemaxplayers {MAXPLAYERS_OVERRIDE}'.format(**vars))
    f = open(f'{CONFIG_DIR}/' + vars['SERVERCFGFILE'], 'a')
    f.write('\nsv_visiblemaxplayers {MAXPLAYERS_OVERRIDE}'.format(**vars))
    f.close()

# Set Map Group
if vars.get('MAP_GROUP'):
    base.append('+map_group {MAP_GROUP}'.format(**vars))

# Set Map
if vars.get('MAP'):
   base.append('+map {MAP}'.format(**vars))

# Set Hostname
if vars.get('SERVER_NAME'):
    base.append('+hostname {SERVER_NAME}'.format(**vars))
elif vars.get('HOSTNAME'):
    base.append('+hostname {HOSTNAME}'.format(**vars))


base.append('+servercfgfile {SERVERCFGFILE}'.format(**vars))

# Set Teamnames
if vars.get('TEAM1') and vars.get('TEAM2'):
    f = open(f'{CONFIG_DIR}/' + vars['SERVERCFGFILE'], 'a')
    f.write('\nmp_teamname_1 {TEAM1}\nmp_teamname_2 {TEAM2}'.format(**vars))
    f.close()

# Set Event Name
#if vars.get('EVENT_NAME') and vars['EVENT_NAME'].strip() != '' and os.path.exists('/csgo/csgo/cfg/warmod/on_map_load.cfg'):
#    f = open('/csgo/csgo/cfg/warmod/on_map_load.cfg', 'a')
#    f.write('wm_competition "{EVENT_NAME}"\nwm_event "{EVENT_NAME}"\nwm_chat_prefix "{EVENT_NAME}"\n'.format(**vars))
#    f.close()

# Add STEAMTOKEN if required
if vars.get('STEAMTOKEN'):
    base.append('+sv_setsteamaccount {STEAMTOKEN}'.format(**vars))
#else:
#    f = open(f'{CONFIG_DIR}/' + vars['SERVERCFGFILE'], 'a')
#    f.write('\nsv_lan 1\n')
#    f.close()

# Enable TV
if vars.get('TV_ENABLE') and vars['TV_ENABLE'] == '1':
    base.append('+tv_enable 1')

# Set TV name
if 'TV_NAME' in vars:
    base.append('+tv_name {TV_NAME}'.format(**vars))
    base.append('+tv_title {TV_NAME}'.format(**vars))

# Set challonge match number
#if vars.get('MATCH_NO') and vars['MATCH_NO'].strip() != '':
#    f = open('/csgo/csgo/cfg/warmod/on_map_load.cfg', 'a')
#    f.write('\nls_match_no "{MATCH_NO}"'.format(**vars))
#    f.close()
    #base.append('+ls_challonge "{LS_CHALLONGE}"'.format(**vars))

if os.path.exists('csgo/scripts/mysql-files/fresh_install.sql'):
    mysql_root_password = os.popen('echo -n l33t | sha256sum | base64 | head -c 32 ; echo').read().strip()
    os.system('mysql -uroot -p"{}" -hmariadb -e "CREATE DATABASE IF NOT EXISTS sourcemod;"'.format(mysql_root_password))
    os.system('mysql -uroot -p"{}" -hmariadb sourcemod < csgo/addons/sourcemod/configs/sql-init-scripts/mysql/create_admins.sql'.format(mysql_root_password))
    os.system('mysql -uroot -p"{}" -hmariadb < csgo/scripts/mysql-files/fresh_install.sql'.format(mysql_root_password))

#os.system("hostname -I | python3 stats.py &")

print(base)
subprocess.call(base)
