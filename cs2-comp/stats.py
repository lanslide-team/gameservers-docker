#!/usr/bin/python3

import asyncio
import json
import os
import sys
import time
from rcon.source import Client


class Query:
    SOURCE_RESPONSE: list[str] = ['Name', 'Map', 'Players', 'MaxPlayers', 'GamePort']
    INITIAL_SLEEP: int = 5
    DEFAULT_SLEEP: int = 5

    @classmethod
    def __process_command(cls, client, command):
        lines = client.run(command).split('\n')
        output = ""

        for line in lines:
             tokens = line.split('=')
             if len(tokens) == 2:
                 output += tokens[1].strip()
             else:
                 output += line.strip()

        return output

    @classmethod
    async def process_game(cls, host: str, port: int, rcon_password: str) -> dict:
        pr = {}
        while True:
            try:
                status_json = None
                with Client(host, int(port), passwd=rcon_password) as client:
                    hostname = cls.__process_command(client, 'hostname')
                    mp_teamname_1 = cls.__process_command(client, 'mp_teamname_1')
                    mp_teamname_2 = cls.__process_command(client, 'mp_teamname_2')
                    status_json = json.loads(cls.__process_command(client, 'status_json'))
                    sv_visiblemaxplayers = cls.__process_command(client, 'sv_visiblemaxplayers')
#                    match_state = cls.__process_command(client, 'ps_matchstate')
#                    mapscore_json = cls.__process_command(client, 'ps_mapscore_json')
                    get5_status = json.loads(cls.__process_command(client, 'get5_status'))

#                    if 'match is running' in match_state.lower():
#                        match_state = ''
#                    if 'match is running' in mapscore_json.lower():
#                        mapscore_json = ''

                    pr['Name'] = hostname
                    pr['MaxPlayers'] = sv_visiblemaxplayers
                    
#                    pr['MatchState'] = None if 'Unknown command' in match_state else match_state
#                    pr['MapScoreJSON'] = None if 'Unknown command' in mapscore_json else mapscore_json
                    pr['Get5Status'] = None if 'Unknown command' in get5_status else get5_status
                     

                    try:
                        pr['Players'] = status_json['server']['clients_human']
                    except KeyError:
                        pr['Players'] = None

                    try:
                        pr['Map'] = status_json['server']['map']
                    except KeyError:
                        pr['Map'] = None

            except asyncio.exceptions.TimeoutError:
                pr = {'Error': 'Timeout'}
            except: 
                pr = {'Error': 'Timeout'}

            with open('/cs2/stats.json', 'w', encoding='utf-8') as f:
                json.dump(pr, f, ensure_ascii=False, indent=4)

            time.sleep(cls.DEFAULT_SLEEP)


if __name__ == '__main__':
    host = input().strip()
    time.sleep(Query.INITIAL_SLEEP)
    asyncio.run(Query.process_game(host=host, port=os.environ['PORT'], rcon_password=os.environ['RCON_PASSWORD']))

