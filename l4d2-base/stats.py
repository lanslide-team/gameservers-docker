import asyncio
import os
import time
from opengsq.protocols import Source
from rcon.source import Client

class Query:
    SOURCE_RESPONSE: list[str] = ['name', 'map', 'players', 'max_players', 'port']
    INITIAL_SLEEP: int = 10
    DEFAULT_SLEEP: int = 5

    @classmethod
    def __process_info(cls, response: dict, response_keys: list[str]) -> dict:
        result = {}
        for tag in response_keys:
            result[tag] = getattr(response, tag)
        return result

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
                return cls.__process_command(client, command)
        except:
            pr = {'Error': 'Timeout'}

    @classmethod
    async def process_game(cls, protocol: callable, response_keys: list[str], host: str, port: int, timeout: float = 5.0, rcon_password: str = 'lanslide') -> dict:
        cls.run_command(host, port, rcon_password, f"changelevel {os.environ['MAP']} versus")
        time.sleep(1)
        cls.run_command(host, port, rcon_password, f"exec server.cfg")

        while True:
            try:
                response = protocol(host=host, port=port, timeout=timeout)
                response = await response.get_info()
                processed_response = cls.__process_info(response=response, response_keys=response_keys)
            except asyncio.exceptions.TimeoutError:
                processed_response = {'Error': 'Timeout'}

            f = open('stats.json', 'w')
            f.write(str(processed_response))
            f.close()

            time.sleep(cls.DEFAULT_SLEEP)


if __name__ == '__main__':
    host = input().strip()
    time.sleep(Query.INITIAL_SLEEP)
    asyncio.run(Query.process_game(protocol=Source, response_keys=Query.SOURCE_RESPONSE, host=host, port=27015, timeout=1, rcon_password=f"{os.environ['RCON_PASSWORD']}"))
