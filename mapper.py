#!/usr/bin/env python3
import sys

header_processed = False

for line in sys.stdin:
    line = line.strip()
    fields = line.split("\t")

    if not header_processed:
        # Kiểm tra xem dòng có chứa chuỗi 'country' (một phần của tiêu đề)
        if 'country' in line.lower():
            header_processed = True
            continue

    if len(fields) > 7:
        country = fields[0]
        try:
            temp = float(fields[7])
            print("{}\t{}".format(country, temp))
        except ValueError:
            continue