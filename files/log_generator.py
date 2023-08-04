import os
import sys
import random
from datetime import datetime, timedelta
from countries import COUNTRIES  # Importing COUNTRIES from countries.py

# Function to generate a random stream log entry


def generate_stream_entry():
    country = random.choice(COUNTRIES)
    user_id = random.randint(10000000, 99999999)
    sng_id = random.randint(10000000, 99999999)
    return f"{sng_id}|{user_id}|{country}"

# Function to generate a log file for a specific date


def generate_log_file(date_str, num_streams):
    log_filename = f"listen-{date_str}.txt"
    log_path = os.path.join("logs/sample_logs", log_filename)

    with open(log_path, "w") as file:
        for _ in range(num_streams):
            stream_entry = generate_stream_entry()
            file.write(f"{stream_entry}\n")

    print(f"Generated {num_streams} log entries in {log_filename}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python log_generator.py <num_streams>")
        sys.exit(1)

    try:
        num_streams = int(sys.argv[1])
        if num_streams <= 0:
            print("Number of streams must be a positive integer.")
            sys.exit(1)
    except ValueError:
        print("Invalid input. Number of streams must be a positive integer.")
        sys.exit(1)

    today = datetime.now()
    start_date = today - timedelta(days=7)

    while start_date <= today:
        date_str = start_date.strftime("%Y%m%d")
        generate_log_file(date_str, num_streams)
        start_date += timedelta(days=1)
