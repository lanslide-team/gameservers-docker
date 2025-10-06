#!/usr/bin/python3
import os
import subprocess
import configparser
import sys
import time
from pathlib import Path

if len(sys.argv) < 2:
    print(f"Usage: {sys.argv[0]} <type>")
    sys.exit(1)

# Assign the first argument to variable 'type'
docker_type = sys.argv[1]

def already_in_config(file: str, search_txt: str) -> bool:
    """Return True if search_txt is found anywhere in the file."""
    try:
        with open(file, "r", encoding="utf-8") as f:
            return any(search_txt in line for line in f)
    except FileNotFoundError:
        return False

def find_or_replace(file: str, search_txt: str, replace_txt: str, line_start: bool = False) -> None:
    """
    Replace a line containing search_txt (anchored if line_start=True),
    or append replace_txt at the end. Ensures the file ends with a newline
    before appending so no content is merged.
    """
    Path(file).touch(exist_ok=True)  # create empty file if it doesn't exist

    if already_in_config(file, search_txt):
        if line_start:
            search_txt = f"^{search_txt}"
        os.system(f"sed -i '/{search_txt}/c\\{replace_txt}' {file}")
    else:
        size = os.path.getsize(file)
        needs_newline = False

        if size > 0:  # only check if the file has content
            with open(file, "rb") as f:
                f.seek(-1, os.SEEK_END)
                needs_newline = f.read(1) != b"\n"

        with open(file, "a", encoding="utf-8") as f:
            if needs_newline:
                f.write("\n")
            f.write(f"{replace_txt}\n")

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

# Override default config
if docker_type == 'armsrace':
    vars['SV_HOSTNAME'] = 'CS2 Armsrace Server';
    vars['GAME_ALIAS'] = 'armsrace';
    vars['MAP'] = 'ar_shoots';
elif docker_type == 'wingman':
    vars['SV_HOSTNAME'] = 'CS2 Wingman Server';
    vars['GAME_ALIAS'] = 'wingman';
    vars['MAP'] = 'de_inferno';
    vars['IS_WINGMAN'] = 1;
    vars['PLAYERS_PER_TEAM'] = 2;
    vars['WHITELIST_ENABLED'] = 1;
elif docker_type == 'comp':
    vars['WHITELIST_ENABLED'] = 1;

# For each envvar stored, check to see if one was set in ENV and set it
for k, v in vars.items():
    try:
        vars[k] = os.environ[k]
    except KeyError:
        continue


max_players = 5 if 'IS_WINGMAN' in vars and vars['IS_WINGMAN'] == '1' else 13

logs_folder = 'LAN_LOGS'
if vars.get('MATCH_ID'):
    logs_folder = f"{logs_folder}/{vars.get('MATCH_ID')}"

base = ["./game/bin/linuxsteamrt64/cs2", "-dedicated", "-console", "-usercon", "-serverlogging", f"+sv_logsdir {logs_folder}",
        "+sv_logfile 1", f"-maxplayers_override {max_players}", "+ip 0.0.0.0", "+rcon_connected_clients_allow 1"]

if not vars.get('SERVERCFGFILE'):
    vars['SERVERCFGFILE'] = 'server.cfg'

# Set server port
if vars.get('PORT'):
    base.append('-port {PORT}'.format(**vars))
    base.append('-hostport {PORT}'.format(**vars))

if vars.get('SV_LAN'):
    base.append('+sv_lan {SV_LAN}'.format(**vars))

# Set GAME_ALIAS
if vars.get('GAME_ALIAS'):
    base.append('+game_alias {GAME_ALIAS}'.format(**vars))

# Set hibernation
if vars.get('SV_HIBERNATE_WHEN_EMPTY'):
    base.append('+sv_hibernate_when_empty {SV_HIBERNATE_WHEN_EMPTY}'.format(**vars));

# Set RCON password
if vars.get('RCON_PASSWORD'):
    base.append('+rcon_password {RCON_PASSWORD}'.format(**vars))

cfg_dir = 'game/csgo/cfg';
server_cfg = f"{cfg_dir}/server.cfg"
armsrace_cfg = f"{cfg_dir}/gamemode_armsrace_server.cfg"
competitive_cfg = f"{cfg_dir}/gamemode_competitive_server.cfg"
wingman_cfg = f"{cfg_dir}/gamemode_competitive2v2_server.cfg"

# Set SV password
if vars.get('SV_PASSWORD'):
    find_or_replace(server_cfg, 'sv_password', f"sv_password \"{vars['SV_PASSWORD']}\"")

# Set Max Players
if vars.get('MAXPLAYERS_OVERRIDE'):
    find_or_replace(server_cfg, 'sv_visiblemaxplayers', f"sv_visiblemaxplayers {vars['MAXPLAYERS_OVERRIDE']}")

# Set Map Group
#if vars.get('MAP_GROUP'):
#    base.append('+map_group {MAP_GROUP}'.format(**vars))

# Set Map
if vars.get('MAP'):
   base.append('+map {MAP}'.format(**vars))

# Set Hostname
if vars.get('SERVER_NAME'):
    base.append('+hostname {SERVER_NAME}'.format(**vars))
elif vars.get('SV_HOSTNAME'):
    base.append('+hostname {SV_HOSTNAME}'.format(**vars))


base.append('+servercfgfile {SERVERCFGFILE}'.format(**vars))

# Enable TV
if vars.get('TV_ENABLE') and vars['TV_ENABLE'] == '1':
    base.append('-addhltv')
    base.append('-addhltv1')

# Set TV name
if 'TV_NAME' in vars:
    if vars['TV_NAME'] == 'GOTV':
        vars['TV_NAME'] = '[TV] ' + vars['SV_HOSTNAME']

#if os.path.exists('csgo/scripts/mysql-files/fresh_install.sql'):
mysql_root_password = os.popen('echo -n l33t | sha256sum | base64 | head -c 32 ; echo').read().strip()
#os.system('mysql -uroot -p"{}" -hmariadb -e "CREATE DATABASE IF NOT EXISTS matchzy;"'.format(mysql_root_password))

os.system(f"hostname -I | python3 stats.py {docker_type} &")

if docker_type == 'comp' or docker_type == 'wingman':
    os.system("python3 config_admins.py simple > game/csgo/cfg/MatchZy/admins.json")
    os.system("python3 config_whitelist.py > game/csgo/cfg/MatchZy/whitelist.cfg")
    os.system("python3 config_admins.py > game/csgo/addons/counterstrikesharp/configs/admins.json")
    os.system("python3 config_match.py > game/csgo/match.json")

    config_root = 'game/csgo/cfg/MatchZy'
    matchzy_cfg = config_root + '/config.cfg'
    database_cfg = config_root + '/database.json'
    live_cfg = config_root + '/live.cfg'
    live_wingman_cfg = config_root + '/live_wingman.cfg'
    warmup_cfg = config_root + '/warmup.cfg'

    find_or_replace(matchzy_cfg, 'matchzy_whitelist_enabled_default', f"matchzy_whitelist_enabled_default {'true' if vars['WHITELIST_ENABLED'] == '1' else 'false'}")
    find_or_replace(matchzy_cfg, 'matchzy_knife_enabled_default', f"matchzy_knife_enabled_default {'true' if vars['ENABLE_KNIFE'] == '1' else 'false'}")
    find_or_replace(matchzy_cfg, 'matchzy_minimum_ready_required', f"matchzy_minimum_ready_required {vars['MIN_PLAYERS_TO_READY']}")
    find_or_replace(matchzy_cfg, 'matchzy_demo_path', f"matchzy_demo_path \"{vars['DEMO_PATH']}\"", True)
    find_or_replace(matchzy_cfg, 'matchzy_demo_name_format ', f"matchzy_demo_name_format \"{vars['DEMO_NAME_FORMAT']}\"", True)
    find_or_replace(matchzy_cfg, 'matchzy_stop_command_available', f"matchzy_stop_command_available {'true' if vars['ENABLE_STOP_COMMAND'] == '1' else 'false'}", True)
    find_or_replace(matchzy_cfg, 'matchzy_stop_command_no_damage', f"matchzy_stop_command_no_damage {'true' if vars['ENABLE_STOP_NO_DAMAGE'] == '1' else 'false'}", True)
    find_or_replace(matchzy_cfg, 'matchzy_use_pause_command_for_tactical_pause', f"matchzy_use_pause_command_for_tactical_pause {'true' if vars['USE_PAUSE_COMMAND_FOR_TAC'] == '1' else 'false'}", True)
    find_or_replace(matchzy_cfg, 'matchzy_enable_tech_pause', f"matchzy_enable_tech_pause {'true' if vars['ENABLE_TECH_PAUSE'] == '1' else 'false'}")
    find_or_replace(matchzy_cfg, 'matchzy_tech_pause_duration', f"matchzy_tech_pause_duration {vars['TECH_PAUSE_DURATION']}")
    find_or_replace(matchzy_cfg, 'matchzy_max_tech_pauses_allowed', f"matchzy_max_tech_pauses_allowed {vars['MAX_TECH_PAUSES']}")
    find_or_replace(matchzy_cfg, 'matchzy_pause_after_restore', f"matchzy_pause_after_restore {'true' if vars['PAUSE_AFTER_RESTORE'] == '1' else 'false'}")
    find_or_replace(matchzy_cfg, 'matchzy_chat_prefix', f"matchzy_chat_prefix [{{Green}}{vars['EVENT_NAME']}{{Default}}]")
    find_or_replace(matchzy_cfg, 'matchzy_admin_chat_prefix', f"matchzy_admin_chat_prefix {vars['ADMIN_CHAT_PREFIX']}")
    find_or_replace(matchzy_cfg, 'matchzy_chat_messages_timer_delay', f"matchzy_chat_messages_timer_delay {vars['CHAT_MESSAGES_TIMER_DELAY']}")
    find_or_replace(matchzy_cfg, 'matchzy_playout_enabled_default', f"matchzy_playout_enabled_default {'true' if vars['PLAYOUT_ENABLED'] == '1' else 'false'}")
    find_or_replace(matchzy_cfg, 'matchzy_kick_when_no_match_loaded', f"matchzy_kick_when_no_match_loaded {'true' if vars['KICK_WHEN_NO_MATCH'] == '1' else 'false'}")
    find_or_replace(matchzy_cfg, 'matchzy_reset_cvars_on_series_end', f"matchzy_reset_cvars_on_series_end {'true' if vars['RESET_CVARS_ON_SERIES_END'] == '1' else 'false'}")
    find_or_replace(matchzy_cfg, 'matchzy_demo_upload_url', f"matchzy_demo_upload_url \"{vars['DEMO_UPLOAD_URL']}\"")
    find_or_replace(matchzy_cfg, 'matchzy_autostart_mode', f"matchzy_autostart_mode {vars['AUTOSTART_MODE']}")
    find_or_replace(matchzy_cfg, 'matchzy_save_nades_as_global_enabled', f"matchzy_save_nades_as_global_enabled {'true' if vars['SAVE_NADES_AS_GLOBAL'] == '1' else 'false'}")
    find_or_replace(matchzy_cfg, 'matchzy_allow_force_ready', f"matchzy_allow_force_ready {'true' if vars['ALLOW_FORCE_READY'] == '1' else 'false'}")
    find_or_replace(matchzy_cfg, 'matchzy_max_saved_last_grenades', f"matchzy_max_saved_last_grenades {vars['MAX_SAVED_LAST_GRENADE']}")
    find_or_replace(matchzy_cfg, 'matchzy_smoke_color_enabled', f"matchzy_smoke_color_enabled {'true' if vars['SMOKE_COLOR_ENABLED'] == '1' else 'false'}")
    find_or_replace(matchzy_cfg, 'matchzy_everyone_is_admin', f"matchzy_everyone_is_admin {'true' if vars['EVERYONE_IS_ADMIN'] == '1' else 'false'}")
    find_or_replace(matchzy_cfg, 'matchzy_show_credits_on_match_start', f"matchzy_show_credits_on_match_start {'true' if vars['SHOW_CREDITS_AT_MATCH_START'] == '1' else 'false'}")
    find_or_replace(matchzy_cfg, 'matchzy_hostname_format', f"matchzy_hostname_format \"{vars['HOSTNAME_FORMAT']}\"")

    find_or_replace(matchzy_cfg, 'matchzy_enable_damage_report', f"matchzy_enable_damage_report {'true' if vars['ENABLE_DAMAGE_REPORT'] == '1' else 'false'}")
    find_or_replace(matchzy_cfg, 'matchzy_match_start_message', f"matchzy_match_start_message {vars['MATCH_START_MESSAGE']}")
    find_or_replace(matchzy_cfg, 'matchzy_enable_match_scrim', f"matchzy_enable_match_scrim {'true' if vars['ENABLE_MATCH_SCRIM'] == '1' else 'false'}")

    # Backup [Round log details]
    # find_or_replace(matchzy_cfg, 'matchzy_remote_backup_url', f"matchzy_remote_backup_url \"https://portal.lanslide.com.au/api/v1/backup/\"")
    # find_or_replace(matchzy_cfg, 'matchzy_remote_backup_header_key', f"matchzy_remote_backup_header_key Authorization")
    # find_or_replace(matchzy_cfg, 'matchzy_remote_backup_header_value', f"matchzy_remote_backup_header_value \"{vars['MATCH_API_KEY']}\"")

    #find_or_replace(database_cfg, '"DatabaseType"', f"    \"DatabaseType\": \"MySQL\",", False)
    find_or_replace(database_cfg, '"MySqlHost"', f"    \"MySqlHost\": \"mariadb\",", False)
    find_or_replace(database_cfg, '"MySqlDatabase"', f"    \"MySqlDatabase\": \"matchzy\",", False)
    find_or_replace(database_cfg, '"MySqlUsername"', f"    \"MySqlUsername\": \"root\",", False)
    find_or_replace(database_cfg, '"MySqlPassword"', f"    \"MySqlPassword\": \"{mysql_root_password}\",", False)

    # Add exta commands to the end
    find_or_replace(warmup_cfg, 'mp_warmup_pausetimer', f"mp_warmup_pausetimer {vars['MP_WARMUP_PAUSETIMER']}")
    find_or_replace(warmup_cfg, 'mp_warmuptime', f"mp_warmuptime {vars['MP_WARMUPTIME']}")
    find_or_replace(warmup_cfg, 'sv_auto_full_alltalk_during_warmup_half_end', f"sv_auto_full_alltalk_during_warmup_half_end 1")

    # LIVE
    
    # Update live config
    find_or_replace(live_cfg, 'mp_disconnect_kills_players', f"mp_disconnect_kills_players {vars['MP_DISCONNECT_KILLS_PLAYS']}")
    find_or_replace(live_cfg, 'mp_freezetime', f"mp_freezetime {vars['FREEZETIME']}")
    find_or_replace(live_cfg, 'mp_overtime_startmoney', f"mp_overtime_startmoney {vars['OVERTIME_STARTMONEY']}")
    find_or_replace(live_cfg, 'sv_auto_full_alltalk_during_warmup_half_end', f"sv_auto_full_alltalk_during_warmup_half_end {vars['SV_AUTO_FULL_ALLTALK_DURING_WARMUP_HALF_END']}")
    find_or_replace(live_cfg, 'sv_hibernate_postgame_delay', f"sv_hibernate_postgame_delay {vars['SV_HIBERNATE_POSTGAME_DELAY']}", True)
    find_or_replace(live_cfg, 'sv_deadtalk', f"sv_deadtalk {vars['SV_DEADTALK']}")
    find_or_replace(live_cfg, 'sv_logecho', f"sv_logecho {vars['SV_LOGECHO']}", True)

    # Timeouts
    find_or_replace(live_cfg, 'mp_team_timeout_max', f"mp_team_timeout_max {vars['MP_TEAM_TIMEOUT_MAX']}")
    find_or_replace(live_cfg, 'mp_team_timeout_ot_max', f"mp_team_timeout_ot_max {vars['MP_TEAM_TIMEOUT_OT_MAX']}")
    find_or_replace(live_cfg, 'mp_team_timeout_time', f"mp_team_timeout_time {vars['MP_TEAM_TIMEOUT_TIME']}")
    find_or_replace(live_cfg, 'mp_team_timeout_ot_add_once', f"mp_team_timeout_ot_add_once {vars['MP_TEAM_TIMEOUT_OT_ADD_ONCE']}")
    find_or_replace(live_cfg, 'mp_team_timeout_ot_add_each', f"mp_team_timeout_ot_add_each {vars['MP_TEAM_TIMEOUT_OT_ADD_EACH']}")
    find_or_replace(live_cfg, 'mp_technical_timeout_per_team', f"mp_technical_timeout_per_team {vars['MP_TECHNICAL_TIMEOUT_PER_TEAM']}")
    find_or_replace(live_cfg, 'mp_technical_timeout_duration_s', f"mp_technical_timeout_duration_s {vars['MP_TECHNICAL_TIMEOUT_DURATION_S']}")
    
    # LIVE WINGMAN

    # Update live config
    find_or_replace(live_wingman_cfg, 'mp_disconnect_kills_players', f"mp_disconnect_kills_players {vars['MP_DISCONNECT_KILLS_PLAYS']}")
    find_or_replace(live_wingman_cfg, 'mp_freezetime', f"mp_freezetime {vars['FREEZETIME']}")
    find_or_replace(live_wingman_cfg, 'mp_overtime_startmoney', f"mp_overtime_startmoney {vars['OVERTIME_STARTMONEY']}")
    find_or_replace(live_wingman_cfg, 'sv_auto_full_alltalk_during_warmup_half_end', f"sv_auto_full_alltalk_during_warmup_half_end {vars['SV_AUTO_FULL_ALLTALK_DURING_WARMUP_HALF_END']}")
    find_or_replace(live_wingman_cfg, 'sv_hibernate_postgame_delay', f"sv_hibernate_postgame_delay {vars['SV_HIBERNATE_POSTGAME_DELAY']}", True)
    find_or_replace(live_wingman_cfg, 'sv_deadtalk', f"sv_deadtalk {vars['SV_DEADTALK']}")
    find_or_replace(live_wingman_cfg, 'sv_logecho', f"sv_logecho {vars['SV_LOGECHO']}", True)

    # Timeouts
    find_or_replace(live_wingman_cfg, 'mp_team_timeout_max', f"mp_team_timeout_max {vars['MP_TEAM_TIMEOUT_MAX']}")
    find_or_replace(live_wingman_cfg, 'mp_team_timeout_ot_max', f"mp_team_timeout_ot_max {vars['MP_TEAM_TIMEOUT_OT_MAX']}")
    find_or_replace(live_wingman_cfg, 'mp_team_timeout_time', f"mp_team_timeout_time {vars['MP_TEAM_TIMEOUT_TIME']}")
    find_or_replace(live_wingman_cfg, 'mp_team_timeout_ot_add_once', f"mp_team_timeout_ot_add_once {vars['MP_TEAM_TIMEOUT_OT_ADD_ONCE']}")
    find_or_replace(live_wingman_cfg, 'mp_team_timeout_ot_add_each', f"mp_team_timeout_ot_add_each {vars['MP_TEAM_TIMEOUT_OT_ADD_EACH']}")
    find_or_replace(live_wingman_cfg, 'mp_technical_timeout_per_team', f"mp_technical_timeout_per_team {vars['MP_TECHNICAL_TIMEOUT_PER_TEAM']}")
    find_or_replace(live_wingman_cfg, 'mp_technical_timeout_duration_s', f"mp_technical_timeout_duration_s {vars['MP_TECHNICAL_TIMEOUT_DURATION_S']}")
 

# Warmup
find_or_replace(server_cfg, 'mp_warmup_pausetimer', f"mp_warmup_pausetimer {vars['MP_WARMUP_PAUSETIMER']}")
find_or_replace(server_cfg, 'mp_warmuptime', f"mp_warmuptime {vars['MP_WARMUPTIME']}")

# Game Settings
find_or_replace(server_cfg, 'sv_deadtalk', f"sv_deadtalk {vars['SV_DEADTALK']}")
find_or_replace(server_cfg, 'sv_hibernate_postgame_delay', f"sv_hibernate_postgame_delay {vars['SV_HIBERNATE_POSTGAME_DELAY']}", True)
find_or_replace(server_cfg, 'sv_logecho', f"sv_logecho {vars['SV_LOGECHO']}", True)

# CSTV Settings
find_or_replace(server_cfg, 'tv_advertise_watchable', f"tv_advertise_watchable {vars['TV_ADVERTISE_WATCHABLE']}", True)
find_or_replace(server_cfg, 'tv_delay ', f"tv_delay {vars['TV_DELAY']}", True)
find_or_replace(server_cfg, 'tv_delay1', f"tv_delay1 {vars['TV_DELAY1']}", True)
find_or_replace(server_cfg, 'tv_enable ', f"tv_enable {vars['TV_ENABLE']}", True)
find_or_replace(server_cfg, 'tv_enable1', f"tv_enable1 {vars['TV_ENABLE1']}", True)
find_or_replace(server_cfg, 'tv_name', f"tv_name \"{vars['TV_NAME']}\"", True)
find_or_replace(server_cfg, 'tv_nochat', f"tv_nochat {vars['TV_NOCHAT']}", True)
find_or_replace(server_cfg, 'tv_port', f"tv_port {vars['TV_PORT']}", True)
find_or_replace(server_cfg, 'tv_timeout', f"tv_timeout {vars['TV_TIMEOUT']}", True)
find_or_replace(server_cfg, 'tv_title', f"tv_title \"{vars['TV_NAME']}\"", True)

# ARMSRACE OVERRIDES
find_or_replace(armsrace_cfg, 'mp_disconnect_kills_players', f"mp_disconnect_kills_players {vars['MP_DISCONNECT_KILLS_PLAYS']}")
find_or_replace(armsrace_cfg, 'mp_freezetime', f"mp_freezetime {vars['FREEZETIME']}")

find_or_replace(armsrace_cfg, 'mp_warmuptime', f"mp_warmuptime {vars['MP_WARMUPTIME']}")

# COMPETITVE OVERRIDES
find_or_replace(competitive_cfg, 'mp_disconnect_kills_players', f"mp_disconnect_kills_players {vars['MP_DISCONNECT_KILLS_PLAYS']}")
find_or_replace(competitive_cfg, 'mp_freezetime', f"mp_freezetime {vars['FREEZETIME']}")
find_or_replace(competitive_cfg, 'mp_overtime_startmoney', f"mp_overtime_startmoney {vars['OVERTIME_STARTMONEY']}")

find_or_replace(competitive_cfg, 'mp_team_timeout_max', f"mp_team_timeout_max {vars['MP_TEAM_TIMEOUT_MAX']}")
find_or_replace(competitive_cfg, 'mp_team_timeout_ot_max', f"mp_team_timeout_ot_max {vars['MP_TEAM_TIMEOUT_OT_MAX']}")
find_or_replace(competitive_cfg, 'mp_team_timeout_time', f"mp_team_timeout_time {vars['MP_TEAM_TIMEOUT_TIME']}")
find_or_replace(competitive_cfg, 'mp_team_timeout_ot_add_once', f"mp_team_timeout_ot_add_once {vars['MP_TEAM_TIMEOUT_OT_ADD_ONCE']}")
find_or_replace(competitive_cfg, 'mp_team_timeout_ot_add_each', f"mp_team_timeout_ot_add_each {vars['MP_TEAM_TIMEOUT_OT_ADD_EACH']}")
find_or_replace(competitive_cfg, 'mp_technical_timeout_per_team', f"mp_technical_timeout_per_team {vars['MP_TECHNICAL_TIMEOUT_PER_TEAM']}")
find_or_replace(competitive_cfg, 'mp_technical_timeout_duration_s', f"mp_technical_timeout_duration_s {vars['MP_TECHNICAL_TIMEOUT_DURATION_S']}")

find_or_replace(competitive_cfg, 'sv_auto_full_alltalk_during_warmup_half_end', f"sv_auto_full_alltalk_during_warmup_half_end {vars['SV_AUTO_FULL_ALLTALK_DURING_WARMUP_HALF_END']}")
find_or_replace(competitive_cfg, 'sv_deadtalk', f"sv_deadtalk {vars['SV_DEADTALK']}")
find_or_replace(competitive_cfg, 'sv_hibernate_postgame_delay', f"sv_hibernate_postgame_delay {vars['SV_HIBERNATE_POSTGAME_DELAY']}", True)

find_or_replace(competitive_cfg, 'tv_delay ', f"tv_delay {vars['TV_DELAY']}", True)
find_or_replace(competitive_cfg, 'tv_delay1', f"tv_delay1 {vars['TV_DELAY1']}", True)

find_or_replace(competitive_cfg, 'mp_warmuptime', f"mp_warmuptime {vars['MP_WARMUPTIME']}")

# SETTINGS.CFG

# WINGMAN OVERRIDES
find_or_replace(wingman_cfg, 'mp_freezetime', f"mp_freezetime {vars['FREEZETIME']}")
find_or_replace(wingman_cfg, 'mp_overtime_startmoney', f"mp_overtime_startmoney {vars['OVERTIME_STARTMONEY']}")

find_or_replace(wingman_cfg, 'mp_team_timeout_max', f"mp_team_timeout_max {vars['MP_TEAM_TIMEOUT_MAX']}")
find_or_replace(wingman_cfg, 'mp_team_timeout_ot_max', f"mp_team_timeout_ot_max {vars['MP_TEAM_TIMEOUT_OT_MAX']}")
find_or_replace(wingman_cfg, 'mp_team_timeout_time', f"mp_team_timeout_time {vars['MP_TEAM_TIMEOUT_TIME']}")
find_or_replace(wingman_cfg, 'mp_team_timeout_ot_add_once', f"mp_team_timeout_ot_add_once {vars['MP_TEAM_TIMEOUT_OT_ADD_ONCE']}")
find_or_replace(wingman_cfg, 'mp_team_timeout_ot_add_each', f"mp_team_timeout_ot_add_each {vars['MP_TEAM_TIMEOUT_OT_ADD_EACH']}")
find_or_replace(wingman_cfg, 'mp_technical_timeout_per_team', f"mp_technical_timeout_per_team {vars['MP_TECHNICAL_TIMEOUT_PER_TEAM']}")
find_or_replace(wingman_cfg, 'mp_technical_timeout_duration_s', f"mp_technical_timeout_duration_s {vars['MP_TECHNICAL_TIMEOUT_DURATION_S']}")

find_or_replace(wingman_cfg, 'tv_delay ', f"tv_delay {vars['TV_DELAY']}", True)
find_or_replace(wingman_cfg, 'tv_delay1', f"tv_delay1 {vars['TV_DELAY1']}", True)


os.system(f"echo \"{base}\" >> cmd_params")

subprocess.call(base)

#while True:
#    time.sleep(1)

# OLD CSTV Settings

#find_or_replace(server_cfg, 'tv_allow_camera_man', f"tv_allow_camera_man {vars['TV_ALLOW_CAMERA_MAN']}", True)
#find_or_replace(server_cfg, 'tv_allow_static_shots', f"tv_allow_static_shots {vars['TV_ALLOW_STATIC_SHOTS']}", True)
#find_or_replace(server_cfg, 'tv_autorecord', f"tv_autorecord {vars['TV_AUTORECORD']}", True)
#find_or_replace(server_cfg, 'tv_chatgroupsize', f"tv_chatgroupsize {vars['TV_CHATGROUPSIZE']}", True)
#find_or_replace(server_cfg, 'tv_chattimelimit', f"tv_chattimelimit {vars['TV_CHATTIMELIMIT']}", True)
#find_or_replace(server_cfg, 'tv_debug', f"tv_debug {vars['TV_DEBUG']}", True)
#find_or_replace(server_cfg, 'tv_delay', f"tv_delay {vars['TV_DELAY']}", True)
#find_or_replace(server_cfg, 'tv_delay1', f"tv_delay {vars['TV_DELAY1']}", True)
#find_or_replace(server_cfg, 'tv_delaymapchange', f"tv_delaymapchange {vars['TV_DELAYMAPCHANGE']}", True)
#find_or_replace(server_cfg, 'tv_deltacache', f"tv_deltacache {vars['TV_DELTACACHE']}", True)
#find_or_replace(server_cfg, 'tv_dispatchmode', f"tv_dispatchmode {vars['TV_DISPATCHMODE']}", True)
#find_or_replace(server_cfg, 'tv_enable1', f"tv_enable1 {vars['TV_ENABLE1']}", True)
#find_or_replace(server_cfg, 'tv_maxclients', f"tv_maxclients {vars['TV_MAXCLIENTS']}", True)
#find_or_replace(server_cfg, 'tv_maxrate', f"tv_maxrate {vars['TV_MAXRATE']}", True)
#find_or_replace(server_cfg, 'tv_name', f"tv_name \"{vars['TV_NAME']}\"", True)
#find_or_replace(server_cfg, 'tv_overridemaster', f"tv_overridemaster {vars['TV_OVERRIDEMASTER']}", True)
#find_or_replace(server_cfg, 'tv_port', f"tv_port {vars['TV_PORT']}", True)
#find_or_replace(server_cfg, 'tv_port1', f"tv_port1 {vars['TV_PORT1']}", True)
#find_or_replace(server_cfg, 'tv_password', f"tv_password \"{vars['TV_PASSWORD']}\"", True)
#find_or_replace(server_cfg, 'tv_relaypassword', f"tv_relaypassword \"{vars['TV_RELAYPASSWORD']}\"", True)
#find_or_replace(server_cfg, 'tv_relayradio', f"tv_relayradio {vars['TV_RELAYRADIO']}", True)
#find_or_replace(server_cfg, 'tv_relayvoice', f"tv_relayvoice {vars['TV_RELAYVOICE']}", True)
#find_or_replace(server_cfg, 'tv_show_allchat', f"tv_show_allchat {vars['TV_SHOW_ALLCHAT']}", True)
#find_or_replace(server_cfg, 'tv_title', f"tv_title \"{vars['TV_NAME']}\"", True)
#find_or_replace(server_cfg, 'tv_transmitall', f"tv_transmitall {vars['TV_TRANSMITALL']}", True)
