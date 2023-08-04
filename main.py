import os
import sys
import time
from datetime import datetime, timedelta
from files.countries import COUNTRIES
from files.log_parser import parse_log_file
from files.data_processor import process_streams, get_top_n_songs
from files.file_writer import write_top_n_songs_to_file

TOP_N_SONGS = 50


def compute_top_n_songs(log_folder, output_folder, n=50):
    # Get the date of 7 days ago from today
    end_date = datetime.now() - timedelta(days=1)  # Use yesterday as the end date
    start_date = end_date - timedelta(days=7)

    weekly_counts = {country: {} for country in COUNTRIES}
    missing_log_dates = []
    total_corrupted_rows = 0

    while start_date <= end_date:
        log_date = start_date.strftime('%Y%m%d')
        log_file_1 = os.path.join(log_folder, f'listen-{log_date}.txt')
        log_file_2 = os.path.join(
            log_folder, f'listen-{start_date.strftime("%Y-%m-%d")}.txt')

        # Check if either log file format exists
        if os.path.isfile(log_file_1):
            daily_streams, corrupted_rows = parse_log_file(log_file_1)
        elif os.path.isfile(log_file_2):
            daily_streams, corrupted_rows = parse_log_file(log_file_2)
        else:
            # Log a warning for missing log files
            missing_log_dates.append(start_date.strftime("%Y-%m-%d"))
            # Move to the next day
            start_date += timedelta(days=1)
            continue

        total_corrupted_rows += corrupted_rows
        process_streams(daily_streams, weekly_counts)
        start_date += timedelta(days=1)

    # Organize error logs into dated subfolder
    today_date = datetime.now().strftime('%Y-%m-%d')
    errors_logs_folder = os.path.join(log_folder, 'errors_logs', today_date)
    os.makedirs(errors_logs_folder, exist_ok=True)

    if missing_log_dates:
        missing_log_file = os.path.join(
            errors_logs_folder, 'missing_log_files.txt')
        with open(missing_log_file, 'w') as error_log:
            error_log.write('Missing log files for the following dates:\n')
            for date in missing_log_dates:
                error_log.write(f'{date}\n')

    if total_corrupted_rows > 0:
        corrupted_rows_file = os.path.join(
            errors_logs_folder, 'corrupted_rows_summary.txt')
        with open(corrupted_rows_file, 'w') as error_log:
            error_log.write(
                f'Total corrupted rows found: {total_corrupted_rows}\n')

    top_n_songs = get_top_n_songs(weekly_counts, n=n)
    output_file = os.path.join(
        output_folder, f'country_top_{n}_{end_date.strftime("%Y%m%d")}.txt')
    write_top_n_songs_to_file(top_n_songs, output_file)


def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <top_n>")
        sys.exit(1)

    top_n = int(sys.argv[1])
    log_folder = './logs/sample_logs'
    output_folder = './logs/output_logs'

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    start_time = time.time()
    compute_top_n_songs(log_folder, output_folder, top_n)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Top {top_n} songs computed in {elapsed_time:.2f} seconds.")


if __name__ == '__main__':
    main()
