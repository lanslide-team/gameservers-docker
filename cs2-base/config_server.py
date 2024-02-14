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
    allow_players_without_match: str|None = process_env('ALLOW_PLAYERS_WITHOUT_MATCH', True);
    autoload_match_config_file: str|None = process_env('AUTOLOAD_MATCH_CONFIG_FILE', True);

    config = {
        'local': 'en',
        'allow_players_without_match': allow_players_without_match,
        'match_config_filename': 'match.json',
        'autoload_match_config_file': autoload_match_config_file
    };

    config_json: str = json.dumps(config, indent=4)
    print(config_json)


if __name__ == '__main__':
    generate_config()
