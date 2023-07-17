import aiohttp
import logging


async def request_http_get(url, headers):
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as response:
            try:
                info = await response.json()
                logging.info("Body:", info)
            except Exception as e:
                logging.info(e)
            return info
