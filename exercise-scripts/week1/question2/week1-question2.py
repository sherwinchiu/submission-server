#!/usr/bin/env python
# -*- coding: utf-8 -*-

# week1-question2.py
# Print a few sentences out
# Week 1, Question 2

import subprocess
import re
import os, sys

sys.path.append(os.path.join(os.path.dirname(__file__),'../../'))

import driver

# Custom Tests
def test1(text):
    return bool(re.search(r"My\s+name\s+is\s+\w+", text))

def test2(text):
    return bool(re.search(r"I\s+want\s+to\s+learn\s+programming\s+because\s+\w+", text))

def test3(text):
    return bool(re.search(r"My\s+favorite\s+color\s+is\s+\w+", text))

def test4(text):
    return bool(re.search(r"endl\s*;", text))

def test5(text):
    return bool(re.search(r"int\s*main\s*\(\s*\)\s*{", text))

def test6(text):
    return bool(re.search(r"return\s*0\s*;", text))

driver.set_directory(os.path.realpath(__file__))
driver.compile(sys.argv[1])
try:
    file_text = open("answer"+sys.argv[1]+".cpp", "r").read()
    output_text = driver.run_program("./main"+sys.argv[1]+".exe",sys.argv[1])
except:
    sys.exit(1)

# Delete input file
subprocess.call("make clean NUM="+sys.argv[1])

# Output results
test_outcome = [test1(output_text), test2(output_text), test3(output_text), test4(output_text), test5(file_text), test6(file_text)]

driver.print_results(test_outcome, sys.argv[1])

sys.exit(0)