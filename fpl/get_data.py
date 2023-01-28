import requests
import json

FPL_URL = "https://fantasy.premierleague.com/api/bootstrap-static/"


def get_game_data():
    # get json object from fpl api
    data = requests.get(FPL_URL).json()
    json_pretty = data

    return json_pretty
