#!/usr/bin/env python3

import sys 

def print_command_line_args():
    print("1st Variable : ",sys.argv[1])
    print("2nd Variable : ",sys.argv[2])
    print("Script and variables : ",sys.argv[0],sys.argv[1],sys.argv[2])
    
if __name__ == "__main__":
    print_command_line_args()