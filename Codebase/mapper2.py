    # this is the mapper file only for the task number - 2


#!/usr/bin/env python
import sys

for line in sys.stdin:
    line = line.strip()
    data = line.split(",")

    # Skip header
    if len(data) < 3 or data[0] == "job_id":
        continue

    try:
        industry = data[2]
        sys.stdout.write(industry + "\t1\n")
    except:
        continue



    # this is the mapper file for the task number - 2
    # for the reducer for task 2 , no change same file.


