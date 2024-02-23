#!/usr/bin/python3
import json
import os
import time

def process_env(key: str, default_value = None):
    try:
        return os.environ[key]
    except KeyError:
        return default_value


def generate_config() -> None:
    team1: str|None = process_env('TEAM1')
    team1_id: str|None = process_env('TEAM1_ID', '1')
    team1_tag: str|None = process_env('TEAM1_TAG', None)
    team1_flag: str|None = process_env('TEAM1_FLAG', 'AU')
    team2: str|None = process_env('TEAM2')
    team2_id: str|None = process_env('TEAM2_ID', '2')
    team2_tag: str|None = process_env('TEAM2_TAG', None)
    team2_flag: str|None = process_env('TEAM2_FLAG', 'AU')
    match_id: str = process_env('MATCH_ID', '1')
    match_api_key: str = process_env('MATCH_API_KEY', 'casper')
    num_maps: int|None = process_env('NUM_MAPS', 1)
    team_mode: int = process_env('TEAM_MODE', 0)
#    allow_suicide: bool|None = process_env('ALLOW_SUICIDE', '1')
#    veto_map: str|None = process_env('VETO_MAP', 'de_dust2')
    veto_map_pool: str|None = process_env('VETO_MAP_POOL', None)
    veto_mode: str|None = process_env('VETO_MODE', None)

    is_wingman: bool = process_env('IS_WINGMAN', '0') == '1'
    players_per_team: int = process_env('PLAYERS_PER_TEAM', 5)
    min_players_to_ready: int = process_env('MIN_PLAYERS_TO_READY', 5)
    max_rounds: int = 8*2 if is_wingman else 12*2
    max_overtime_rounds: int = process_env('MAX_OVERTIME_ROUNDS', 6)
 #   vote_timeout: int = process_env('VOTE_TIMEOUT', 60 * 1000)
    side_type: str = process_env('SIDE_TYPE', 'standard')
    veto_first: str = process_env('VETO_FIRST', 'team1')
    skip_veto: bool = process_env('SKIP_VETO', '0') == '1'
    clinch_series: bool = process_env('CLINCH_SERIES', '1') == '1'
    min_spectators_to_ready: int = process_env('MIN_SPECTATORS_TO_READY', '0')
#    eventula_apistats_token: str = process_env('EVENTULA_APISTATS_TOKEN', '');

    player_nuke = {'76561198014036883': 'Nuke'}
    player_papa = {'76561197960295774': 'Papa Smurf'}

    config: dict = {}
    # 'de_ancient', 'de_anubis', 'de_inferno', 'de_mirage', 'de_nuke', 'de_overpass', 'de_vertigo'
    # 'de_inferno', 'de_nuke', 'de_overpass', 'de_vertigo'
    config['maplist'] = [] if veto_map_pool is None else veto_map_pool.rstrip(',').split(',')
    config['veto_mode'] = [] if veto_mode is None else veto_mode.rstrip(',').split(',')
    config['team1'] = {'id': team1_id, 'name': team1, 'tag': team1_tag, 'flag': team1_flag, 'players': player_nuke}
    config['team2'] = {'id': team2_id, 'name': team2, 'tag': team2_tag, 'flag': team2_flag, 'players': player_papa}
    config['matchid'] = str(match_id)
    config['num_maps'] = int(num_maps)
    config['players_per_team'] = int(players_per_team)         # 2 = wingman, 5 = comp
    config['min_players_to_ready'] = int(min_players_to_ready) # 2 = wingman, 5 = comp
    config['min_spectators_to_ready'] = int(min_spectators_to_ready)
    config['max_rounds'] = int(max_rounds)                     # 18 = wingman, 24 = comp
    config['max_overtime_rounds'] = int(max_overtime_rounds)   # 6 = wingman, 6 = comp
#    config['vote_timeout'] = int(vote_timeout)
 #   config['eventula_apistats_url'] = None # f"https://dev.lan2play.de/api/matchmaking/{config['matchid']}/"
 #   config['eventula_apistats_token'] = "Bearer " + eventula_apistats_token
 #   config['eventula_demo_upload_url'] = "https://portal.lanslide.com.au/g5-demo-upload"
 #   config['allow_suicide'] = allow_suicide == '1'
#    config['vote_map'] = veto_map
    config['wingman'] = is_wingman
    config['side_type'] = side_type
    config['veto_first'] = veto_first
    config['skip_veto'] = skip_veto
    config['clinch_series'] = clinch_series
#    config['team_mode'] = int(team_mode)

    if 'MAP_SIDES' in os.environ:
        config['map_sides'] = os.environ['MAP_SIDES'].rstrip(',').split(',')

    cvars = {}
    cvars['get5_remote_log_url'] = 'https://g5.lanslide.com.au/api'
    cvars['get5_remote_log_header_key'] = 'Authorization'
    cvars['get5_remote_log_header_value'] = match_api_key
    cvars['mp_maxrounds'] = int(max_rounds)
    cvars['mp_freezetime'] = 10 if is_wingman else 20
    cvars['mp_overtime_startmoney'] = 12500
    cvars['sv_competitive_official_5v5'] = 0 if is_wingman else 1
    config['cvars'] = cvars
    config_json: str = json.dumps(config, indent=4)
 
    print(config_json)


if __name__ == '__main__':
    generate_config()
