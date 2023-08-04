# Top Songs By Country

## Description

This project aims to compute the top N songs for each country based on daily logs of song streams.

## Project Structure

The project is organized as follows:

- `files/`: Contains the core functionality of the project.
  - `countries.py`: Defines the list of country codes.
  - `data_processor.py`: Processes the stream data and calculates top N songs.
  - `file_writer.py`: Writes the output to files.
  - `log_generator.py`: Generates sample log files for testing.
  - `log_parser.py`: Parses the log files.
- `logs/`: Contains various log files and outputs.
  - `daily_logs/`: Stores daily log files in the format `listen-YYYYMMDD.txt`.
  - `sample_logs/`: Contains sample log files for testing purposes.
  - `error_logs/`: Stores logs related to errors, missing log files, etc.
  - `output_logs/`: Contains output log files with top N songs.
- `main.py`: Main script to execute the computation.

## Usage

1. Create the necessary log files in the `daily_logs/` folder.
2. Run `main.py` to compute the top N songs for each country.
   - Usage: `python main.py <top_n>`

## Generating Sample Logs for Tests

You can use the `log_generator.py` script to generate sample log files for testing purposes. Here's how:

Replace `<num_streams>` with the number of stream entries you want to generate for each day.

```bash
python log_generator.py <num_streams>
```

### Computing Top N Songs

To compute the top N songs for each country, use the main.py script. Run the following command:

Replace <top_n> with the number of top songs you want to compute for each country.

```bash
python main.py <top_n>
```

## Prerequisites

- Python 3.6+
- Linux environment

## Features

Parsing daily log files from the daily_logs folder.
Computing top N songs for each country.
Writing output files to the output_logs folder.
Handling missing log files and corrupted rows.
Error logging and reporting.

## Example

To compute the top 50 songs for each country and generate log files with 1000 stream entries each, follow these steps:

Generate sample logs:

```bash
python log_generator.py 1000
```

Compute top 50 songs:

```bash
python main.py 50
```

## Important Notes

- The countries.py file contains the list of all ISO country codes.
- The errors-logs folder contains logs for missing log files and corrupted rows.
- The project uses minimal RAM by writing intermediate information to disk.
- It is designed to be readable, maintainable, and to run on Linux.
- The codebase adheres to the guidelines and constraints provided.

## Contact

For questions or support, please contact [your contact email].
