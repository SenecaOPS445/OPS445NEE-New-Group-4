#!/usr/bin/env python3
# Author: Wcao23


def cpu_usage():
    '''Getting a single snapshot of cpu usage'''
    # Access the CPU usage file and read the data
    try:
        cpu_file = open("/proc/stat", "r")
        lines = cpu_file.readlines()
    # Grab the data (user, nice, system, idle) and store it into variables
        for line in lines:
            if lines.startswith("cpu"):
                data = line.split()
                user = data[1]
                nice = data[2]
                system = data[3]
                idle = data [4]
    # Calculate the total and minus idle will estimate the usage
                total = user+ nice+ system+ idle
                percent = 100 * (1 - (idle/total))
                return percent
    except:
        return None
 






