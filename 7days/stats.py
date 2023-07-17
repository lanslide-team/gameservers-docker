import asyncio
import os
import time
from opengsq.protocols import Source


class Query:
    SOURCE_RESPONSE: list[str] = ['Name', 'Map', 'Players', 'MaxPlayers', 'GamePort']
    DEFAULT_SLEEP: int = 5

    @classmethod
    def __process_info(cls, response: dict, response_keys: list[str]) -> dict:
        result = {}
        for tag in response_keys:
            result[tag] = response[tag]
        return result

    @classmethod
    async def process_game(cls, protocol: callable, response_keys: list[str], host: str, port: int, timeout: float = 5.0) -> dict:
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
    asyncio.run(Query.process_game(protocol=Source, response_keys=Query.SOURCE_RESPONSE, host=host, port=os.environ['SERVER_PORT'], timeout=1))

