#!/usr/bin/env python
# -*- coding: utf-8 -*-

# week1-question3.py
# Using escape characters
# Week 1, Question 3

import subprocess
import re
import os, sys

sys.path.append(os.path.join(os.path.dirname(__file__),'../../'))

import driver

# Custom Tests
def test1(text):
    return bool(re.search(r"Bob\s+said\s*,\s+\"\s*Hello\s*\"\s+to\s+his\s+neighbour", text))

def test2(text):
    return bool(re.search(r"The\s+neighbour\s+said\s*,\s+\"\s*Hello\s*\"\s+back", text))

def test3(text):
    return bool(re.search(r"Bob\s+said\s*,\s+\\\"\s*Hello\s*\\\"\s+to\s+his\s+neighbour", text))

def test4(text):
    return bool(re.search(r"The\s+neighbour\s+said\s*,\s+\\\"\s*Hello\s*\\\"\s+back", text))

def test5(text):
    return bool(re.search(r"\n", text))

def test6(text):
    return bool((len(re.findall(r"cout", text)) == 1))

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
test_outcome = [test1(output_text), test2(output_text), test3(file_text), test4(file_text), test5(file_text), test6(file_text)]

driver.print_results(test_outcome, sys.argv[1])

sys.exit(0)