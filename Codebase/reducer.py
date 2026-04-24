#!/usr/bin/env python
import sys

current_key = None
count = 0

for line in sys.stdin:
    line = line.strip()
    parts = line.split("\t")

    if len(parts) != 2:
        continue

    key = parts[0]
    try:
        value = int(parts[1])
    except:
        continue

    if current_key == key:
        count += value
    else:
        if current_key is not None:
            sys.stdout.write("%s\t%d\n" % (current_key, count))
        current_key = key
        count = value

if current_key is not None:
    sys.stdout.write("%s\t%d\n" % (current_key, count))