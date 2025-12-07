from pathlib import Path

from bs4 import BeautifulSoup
import requests
from requests.exceptions import HTTPError


from aoc_2025.hidden import SESSION_ID


YEAR = 2025


def get_data(day, force=False):
    out_pth = Path(f"input_data/day{day}.txt")

    if force or not out_pth.exists():
        puzzle_input = get_personal_input(day)
        out_pth.write_text(puzzle_input)

        example_input = get_example_input(day)
        (out_pth.with_suffix(".ex.txt")).write_text(example_input)


def get_personal_input(day):
    url = f"https://adventofcode.com/{YEAR}/day/{day}/input"
    response = requests.get(url, cookies={"session": SESSION_ID})
    response.raise_for_status()
    return response.content.decode()


def get_example_input(day):
    url = f"https://adventofcode.com/{YEAR}/day/{day}"
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.content, "html.parser")
    # The example is (always?) in the first <pre> block
    ex = soup.find("pre").get_text()
    return ex


def main():
    for day in range(1, 13):
        try:
            get_data(day=day)
        except HTTPError as e:
            if e.response.status_code == 404:
                print(f"Good luck on day {day - 1}!")
                break
            raise


if __name__ == "__main__":
    main()
