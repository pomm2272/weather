#!/usr/bin/env python3
import sys
from collections import defaultdict

temp_sum = defaultdict(float)
temp_count = defaultdict(int)

for line in sys.stdin:
    country, temp = line.strip().split('\t')
    try:
        temp = float(temp)
        temp_sum[country] += temp
        temp_count[country] += 1
    except ValueError:
        continue

for country in temp_sum:
    avg_temp = temp_sum[country] / temp_count[country]
    print("{}\t{:.2f}".format(country, avg_temp))