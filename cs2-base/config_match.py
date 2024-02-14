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
    allow_suicide: bool|None = process_env('ALLOW_SUICIDE', '1')
    veto_map: str|None = process_env('VETO_MAP', 'de_dust2')
    veto_map_pool: str|None = process_env('VETO_MAP_POOL', None)

    is_wingman: bool = process_env('IS_WINGMAN', '0') == '1'
    players_per_team: int = process_env('PLAYERS_PER_TEAM', 5)
    min_players_to_ready: int = process_env('MIN_PLAYERS_TO_READY', 5)
    max_rounds: int = 9*2 if is_wingman else 12*2
    max_overtime_rounds: int = process_env('MAX_OVERTIME_ROUNDS', 6)
    vote_timeout: int = process_env('VOTE_TIMEOUT', 60 * 1000)
    side_type: str = process_env('SIDE_TYPE', 'standard')
    veto_first: str = process_env('VETO_FIRST', 'team1')
    skip_veto: bool = process_env('SKIP_VETO', '0') == '1'

    config: dict = {}
    # 'de_ancient', 'de_anubis', 'de_inferno', 'de_mirage', 'de_nuke', 'de_overpass', 'de_vertigo'
    # 'de_inferno', 'de_nuke', 'de_overpass', 'de_vertigo'
    config['maplist'] = [] if veto_map_pool is None else veto_map_pool.split(",")
    config['team1'] = {'id': team1_id, 'name': team1, 'tag': team1_tag, 'flag': team1_flag}
    config['team2'] = {'id': team2_id, 'name': team2, 'tag': team2_tag, 'flag': team2_flag}
    config['matchid'] = str(match_id)
    config['num_maps'] = int(num_maps)
    config['players_per_team'] = int(players_per_team)         # 2 = wingman, 5 = comp
    config['min_players_to_ready'] = int(min_players_to_ready) # 2 = wingman, 5 = comp
    config['max_rounds'] = int(max_rounds)                     # 18 = wingman, 24 = comp
    config['max_overtime_rounds'] = int(max_overtime_rounds)   # 6 = wingman, 6 = comp
    config['vote_timeout'] = int(vote_timeout)
    config['eventula_apistats_url'] = None # f"https://dev.lan2play.de/api/matchmaking/{config['matchid']}/"
    config['eventula_apistats_token'] = "Bearer AgysgEsiZ7ZNaFs74xWC"
    config['eventula_demo_upload_url'] = "https://portal.lanslide.com.au/g5-demo-upload"
    config['allow_suicide'] = allow_suicide == '1'
    config['vote_map'] = veto_map
    config['team_mode'] = int(team_mode)

    cvars = {}
    cvars['get5_remote_log_url'] = 'https://g5.lanslide.com.au/api'
    cvars['get5_remote_log_header_key'] = 'Authorization'
    cvars['get5_remote_log_header_value'] = match_api_key
    cvars['wingman'] = "true" if is_wingman else "false"
    cvars['side_type'] = side_type
    cvars['veto_first'] = veto_first
    cvars['skip_veto'] = "true" if skip_veto else "false"
    config['cvars'] = cvars
    config_json: str = json.dumps(config, indent=4)
 
    print(config_json)


if __name__ == '__main__':
    generate_config()
