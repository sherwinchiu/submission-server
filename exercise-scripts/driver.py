import subprocess
import re
import os, sys
import time
import inspect

def set_directory(directory):
    current_directory = os.path.dirname(directory)
    os.chdir(current_directory)

def compile(file_num):
    # Compile input file
    try:
        error_message = subprocess.run("make compile NUM="+file_num, stderr=subprocess.PIPE).stderr.decode("utf-8").split('make:')[0]
        if(re.search(r"error:", error_message)):
            print("Found an error while trying to compile your code! Your error: ")
            print(error_message)
            print("Try fixing this error and resubmitting!")
            subprocess.call('make clean NUM='+file_num)
            sys.exit(1)
    except Exception as e:
        print(e)
    
def run_program(program_name, file_num):
    init_time = time.perf_counter()
    out = subprocess.Popen(program_name, stdout=subprocess.PIPE)
    print(time.perf_counter()-init_time)
    try:
        out.communicate(timeout=2)
    except:
        out.kill()
        print("Timeout")
        subprocess.call('make clean NUM='+file_num)
        sys.exit(1)
    out = out.communicate()[0].decode("utf-8") 
    return out

def print_results(test_outcome, file_num):
    print(inspect.stack()[1].filename)
    print(file_num)  
    test_num = len(test_outcome)
    for i in range(test_num):
        if(test_outcome[i]):
            print("Pass")
        else:
            print("Fail")

def __init__():
    pass