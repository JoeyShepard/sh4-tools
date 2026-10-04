#!/usr/bin/env python3

from pathlib import Path
import inspect
from color import *

def line_num():
    return inspect.currentframe().f_back.f_back.f_lineno

def check(a,b):
    assert a==b,(f"Found {a} but expected {b}",line_num())

def check_eq(a,b):
    assert a==b,(f"Found {a} but expected {b}",line_num())

def check_ne(a,b):
    assert a!=b,(f"Expected {a}!={b} but equal",line_num())

def check_not_reached(a=None):
    if a==None:
        msg=""
    else:
        msg=f" ({a})"
    assert 1==0,(f"Reached line unexpectedly{msg}",line_num())


PREFIX="- "
COL_SIZES=[20,10]

def do_tests(test_name,test_list):
    output=test_name.ljust(COL_SIZES[0])
    output+=f"{len(test_list)} tests".ljust(COL_SIZES[1])
    test_count=1
    for test in test_list:
        try:
            test()
        except AssertionError as e:
            msg,line=e.args[0]
            print(output)
            print(f"{PREFIX}{msg}")
            printc(f"{PREFIX}FAILED: {test.__name__}() - line {line} of {Path(inspect.getfile(test)).name} \n","red")
            exit(1)
        test_count+=1
    print(output,end="")
    printc("PASS\n","green")
