#!/usr/bin/env python
# -*- coding: utf-8 -*-

# week3-question3.py
# Even or Odd
# Week 3, Question 3

import subprocess
import re
import os, sys
import random

sys.path.append(os.path.join(os.path.dirname(__file__),'../../'))

import driver

# Custom Tests
# Check for function declaration and definition
def test1(text):
    text1 = len(re.findall(r"void\s+parity\s*\(\s*int\s*\w+\s*\)\s*;", text)) == 1
    text2 = len(re.findall(r"void\s+parity\s*\(\s*int\s*\w+\s*\)\s*{", text)) == 1
    return text1 and text2

# Check for even/odd
def test2(expected_out, out):
    if(expected_out%2 == 0 and re.search(r"even", out)):
        return True
    elif(expected_out%2 == 1 and re.search(r"odd", out)):
        return True
    return False

driver.set_directory(os.path.realpath(__file__))
rand1 = random.randint(-1000, 1000)
rand2 = random.randint(-1000, 10000)
rand3 = random.randint(-10000, 10000)
rand_params = "25 10 -12 " + str(rand1) + " " + str(rand2) + " " + str(rand3)
try:
    file_text = driver.add_header_guards(sys.argv[1])
    driver.compile(sys.argv[1])
    output_text = driver.run_program(("./main"+sys.argv[1]+".exe " + rand_params), sys.argv[1])
    output_text = output_text.split(":")
except:
    sys.exit(1)
# Delete input file
subprocess.call("make clean NUM="+sys.argv[1])
# Output results
rand_params = rand_params.split(" ")
test_outcome = [test1(file_text)]
for i in range(len(output_text)):
    test_outcome.append(test2(int(rand_params[i]), output_text[i]))

driver.print_results(test_outcome, sys.argv[1])

sys.exit(0)