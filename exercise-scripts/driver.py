import subprocess
import re
import os, sys
import time
import inspect

def set_directory(directory):
    current_directory = os.path.dirname(directory)
    os.chdir(current_directory)

def compile(file_num):
    print(file_num)  
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

def add_header_guards(file_num):
    file = open("answer"+file_num+".cpp", "r")
    file_text = file.read()
    file_text = file_text.split("\n")
    main_found = False
    i = 0
    para_count = 1
    
    while(not main_found):
        if(re.match(r"int\s+main\s*\(\s*\)\s*{", file_text[i])):
            file_text.insert(i, "#include \"driver.cpp\"")
            i += 1
            file_text.insert(i, "#ifndef TESTING")
            main_found = True
        i += 1 
    while(para_count != 0):
        if(re.match(r"{", file_text[i])):
            para_count += 1
        elif(re.match(r"}", file_text[i])):
            para_count -= 1
        i += 1 
   
    file_text.insert(i, "#endif")
    file_text = "\n".join(file_text)
    file = open("answer"+file_num+".cpp", "w")
    file.write(file_text)
    file.close()
    return file_text

def check_includes(file_text, do_not_include):
    text = file_text.split("\n")
    include_text = []
    result = True
    for i in range(len(text)):
        if(re.match(r"#include", text[i])):
            include_text.append(text[i])
    for i in range(len(include_text)):
        for j in range(len(do_not_include)):
            if(re.match(r"#include\s+<\s*"+do_not_include[j]+r"\s*>", include_text[i])):
                result = False
    return result

def run_program(program_name, file_num):
    init_time = time.perf_counter()
    out = subprocess.Popen(program_name, stdout=subprocess.PIPE)
    try:
        out.communicate(timeout=2)
        print(time.perf_counter()-init_time)
    except:
        out.kill()
        print("Timeout")
        subprocess.call('make clean NUM='+file_num)
        sys.exit(1)
    out = out.communicate()[0].decode("utf-8") 
    return out

def run_input_program(program_name, file_num, inputs):
    init_time = time.perf_counter()
    out = subprocess.Popen(program_name, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
    try:
        new_out = out.communicate(input=inputs.encode(), timeout=2)[0].decode("utf-8")
        new_out = re.findall(r"-?[0-9]+\.?[0-9]*", new_out)[0]
        print(time.perf_counter()-init_time)
    except:
        out.kill()
        print("Timeout")
        subprocess.call('make clean NUM='+file_num)
        sys.exit(1)
    return new_out

def run_function_program(program_name, file_num):
    init_time = time.perf_counter()
    out = subprocess.Popen(program_name, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
    try:
        out.communicate(timeout=2)
        print(time.perf_counter()-init_time)
    except:
        out.kill()
        print("Timeout")
        subprocess.call('make clean NUM='+file_num)
        sys.exit(1)
    out = out.communicate()[0].decode("utf-8") 
    return out

def print_results(test_outcome, file_num):
    num_files = len(inspect.stack()[1].filename.split("\\"))-1
    print(inspect.stack()[1].filename.split("\\")[num_files])
    test_num = len(test_outcome)
    for i in range(test_num):
        if(test_outcome[i]):
            print("Pass")
        else:
            print("Fail")

def __init__():
    pass