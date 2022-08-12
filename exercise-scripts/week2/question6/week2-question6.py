#!/usr/bin/env python
# -*- coding: utf-8 -*-

# week2-question6
# Number Guesser
# Week 2, Question 6

import subprocess
import re
import os, sys
import random

sys.path.append(os.path.join(os.path.dirname(__file__),'../../'))

import driver

def guess_num():
    send_text_forward = ""
    send_text_backward = ""
    for i in range (1, 100):
        send_text_forward += str(i)
        send_text_forward += " "
    for i in range (100, 1, -1):
        send_text_backward += str(i)
        send_text_backward += " "
    result_text = driver.run_input_program("./main"+sys.argv[1]+".exe",sys.argv[1], send_text_forward)
    if(re.search(r"lower", result_text)):
        return False
    result_text = driver.run_input_program("./main"+sys.argv[1]+".exe",sys.argv[1], send_text_backward)
    if(re.search(r"higher", result_text)):
        return False
    return True
# Custom Tests

driver.set_directory(os.path.realpath(__file__))
driver.compile(sys.argv[1])
try:
    file_text = open("answer"+sys.argv[1]+".cpp", "r").read()  

except:
    sys.exit(1)
# Output results
test_outcome = [guess_num()]

# Delete input file
subprocess.call("make clean NUM="+sys.argv[1])

driver.print_results(test_outcome, sys.argv[1])

sys.exit(0)