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
    def run_command(cls, host: str, port: int, rcon_password: str, command: str) -> None:
        try:
            with Client(host, int(port), passwd=rcon_password) as client:
                cls.__process_command(client, command)
        except:
            pr = {'Error': 'Timeout'}

    @classmethod
    async def process_game(cls, host: str, port: int, rcon_password: str) -> dict:
        pr = {}

        if 'IS_WINGMAN' in os.environ and os.environ['IS_WINGMAN'] == '1':
            cls.run_command(host, port, rcon_password, f"game_mode 2")
            time.sleep(1)
            cls.run_command(host, port, rcon_password, f"map {os.environ['MAP']}")
            time.sleep(Query.INITIAL_SLEEP)

        # Load the match config
        cls.run_command(host, port, rcon_password, 'matchzy_loadmatch match.json')
                   
        while True:
            try:
                status_json = None
                with Client(host, int(port), passwd=rcon_password) as client:
                    hostname = cls.__process_command(client, 'hostname')
                    status_json = json.loads(cls.__process_command(client, 'status_json'))
                    sv_visiblemaxplayers = cls.__process_command(client, 'sv_visiblemaxplayers')

                    pr['Name'] = hostname
                    pr['MaxPlayers'] = sv_visiblemaxplayers

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

