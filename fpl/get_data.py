import pandas as pd
import requests

FPL_URL = "https://fantasy.premierleague.com/api/bootstrap-static/"


def get_game_data():
    # get json object from fpl api
    data = requests.get(FPL_URL).json()

    return data
