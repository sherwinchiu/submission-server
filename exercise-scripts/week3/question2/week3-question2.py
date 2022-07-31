#!/usr/bin/env python
# -*- coding: utf-8 -*-

# week3-question2.py
# Absolute Value
# Week 3, Question 2

import subprocess
import re
import os, sys
import random

sys.path.append(os.path.join(os.path.dirname(__file__),'../../'))

import driver

# Custom Tests
# Check for only iostream
def test1(text):
    return driver.check_includes(text, ["cmath"])

# Check for function declaration and definition
def test2(text):
    text1 = len(re.findall(r"double\s+absolute\s*\(\s*double\s*\w+\s*\)\s*;", text)) == 1
    text2 = len(re.findall(r"double\s+absolute\s*\(\s*double\s*\w+\s*\)\s*{", text)) == 1
    return text1 and text2

# Check for equals
def test3(expected_out, out):
    return abs(expected_out) > out*0.999 and abs(expected_out) < out*1.001

driver.set_directory(os.path.realpath(__file__))
rand1 = random.uniform(-1000, 1000)
rand2 = random.uniform(-1000, 10000)
rand3 = random.uniform(-10000, 10000)
rand_params = str(rand1) + " " + str(rand2) + " " + str(rand3)
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
test_outcome = [test1(file_text), test2(file_text), test3(23, float(output_text[0])), test3(-23, float(output_text[1])),
test3(rand1, float(output_text[2])), test3(rand2, float(output_text[3])), test3(rand3, float(output_text[4]))]

driver.print_results(test_outcome, sys.argv[1])

sys.exit(0)