#!/usr/bin/env python3
# Author:Tyson Pellatt (tpellatt)
# Purpose: make a definiton/script that can be used to try and calcualte CPU usage

def cpu_use():
    try:
        file = open("/proc/stat", "r")
        lines = file.readlines()

        for line in lines:
            if line.startswith("cpu "):
                values = line.split()[1:]
                values = [int(v) for v in values]
                idle_time = values[3]
                total_time = sum(values)
                return (1 - (idle_time / total_time)) * 100
        file.close()
    except Exception as e:
        print("An error occured: {e}")
    return None

