from pathlib import Path
import csv
from typing import List, Dict

DATA_PATH = Path("data/habits.csv")

def ensure_date_file() -> None:
    """Ensure the CSV file exists with headers."""
    DATA_PATH.parent.mkdir(parents=True, exist_ok=True)
    if not DATA_PATH.exists():
        with open(DATA_PATH, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["date", "feeding", "sleep", "diaper", "mood"])
            writer.writeheader()

def write_habit(row: Dict[str, str]) -> None:
    """Append a habit entry to the CSV file."""
    with open(DATA_PATH, "a", newline="") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=["date", "feeding", "sleep", "diaper", "mood"]
        )
        writer.writerow(row)

def read_habits() -> List[Dict[str, str]]:
    """Read and return all entries."""
    if not DATA_PATH.exists():
        return []

    with open(DATA_PATH, "r", newline="") as file:
        reader = csv.DictReader(file)
        return list(reader)
