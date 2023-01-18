import asyncio
import os
import time
from opengsq.protocols import Quake3


class Query:
    QUAKE3_RESPONSE: list[str] = ['sv_maxclients', 'g_humanplayers', 'clients', 'mapname', 'hostname']
    DEFAULT_SLEEP: int = 5

    @classmethod
    def __process_info(cls, response: dict, response_keys: list[str]) -> dict:
        result = {}
        for tag in response_keys:
            result[tag] = response[tag]
        return result

    @classmethod
    async def process_game(cls, protocol: callable, response_keys: list[str], address: str, query_port: int, timeout: float = 5.0) -> dict:
        while True:
            try:
                response = protocol(address=address, query_port=query_port, timeout=timeout)
                response = await response.get_info()
                processed_response = cls.__process_info(response=response, response_keys=response_keys)
            except asyncio.exceptions.TimeoutError:
                processed_response = {'Error': 'Timeout'}

            f = open('stats.json', 'w')
            f.write(str(processed_response))
            f.close()

            time.sleep(cls.DEFAULT_SLEEP)


if __name__ == '__main__':
    ip = input()
    asyncio.run(Query.process_game(protocol=Quake3, response_keys=Query.QUAKE3_RESPONSE, address=ip, query_port=os.environ['NET_PORT'], timeout=1))

