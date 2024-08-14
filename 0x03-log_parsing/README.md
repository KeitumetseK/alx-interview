# Log Parsing Script

This project contains a Python script `0-stats.py` that reads log entries from stdin, computes metrics, and prints statistics after every 10 lines or upon a keyboard interruption.

## Features

- Calculates the total file size.
- Tracks the number of occurrences of each HTTP status code.

## Usage

Run the generator and pipe the output to the script:

```bash
./0-generator.py | ./0-stats.py

