#!/usr/bin/env python
import sys

for line in sys.stdin:
    line = line.strip()
    data = line.split(",")

    # Skip header safely
    if len(data) < 6 or data[0] == "job_id":
        continue

    try:
        risk = float(data[5])
    except:
        continue

    if risk > 70:
        sys.stdout.write("High_Risk\t1\n")
    else:
        sys.stdout.write("Low_Risk\t1\n")