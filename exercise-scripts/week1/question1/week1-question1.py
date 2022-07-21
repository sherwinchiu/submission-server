#!/usr/bin/env python
# -*- coding: utf-8 -*-

# week1-question1.py
# Hello World! 
# Week 1, Question 1

import subprocess
import re
import os, sys

def initialize():
    # Change directory to working directory
    current_directory = os.path.dirname(os.path.realpath(__file__))
    os.chdir(current_directory)

    # Compile input file
    try:
        subprocess.run("ren *.cpp answer.cpp".split(), shell=True)
        error_message = subprocess.run("make", stderr=subprocess.PIPE).stderr.decode("utf-8").split('make:')[0]
        if(re.search(r"error:", error_message)):
            print("There was in error in your code! Your error: ")
            print(error_message)
            print("Try fixing this error and resubmitting!")
            sys.exit(1)
    except Exception as e:
        print(e)
    
def run_program():
    out = subprocess.Popen("./main.exe", stdout=subprocess.PIPE)
    try:
        out.communicate(timeout=2)
    except:
        out.kill()
        print("Timeout")
        subprocess.call('make clean')
        sys.exit(1)
    out = out.communicate()[0].decode("utf-8") 
    return out

def print_results(test_outcome):
    test_num = len(test_outcome)
    for i in range(test_num):
        if(test_outcome[i]):
            print("Pass")
        else:
            print("Fail")
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

initialize()

# Test
output_text = run_program()
# Delete input file
subprocess.call("make clean")

test_outcome = [test1(output_text), test2(output_text), test3(output_text), test4(output_text), test5(output_text), test6(output_text)]

print_results(test_outcome)

sys.exit(0)