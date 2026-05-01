import csv
from typing import Tuple

class FileHandler:
    """Handles saving and loading vote data."""

    FILE_PATH: str = "data/votes.csv"

    @staticmethod
    def save(john: int, jane: int) -> None:
        """Save votes to a CSV file."""
        try:
            with open(FileHandler.FILE_PATH, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow([john, jane])
        except Exception as e:
            print(f"Error saving file: {e}")

    @staticmethod
    def load() -> Tuple[int, int]:
        """Load votes from a CSV file."""
        try:
            with open(FileHandler.FILE_PATH, "r") as file:
                reader = csv.reader(file)
                row = next(reader)
                return int(row[0]), int(row[1])
        except FileNotFoundError:
            return 0,0
        except Exception as e:
            print(f"Error loading file: {e}")
            return 0,0