#!/usr/bin/env python
# -*- coding: utf-8 -*-

# week2-question3
# Grade Schema
# Week 2, Question 3

import subprocess
import re
import os, sys
import random

sys.path.append(os.path.join(os.path.dirname(__file__),'../../'))

import driver

# Custom Tests
def test1():
    test1_text = driver.run_input_program("./main"+sys.argv[1]+".exe",sys.argv[1], "90")
    return re.search(r"Congrats\s*on\s*getting\s*an\s*A", test1_text, re.I)  

def test2():
    test2_text = driver.run_input_program("./main"+sys.argv[1]+".exe",sys.argv[1], "70")
    return re.search(r"Good\s*job\s*on\s*getting\s*a\s*B", test2_text, re.I)

def test3():
    test3_text = driver.run_input_program("./main"+sys.argv[1]+".exe",sys.argv[1], "68")
    return re.search(r"You\s*got\s*a\s*C", test3_text, re.I)

def test4():
    test4_text = driver.run_input_program("./main"+sys.argv[1]+".exe",sys.argv[1], "58")
    return re.search(r"You\s*got\s*a\s*D", test4_text, re.I)

def test5():
    test5_text = driver.run_input_program("./main"+sys.argv[1]+".exe",sys.argv[1], "40")
    return re.search(r"Unfortunately\s*,\s*you\s*got\s*a\s*F", test5_text, re.I)

def test6():
    result_count = 0
    for i in range(100):
        rand_num = random.uniform(0, 100)
        test6_text = driver.run_input_program("./main"+sys.argv[1]+".exe",sys.argv[1], str(rand_num))
        print(test6_text)
        if(rand_num >= 80):
            if(re.search(r"Congrats\s*on\s*getting\s*an\s*A", test6_text, re.I)):
                result_count += 1
        elif(rand_num >= 70):
            if(re.search(r"Good\s*job\s*on\s*getting\s*a\s*B", test6_text, re.I)):
                result_count += 1
        elif(rand_num >= 60):
            if(re.search(r"You\s*got\s*a\s*C", test6_text, re.I)):
                result_count += 1
        elif(rand_num >= 50):
            if(re.search(r"You\s*got\s*a\s*D", test6_text, re.I)):
               result_count += 1 
        else:
            if(re.search(r"Unfortunately\s*,\s*you\s*got\s*a\s*F", test6_text, re.I)):
                result_count += 1
    if (result_count > 95):
        return True
    return False

driver.set_directory(os.path.realpath(__file__))
driver.compile(sys.argv[1])
try:
    file_text = open("answer"+sys.argv[1]+".cpp", "r").read()  
    test_outcome = [test1(), test2(), test3(), test4(), test5(), test6()]  
except:
    subprocess.call("make clean NUM="+sys.argv[1])
    sys.exit(1)
# Output results

# Delete input file
subprocess.call("make clean NUM="+sys.argv[1])

driver.print_results(test_outcome, sys.argv[1])

sys.exit(0)