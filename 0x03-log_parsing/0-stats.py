#!/usr/bin/python3
import sys

# Initialize metrics
total_size = 0
status_codes = {}
valid_codes = [200, 301, 400, 401, 403, 404, 405, 500]

def print_stats():
    """ Print accumulated metrics """
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        print("{}: {}".format(code, status_codes[code]))

try:
    line_count = 0
    for line in sys.stdin:
        parts = line.split()
        if len(parts) < 7:
            continue
        
        # Extract relevant data
        try:
            file_size = int(parts[-1])
            status_code = int(parts[-2])
            if status_code not in valid_codes:
                continue
        except ValueError:
            continue
        
        # Update metrics
        total_size += file_size
        if status_code in status_codes:
            status_codes[status_code] += 1
        else:
            status_codes[status_code] = 1
        
        line_count += 1

        # Print statistics every 10 lines
        if line_count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    pass

# Print final statistics
print_stats()

