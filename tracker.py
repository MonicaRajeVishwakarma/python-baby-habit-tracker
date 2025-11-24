import logging
from typing import Dict
from utils.file_handler import ensure_date_file, read_habits, write_habit

# -----------------------------------------------------------------------------
# Configuration
# -----------------------------------------------------------------------------

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)


# -----------------------------------------------------------------------------
# Helper Functions
# -----------------------------------------------------------------------------

def prompt_for_entry() -> Dict[str, str]:
    """Prompt the user for a habit entry with basic validation."""

    date = input("Date (YYYY-MM-DD): ").strip()
    feeding = input("Feeding time: ").strip()
    sleep = input("Sleep duration (hours): ").strip()
    diaper = input("Diaper change (yes/no): ").strip().lower()
    mood = input("Baby mood: ").strip()

    # Basic validation
    if diaper not in {"yes", "no"}:
        print("Invalid diaper entry. Please type 'yes' or 'no'.")
        return {}

    if not sleep.replace('.', '', 1).isdigit():
        print("Invalid sleep duration. Must be a number.")
        return {}

    return {
        "date": date,
        "feeding": feeding,
        "sleep": sleep,
        "diaper": diaper,
        "mood": mood
    }


def display_entries() -> None:
    """Read and display all habit entries."""
    entries = read_habits()

    print("\n--- All Entries ---")
    if not entries:
        print("No entries found.")
        return

    for entry in entries:
        print(
            f"Date: {entry.get('date', '')}, "
            f"Feeding: {entry.get('feeding', '')}, "
            f"Sleep: {entry.get('sleep', '')} hrs, "
            f"Diaper: {entry.get('diaper', '')}, "
            f"Mood: {entry.get('mood', '')}"
        )


# -----------------------------------------------------------------------------
# Main Application Loop
# -----------------------------------------------------------------------------

def main() -> None:
    ensure_date_file()
    logging.info("Baby Habit Tracker started.")

    print("\nBaby Habit Tracker")
    print("====================")

    while True:
        print("\nOptions:")
        print("1. Add a habit entry")
        print("2. View all entries")
        print("3. Exit")

        choice = input("Choose an option: ").strip()

        match choice:
            case "1":
                entry = prompt_for_entry()
                if entry:
                    write_habit(entry)
                    print("Entry saved!")
                    logging.info("Entry saved successfully.")
            case "2":
                display_entries()
            case "3":
                print("Goodbye!")
                logging.info("Application shutdown by user.")
                break
            case _:
                print("Invalid option. Try again.")


if __name__ == "__main__":
    main()
