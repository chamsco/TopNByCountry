# Function to parse the log file and return a list of streams along with the number of corrupted rows
def parse_log_file(log_file):
    streams = []
    corrupted_rows = 0

    with open(log_file, 'r') as file:
        for line_num, line in enumerate(file, start=1):
            try:
                sng_id, user_id, country = map(
                    str.strip, line.strip().split('|'))
                streams.append(
                    {'sng_id': sng_id, 'user_id': user_id, 'country': country})
            except ValueError:
                # Log corrupted row
                with open('errors-logs/corrupted_rows.txt', 'a') as error_log:
                    error_log.write(
                        f'Corrupted row in {log_file}, line {line_num}: {line}\n')
                corrupted_rows += 1
    return streams, corrupted_rows
