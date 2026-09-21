from api_key import API_KEY
import requests




VERBOSE = True
TEAM_ID = 81  # FC Barcelona
URL = f"https://api.football-data.org/v4/teams/{TEAM_ID}"

if VERBOSE:
    print(f'\n ====================')
    print(f'Team ID: {TEAM_ID}')
    print(f'\n ====================')

headers = {
    "X-Auth-Token": API_KEY,
}