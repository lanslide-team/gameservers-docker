#!/usr/bin/python3
import os
import subprocess
import configparser
import time

def already_in_config(file: str, search_txt: str) -> bool:
    try: 
        with open(file) as f:
            if search_txt in f.read():
                return True
    except:
        pass
    return False

def find_or_replace(file: str, search_txt: str, replace_txt: str, line_start: bool=False) -> None:
    if already_in_config(file, search_txt):
        if line_start:
            search_txt = f"^{search_txt}"
        os.system(f"sed -i '/{search_txt}/c\{replace_txt}' {file}")
    else:
        os.system(f"echo '\n{replace_txt}' >> {file}")

# Read defaultenv config
configpaser = configparser.ConfigParser()
configpaser.read('defaultenv.ini')
config = configpaser['env']
CONFIG_DIR = '/cs2/game/csgo/cfg'

# Add default envvars into vars variable
vars = {}
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

max_players = 5 if 'IS_WINGMAN' in vars and vars['IS_WINGMAN'] == '1' else 13

# insecure?
# sv_load_forced_client_names_file
# rcon_connected_clients_allow
# sv_pure 0
# net_port_try 1
base = ["./game/bin/linuxsteamrt64/cs2", "-dedicated", "-console", "-usercon", "-serverlogging", "+sv_logsdir LAN_LOGS",
        "+sv_logfile 1", f"-maxplayers_override {max_players}", "+sv_reliableavatardata 2", "+sv_lan 1", 
        "+ip 0.0.0.0", "+sv_pure 0", "+rcon_connected_clients_allow 0", "-net_port_try 1"]

if not vars.get('SERVERCFGFILE'):
    vars['SERVERCFGFILE'] = 'server.cfg'

# Set server port
if vars.get('PORT'):
    base.append('-port {PORT}'.format(**vars))
    base.append('-hostport {PORT}'.format(**vars))

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
#if vars.get('TEAM1') and vars.get('TEAM2'):
#    f = open(f'{CONFIG_DIR}/' + vars['SERVERCFGFILE'], 'a')
#    f.write('\nmp_teamname_1 {TEAM1}\nmp_teamname_2 {TEAM2}'.format(**vars))
#    f.close()

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
    base.append('-addhltv1')
    base.append('+tv_delay 0')
    base.append('+tv_delay1 7')
    base.append('+tv_advertise_watchable 0')
    base.append('+tv_enable 1')
    base.append('+tv_delaymapchange 1')
    base.append('+tv_dispatchmode 1')
    base.append('+tv_enable1 1')
    base.append('+tv_max_clients 30')
    base.append('+tv_nochat 1')
    base.append('+tv_show_allchat 0')
    base.append('+tv_port 27020')
    base.append('+tv_port1 27021')
    base.append('+tv_snapshot_rate 128')
    base.append('+tv_snapshot_rate1 128')
    base.append('+tv_password sadge')
    base.append('+tv_relaypassword relaypwdsadge')
    base.append('+tv_relayradio 0')
    base.append('+tv_relayvoice 0')

# Set TV name
if 'TV_NAME' in vars:
    if vars['TV_NAME'] == 'GOTV':
        vars['TV_NAME'] = '[TV] ' + vars['HOSTNAME']

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
#    os.system('mysql -uroot -p"{}" -hmariadb -e "CREATE DATABASE IF NOT EXISTS sourcemod;"'.format(mysql_root_password))
#    os.system('mysql -uroot -p"{}" -hmariadb sourcemod < csgo/addons/sourcemod/configs/sql-init-scripts/mysql/create_admins.sql'.format(mysql_root_password))
#    os.system('mysql -uroot -p"{}" -hmariadb < csgo/scripts/mysql-files/fresh_install.sql'.format(mysql_root_password))

os.system("hostname -I | python3 stats.py &")
os.system("python3 config_admins.py > game/csgo/cfg/MatchZy/admins.json")
os.system("python3 config_admins.py > game/csgo/addons/counterstrikesharp/configs/admins.json")
os.system("python3 config_match.py > game/csgo/match.json")

config_root = 'game/csgo/cfg/MatchZy'
matchzy_cfg = config_root + '/config.cfg'
live_cfg = config_root + '/live.cfg'
warmup_cfg = config_root + '/warmup.cfg'

# Modify MatchZy Settings
# find_or_replace(file, search_txt, replace_txt)

find_or_replace(matchzy_cfg, 'matchzy_knife_enabled_default', f"matchzy_knife_enabled_default {'true' if vars['ENABLE_KNIFE'] == '1' else 'false'}")
find_or_replace(matchzy_cfg, 'matchzy_minimum_ready_required', f"matchzy_minimum_ready_required {vars['MIN_PLAYERS_TO_READY']}")
find_or_replace(matchzy_cfg, 'matchzy_chat_prefix', f"matchzy_chat_prefix [{{Green}}{vars['EVENT_NAME']}{{Default}}]")
find_or_replace(matchzy_cfg, 'matchzy_playout_enabled_default', f"matchzy_playout_enabled_default {'true' if vars['PLAYOUT_ENABLED'] == '1' else 'false'}")
find_or_replace(matchzy_cfg, 'matchzy_demo_upload_url', f"matchzy_demo_upload_url \"{vars['DEMO_UPLOAD_URL']}\"")
find_or_replace(matchzy_cfg, 'matchzy_demo_path', f"matchzy_demo_path \"LAN_DEMOS\"", True)
find_or_replace(matchzy_cfg, 'matchzy_autostart_mode', f"matchzy_autostart_mode {vars['AUTOSTART_MODE']}")
find_or_replace(matchzy_cfg, 'matchzy_use_pause_command_for_tactical_pause', f"matchzy_use_pause_command_for_tactical_pause {'true' if vars['USE_PAUSE_FOR_TECH'] == '1' else 'false'}")

# Add new command
find_or_replace(matchzy_cfg, 'matchzy_enable_match_scrim', f"matchzy_enable_match_scrim {'true' if vars['ENABLE_MATCH_SCRIM'] == '1' else 'false'}")

# Add exta commands to the end
find_or_replace(warmup_cfg, 'matchzy_remote_log_url', f"matchzy_remote_log_url \"https://portal.lanslide.com.au/api/v1/matches/{vars['MATCH_ID']}\"")
find_or_replace(warmup_cfg, 'matchzy_remote_log_header_key', f"matchzy_remote_log_header_key Authorization")
find_or_replace(warmup_cfg, 'matchzy_remote_log_header_value', f"matchzy_remote_log_header_value \"6583bac9a2455\"")
find_or_replace(warmup_cfg, 'sv_auto_full_alltalk_during_warmup_half_end', 'sv_auto_full_alltalk_during_warmup_half_end 1')
find_or_replace(warmup_cfg, 'sv_deadtalk', 'sv_deadtalk 1')
find_or_replace(warmup_cfg, 'tv_relayvoice', 'tv_relayvoice 0')

# Logging
find_or_replace(warmup_cfg, 'log on', 'log on')
find_or_replace(warmup_cfg, 'mp_logdetail', 'mp_logdetail 3')
find_or_replace(warmup_cfg, 'mp_logmoney', 'mp_logmoney')
find_or_replace(warmup_cfg, 'mp_logdetail_items', 'mp_logdetail_items 1')
find_or_replace(warmup_cfg, 'mp_disconnect_kills_players', 'mp_disconnect_kills_players 0')

# Update live config
find_or_replace(live_cfg, 'mp_team_timeout_max', f"mp_team_timeout_max 3")
find_or_replace(live_cfg, 'mp_freezetime', f"mp_freezetime {vars['FREEZETIME']}")
find_or_replace(live_cfg, 'mp_overtime_startmoney', f"mp_overtime_startmoney {vars['OVERTIME_STARTMONEY']}")
find_or_replace(live_cfg, 'mp_team_timeout_ot_max', 'mp_team_timeout_ot_max 1')
find_or_replace(live_cfg, 'mp_team_timeout_ot_add_once', 'mp_team_timeout_ot_add_once 1')
find_or_replace(live_cfg, 'mp_team_timeout_ot_add_each', 'mp_team_timeout_ot_add_each 1')
find_or_replace(live_cfg, 'mp_technical_timeout_duration_s', 'mp_technical_timeout_duration_s 300')
find_or_replace(live_cfg, 'sv_auto_full_alltalk_during_warmup_half_end', 'sv_auto_full_alltalk_during_warmup_half_end 1')
find_or_replace(live_cfg, 'sv_deadtalk', 'sv_deadtalk 0')
find_or_replace(live_cfg, 'tv_relayvoice', 'tv_relayvoice 0')


os.system(f"echo \"{base}\" >> cmd_params")

subprocess.call(base)

while True:
    time.sleep(1)
