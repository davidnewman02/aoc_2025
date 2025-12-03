from pathlib import Path

import requests
from requests.exceptions import HTTPError


from aoc_2025.hidden import SESSION_ID


def get_data(day, force=False):
    year = 2025
    out_pth = Path(f"input_data/day{day}.txt")

    if force or not out_pth.exists():
        uri = f"https://adventofcode.com/{year}/day/{day}/input"
        response = requests.get(uri, cookies={"session": SESSION_ID})
        response.raise_for_status()
        out_pth.write_text(response.content.decode())
        (out_pth.parent / f"day{day}_ex.txt").touch()


for day in range(1, 13):
    try:
        get_data(day=day)
    except HTTPError as e:
        if e.response.status_code == 404: 
            print(f"Good luck on day {day - 1}!")
            break
        raise
