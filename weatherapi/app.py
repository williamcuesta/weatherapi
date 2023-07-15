import os
import logging
import uvicorn

from fastapi import FastAPI

from .router import router
from fastapi_cache import FastAPICache
from fastapi_cache.backends.inmemory import InMemoryBackend

app = FastAPI()

app.include_router(router)


logging.basicConfig(level=logging.DEBUG)


@app.on_event("startup")
async def startup():
    FastAPICache.init(InMemoryBackend())


if __name__ == "__main__":
    pid = os.getpid()
    logging.info(f"{pid}|Starting application...")

    uvicorn.run(app, host="0.0.0.0", port=8000)
