
# Baby Habit Tracker – Python Project

Welcome to the **Baby Habit Tracker**, a simple Python project designed to help track daily baby habits such as feeding, sleep, and diaper changes. 
This project is part of Monica’s AI Engineering learning journey.

---

## Project Overview

This project helps you:

* Record daily baby habits
* Store them in a structured format
* Save and load data from files
* Analyze habits over time (future enhancement)

It builds on your Python skills from Phase 1:

* Functions
* File handling (`read`, `write`, `append`)
* Basic modules (`math`, `random`, `datetime`)
* Error handling

---

## Features

* Add a feeding record (time, amount)
* Add a sleep record (start, end)
* Add a diaper change
* View all records
* Save data to a file
* Load data from a file

---

## Project Structure

```
python-baby-habit-tracker/
│
├── tracker.py
├── data/
    └── habits.csv
├── utils/
    └── file_handler.csv    
└── README.md
```

---

## How to Run the Project

### **1. Clone the Repository**

```
git clone https://github.com/MonicaRajeVishwakarma/python-baby-habit-tracker.git
cd python-baby-habit-tracker
```

### **2. Run the Script**

```
python tracker.py
```

### **3. Follow On-Screen Menu**

You’ll see options such as:

```
1. Add feeding record
2. Add sleep record
3. Add diaper change
4. View all records
5. Save to file
6. Load from file
7. Exit
```

Simply type the number of your choice.

---

## Example Code Snippets

### Saving to a file

```python
from pathlib import Path
import csv
from typing import List, Dict

DATA_PATH = Path("data/habits.csv")

def write_habit(row: Dict[str, str]) -> None:
    """Append a habit entry to the CSV file."""
    with open(DATA_PATH, "a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=row.keys())
        writer.writerow(row)

```

### Loading from a file

```python
from pathlib import Path
import csv
from typing import List, Dict

DATA_PATH = Path("data/habits.csv")

def read_habits() -> List[Dict[str,str]]:
    """Read and return all entries."""
    if not DATA_PATH.exists():
        return []

    with open(DATA_PATH, "r", newline="") as file:
        reader = csv.DictReader(file)
        return list(reader)
```

---

## Future Enhancements

* Convert text data to JSON
* Add charts using `matplotlib`
* Track weekly summaries
* Export reports
* Add GUI version

---

## Why This Project Matters

This project helps you:

* Apply real Python concepts to something meaningful in your life
* Build confidence working with data
* Learn how programmers organize real applications

This is your first real-world Python project — be proud!

