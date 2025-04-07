#!/usr/bin/env python3
import sys
import re

def mapper():
    for line in sys.stdin:
        words = re.findall(r'\w+', line)
        for word in words:
            length = len(word)
            print("{}\t1".format(length))

def reducer():
    current_length = None
    current_count = 0

    for line in sys.stdin:
        try:
            length, count = line.strip().split('\t')
            length = int(length)
            count = int(count)
        except Exception as e:
            sys.stderr.write(f"Error processing line: {line}\nError: {str(e)}\n")
            continue

        if current_length == length:
            current_count += count
        else:
            if current_length is not None:
                print(f"{current_length}\t{current_count}")
            current_length = length
            current_count = count

    if current_length is not None:
        print(f"{current_length}\t{current_count}")

if __name__ == "__main__":
    if 'mapper' in sys.argv[0].lower():
        mapper()
    elif 'reducer' in sys.argv[0].lower():
        reducer()
    else:
        if sys.stdin.isatty():
            print("No input detected.")
        else:
            mapper()
