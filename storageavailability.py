from datetime import datetime
from time import sleep

# read in path to tmpfile
tmpfile = '/tmp/timestamp'

# enter loop
while(True):
    # generate time now
    timestamp = str(datetime.now())

    # write time to the file
    try:
        f = open(tmpfile, "w")
        f.write(timestamp)
        f.close()
    except IOError:
        print(f"Problem writing to file at {timestamp}")

    sleep(1)

    # read file back
    try:
        f = open(tmpfile, "r")
        readtime = f.readline()
        f.close()
    except IOError:
        print(f"Problem reading from file at {timestamp}")

    if readtime == timestamp:
        print(f"Consistent at {timestamp}")
    else:
        print(f"Timestamp inconsistent at {timestamp}")