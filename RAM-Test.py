#!/usr/bin/env python3
# Author:Tyson Pellatt (tpellatt)
# Purpose: make a definiton/script that can be used to try and calcualte avaiable RAM/memory

def ram_usage():
    try:    
        #open the meminfo file which holds RAM information
        file = open("/proc/meminfo", "r")
        lines = file.readlines()

        #starting with line 1 and will go though all lines in meminfo
        count = 1
        for line in lines:
            #we split up the current line and then take give key/name and value/amount
            line_parts = line.split()
            key = line_parts[0].strip()
            value = line_parts[1].strip()
            #the first 2 lines in meminfo are MemTotal/total memory and MemFree/free memory
            if count == 1:
                total_mem = int(value)
            if count == 2:
                free_mem = int(value)
            count += 1
        #to calcualte the used memory
        used_mem = int(total_mem - free_mem)
        
        #print the memory used and the amount of free memeory in MB/Megabytes
        print(f"Used Memory:\n{used_mem / 1024: .2f} MB")
        print(f"Free Memory:\n{free_mem / 1024: .2f} MB")
        file.close()
    #if an exception happend
    except Exception as e:
        print("An error occured: {e}")
