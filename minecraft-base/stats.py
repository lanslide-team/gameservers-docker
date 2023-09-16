import asyncio
import os
import time
from opengsq.protocols import Minecraft


class Query:
    MINECRAFT_RESPONSE: list[str] = ['description', 'players', 'version']
    DEFAULT_SLEEP: int = 5

    @classmethod
    def __process_info(cls, response: dict, response_keys: list[str]) -> dict:
        result = {}
        for tag in response_keys:
            if tag in response.keys():
                result[tag] = response[tag]
        return result

    @classmethod
    async def process_game(cls, protocol: callable, response_keys: list[str], host: str, port: int, timeout: float = 5.0) -> dict:
        while True:
            try:
                response = protocol(host=host, port=port, timeout=timeout)
                response = await response.get_status()
                processed_response = cls.__process_info(response=response, response_keys=response_keys)
            except asyncio.exceptions.TimeoutError:
                processed_response = {'Error': 'Timeout'}
            except Exception as e:
                processed_response = {'Error': str(e)}

            f = open('stats.json', 'w')
            f.write(str(processed_response))
            f.close()

            time.sleep(cls.DEFAULT_SLEEP)


if __name__ == '__main__':
    host = input().strip()
    asyncio.run(Query.process_game(protocol=Minecraft, response_keys=Query.MINECRAFT_RESPONSE, host=host, port=int(os.environ['SERVER_PORT']), timeout=1))

