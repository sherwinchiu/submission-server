#!/usr/bin/env python
# -*- coding: utf-8 -*-

# week3-question1.py
# Number Addition
# Week 3, Question 1

import subprocess
import re
import os, sys
import random

sys.path.append(os.path.join(os.path.dirname(__file__),'../../'))

import driver

# Custom Tests
# Check for function declaration and definition
def test1(text):
    text1 = len(re.findall(r"double\s+sum\s*\(\s*double\s*\w+\s*\,\s*double\s*\w+\s*\)\s*;", text)) == 1
    text2 = len(re.findall(r"double\s+sum\s*\(\s*double\s*\w+\s*\,\s*double\s*\w+\s*\)\s*{", text)) == 1
    return text1 and text2

# Check for int equals
def test2(expected_out, out):
    return expected_out == out

# Check for float equals
def test3(expected_out, out):
    return abs(float(expected_out)) > abs(out)*0.99 and abs(float(expected_out)) < abs(out)*1.01

driver.set_directory(os.path.realpath(__file__))
rand1 = random.uniform(-1000, 1000)
rand2 = random.uniform(-1000, 1000)
rand3 = random.uniform(-10000, 10000)
rand4 = random.uniform(-10000, 10000)
rand_params = str(rand1) + " " + str(rand2) + " " + str(rand3) + " " + str(rand4)
try:
    file_text = driver.add_header_guards(sys.argv[1])
    driver.compile(sys.argv[1])
    output_text = driver.run_program(("./main"+sys.argv[1]+".exe " + rand_params), sys.argv[1])
    output_text = output_text.split("\r\n")
except:
    sys.exit(1)

# Delete input file
subprocess.call("make clean NUM="+sys.argv[1])
# Output results
test_outcome = [test1(file_text), test2(15, float(output_text[0])), test3(93.432, float(output_text[1])),
test3(rand1 + rand2, float(output_text[2])), test3(rand3 + rand4, float(output_text[3])) ]

driver.print_results(test_outcome, sys.argv[1])

sys.exit(0)