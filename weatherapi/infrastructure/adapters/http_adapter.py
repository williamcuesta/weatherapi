import aiohttp
import logging


async def request_http_get(url, headers):
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as response:
            logging.info("Status:", response.status)
            logging.info("Content-type:", response.headers["content-type"])

            info = await response.json()
            logging.info("Body:", info)
            return info


async def request_http_post(url, data, headers):
    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=data, headers=headers) as response:
            logging.info(f"Status: {response.status}")
            logging.info(f"Content-type: {response.headers['content-type']}")
