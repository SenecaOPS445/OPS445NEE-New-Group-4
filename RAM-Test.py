#!/usr/bin/env python3
# Author:Tyson Pellatt (tpellatt)
# Purpose: make a definiton/script that can be used to try and calcualte avaiable RAM/memory

def ram_usage():
    try:    
        file = open("/proc/meminfo", "r")
        lines = file.readlines()

        count = 1
        for line in lines:
            line_parts = line.split()
            key = line_parts[0].strip()
            value = line_parts[1].strip()
            if count == 1:
                total_mem = int(value)
            if count == 2:
                free_mem = int(value)
            count += 1
        used_mem = int(total_mem - free_mem)
        
        print(f"Used Memory:\n{used_mem / 1024: .2f} MB")
        print(f"Free Memory:\n{free_mem / 1024: .2f} MB")
        file.close()

    except Exception as e:
        print("An error occured: {e}")

ram_usage()
