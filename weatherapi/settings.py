import os
from weatherapi import __version__


class AppSettings:
    VERSION = os.getenv("VERSION", __version__).upper()
    URL = os.getenv(
        "URL",
        "http://api.openweathermap.org/data/2.5/weather"
    ).lower()
    APPID = os.getenv(
        "APPID",
        "appid=1508a9a4840a5574c822d70ca2132032"
    )
    TTL = os.getenv("TTL", 120)


APP = AppSettings()
