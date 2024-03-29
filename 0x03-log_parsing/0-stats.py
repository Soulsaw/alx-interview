#!/usr/bin/python3
"""Module doc"""

import sys
from collections import defaultdict
"""Import doc"""


def compute_metrics(lines):
    total_size = 0
    status_count = defaultdict(int)

    for line in lines:
        parts = line.split()
        if len(parts) != 7:
            continue

        try:
            status_code = int(parts[5])
            file_size = int(parts[6])
        except ValueError:
            continue

        total_size += file_size
        status_count[status_code] += 1

    return total_size, status_count

def print_metrics(total_size, status_count):
    print("Total file size:", total_size)
    for code in sorted(status_count.keys()):
        print(f"{code}: {status_count[code]}")

def main():
    lines = []
    try:
        for line in sys.stdin:
            lines.append(line.strip())
            if len(lines) >= 10:
                total_size, status_count = compute_metrics(lines)
                print_metrics(total_size, status_count)
                lines = []
    except KeyboardInterrupt:
        total_size, status_count = compute_metrics(lines)
        print_metrics(total_size, status_count)


if __name__ == "__main__":
    main()
