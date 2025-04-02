#!/usr/bin/env python3
# Author: Wcao23


def cpu_usage():
    '''Getting a single snapshot of cpu usage'''
    # Access the CPU usage file and read the data
    try:
        cpu_file = open("/proc/stat", "r")
        lines = cpu_file.readlines()
    
    # Grab the data (user, nice, system, idle) and store it into variables

    # Calculate the total and minus idle will estimate the usage



    
    except:
        return None
 






