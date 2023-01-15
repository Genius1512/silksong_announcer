#!/bin/python3

from steam import Steam
from decouple import config
from json import loads


def main(STEAM_API_KEY: str, SILKSONG_APP_ID: int) -> int:
    steam = Steam(STEAM_API_KEY)
    release_date = loads(str(steam.apps.get_app_details(SILKSONG_APP_ID)))[str(SILKSONG_APP_ID)]["data"]["release_date"]["date"]
    print(release_date)

    return 0


if __name__ == "__main__":
    __import__("sys").exit(main(config("STEAM_API_KEY"), 1030300)) # type: ignore
