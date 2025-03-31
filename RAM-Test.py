#!/usr/bin/env python3
# Author:Tyson Pellatt (tpellatt)
# Purpose: make a definiton/script that can be used to try and calcualte avaiable RAM/memory

def ram_usage():
    try:    
        file = open("/proc/meminfo", "r")
        lines = file.readlines()

        for lines in file:
            line_parts = lines.split(':')
            key = line_parts[0].strip()
            value = line_parts[1].strip()
            lines[key.strip()] = int(value.strip().split()[0])
        total_mem = lines['MemTotal']
        free_mem = lines['MemFree']
        used_mem = total_mem - free_mem

        print(f"Used Memory:\n{used_mem / 1024: .2f} MB")
        print(f"Free Memory:\n{free_mem / 1024: .2f} MB")
    except Exception as e:
        print("An error occured: {e}")

#testing
file = open("/proc/meminfo", "r")
lines = file.readlines()

mem_info = {}
count = 1
for line in lines:
    line_parts = line.split()
    key = line_parts[0].strip()
    value = line_parts[1].strip()
#   mem_info[key] = int(value.split()[0])
    if count == 1:
        total_mem = int(value)
    if count == 2:
        free_mem = int(value)
    count += 1

#total_mem = lines[1]['MemTotal']
#free_mem = lines['MemFree']
used_mem = int(total_mem - free_mem)

print(f"Used Memory:\n{used_mem / 1024: .2f} MB")
print(f"Free Memory:\n{free_mem / 1024: .2f} MB") 
file.close()  
#ram_usage()
