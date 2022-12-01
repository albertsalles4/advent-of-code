import argparse
import datetime
from pathlib import Path

PARENT_FOLDER = Path(__file__).parent
CHALLENGES_FOLDER = PARENT_FOLDER / "challenges"
TEMPLATE_FILE = CHALLENGES_FOLDER / "template.py"


def create_day_file(day: int, year: int):
    year_folder = CHALLENGES_FOLDER / str(year)
    if not year_folder.exists():
        year_folder.mkdir(parents=True, exist_ok=True)
        init_file = year_folder / "__init__.py"
        init_file.write_text("")

    day_file = year_folder / f"day{day:02d}.py"
    if day_file.exists():
        ValueError(f"Solution for day {day:02d} already exists.")

    template_content = TEMPLATE_FILE.read_text()
    day_file_content = template_content.replace(
        "DAY, YEAR = 0, 0", f"DAY, YEAR = {day}, {year}"
    )

    day_file.write_text(day_file_content)


def cli():
    parser = argparse.ArgumentParser()
    parser.add_argument("--day", type=int, help="Number of problem to set up.")
    parser.add_argument("--year", type=int, help="Year of the number to set up.")
    arguments = parser.parse_args()

    today = datetime.datetime.now()
    day = arguments.day or today.day
    year = arguments.year or today.year

    if not 1 <= day <= 25:
        raise ValueError(f"{day} must be a number between 1 and 25")
    if not 2015 <= year <= today.year:
        raise ValueError(f"{year} must be a number between 2015 and {today.year}")

    main(day=day, year=year)


def main(day: int, year: int):
    create_day_file(day, year)


if __name__ == "__main__":
    raise SystemExit(cli())
