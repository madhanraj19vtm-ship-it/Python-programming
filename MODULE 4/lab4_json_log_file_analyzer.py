# MODULE 4 - LAB 4: JSON-Based Log File Analyzer
# Reads application logs from logs.json and displays records and summaries.

import json
from pathlib import Path
from collections import Counter

LOG_FILE = Path("logs.json")
VALID_LEVELS = ("INFO", "WARNING", "ERROR")

def create_sample_file():
    """Create sample JSON log data if logs.json does not exist."""
    if not LOG_FILE.exists():
        sample_logs = [
            {"timestamp": "10:00", "level": "INFO", "message": "Application started"},
            {"timestamp": "10:05", "level": "WARNING", "message": "Low disk space"},
            {"timestamp": "10:10", "level": "ERROR", "message": "Database connection failed"},
            {"timestamp": "10:15", "level": "INFO", "message": "User logged in"},
            {"timestamp": "10:20", "level": "ERROR", "message": "Unable to load profile"},
            {"timestamp": "10:25", "level": "WARNING", "message": "High memory usage"}
        ]
        with LOG_FILE.open("w", encoding="utf-8") as file:
            json.dump(sample_logs, file, indent=4)

def analyze_logs():
    create_sample_file()

    try:
        with LOG_FILE.open("r", encoding="utf-8") as file:
            logs = json.load(file)
    except FileNotFoundError:
        print("Error: Log file was not found.")
        return
    except json.JSONDecodeError:
        print("Error: logs.json contains invalid JSON data.")
        return
    except OSError as error:
        print("Unable to read the log file:", error)
        return

    if not isinstance(logs, list):
        print("Error: JSON data must contain a list of log records.")
        return

    print("\n===== JSON LOG FILE ANALYZER =====")
    print("\n----- ALL LOG RECORDS -----")

    counts = Counter()
    valid_records = 0

    for record in logs:
        if not isinstance(record, dict):
            print("Skipping invalid log record:", record)
            continue

        timestamp = record.get("timestamp", "N/A")
        level = str(record.get("level", "UNKNOWN")).upper()
        message = record.get("message", "No message")

        print(f"Timestamp: {timestamp}")
        print(f"Level:     {level}")
        print(f"Message:   {message}")
        print("-" * 35)

        if level in VALID_LEVELS:
            counts[level] += 1
        valid_records += 1

    print("\n----- LOG SUMMARY -----")
    print("Total valid log records:", valid_records)

    for level in VALID_LEVELS:
        print(f"Total {level} messages: {counts[level]}")

    unknown_count = sum(
        1 for record in logs
        if isinstance(record, dict)
        and str(record.get("level", "UNKNOWN")).upper() not in VALID_LEVELS
    )
    print("Other/unknown level messages:", unknown_count)

if __name__ == "__main__":
    analyze_logs()
