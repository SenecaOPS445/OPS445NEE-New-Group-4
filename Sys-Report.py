#!/usr/bin/env python3
# Author: miqbal37

import argparse

from ram_test import ram_usage  # import ram file
from cpu_usage import cpu_usage # import cpu file

parser = argparse.ArgumentParser(   #  create instance for argument parser class and add infor for help
                    prog='System Report',
                    description='Returns CPU and RAM Usage of the System',
                    epilog='C for CPU, R for Ram')
parser.add_argument('-c', action='store_true', help="Shows only CPU usage") # adding optional -c arguments for cpu, setting defualt value to False
parser.add_argument('-r', action='store_true', help="Shows only RAM usage") # # adding optional -r arguments for ram, setting defualt value to False
args = parser.parse_args()  # parsing arguments
args_dict = vars(args)  # creating dictionary

if args_dict['r'] == True:  # checks if 'r' is true in the dictionary
    ram_usage() 
if args_dict['c'] == True:  # checks if 'c' is true in the dictionary
    cpu_usage()
if args_dict['c'] == False and args_dict['r'] == False: # checks if both values are false in the dictionary
    ram_usage()
    cpu_usage()








