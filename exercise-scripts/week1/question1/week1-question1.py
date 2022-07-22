#!/usr/bin/env python
# -*- coding: utf-8 -*-

# week1-question1.py
# Hello World! 
# Week 1, Question 1

import subprocess
import re
import os, sys

sys.path.append(os.path.join(os.path.dirname(__file__),'../../'))

import driver

# Custom Tests
# Check for Hello World! text
def test1(text):
    return bool(re.search(r"Hello World!", text))

# Check for Hello
def test2(text):
    return bool(re.search(r"Hello", text))

# Check for World
def test3(text):
    return bool(re.search(r"World", text))

# Check for ! 
def test4(text):
    return bool(re.search(r"!", text))

# Check for no endline at the end
def test5(text):
    return not bool(re.search(r"\n", text))

# Check for no other text
def test6(text):
    return bool(re.search(r"\AHello World!\Z", text))

driver.set_directory(os.path.realpath(__file__))
driver.compile(sys.argv[1])
try:
    # Test
    output_text = driver.run_program("./main"+sys.argv[1]+".exe",sys.argv[1])
except:
    sys.exit(1)

# Delete input file
subprocess.call("make clean NUM="+sys.argv[1])

# Output results
test_outcome = [test1(output_text), test2(output_text), test3(output_text), test4(output_text), test5(output_text), test6(output_text)]

driver.print_results(test_outcome, sys.argv[1])

sys.exit(0)