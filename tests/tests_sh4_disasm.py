#!/usr/bin/env python3

from tests.tests_util import *
from tests.test_sh4_disasm_instructions import *
from src.sh4_disasm import *

def test_inputs():
    #Catch invalid inputs
    invalid_inputs=[
        (1,2,300,4),
        [1,2,300,4],
        ("Hi","Hello"),
        ]

    for i in invalid_inputs:
        reached=False
        try:
            disassemble(i)
            reached=True
        except DisasmError:
            pass
        if reached==True:
            check_not_reached(i)

    #Catch odd number of bytes
    reached=False
    try:
        disassemble([1,2,3])
        reached=True
    except DisasmError:
        pass
    if reached==True:
        check_not_reached()

    #Catch starting on odd address
    reached=False
    try:
        disassemble([1,2,3,4],address=1)
        reached=True
    except DisasmError:
        pass
    if reached==True:
        check_not_reached()

    #Allow starting on even address
    reached=False
    try:
        disassemble([1,2,3,4],address=0x100)
    except DisasmError as e:
        reached=True
    if reached==True:
        check_not_reached()

import time

def test_automated():
    #Read in objdump results for comparison
    objdump_lines=[]
    with open("tests/gnu-as-comparison/objdump-result.txt") as f:
        for i,line in enumerate(f.readlines()):
            if i>6:
                fields=line.split("\t")
                address=fields[0].replace(" ","").replace(":","").upper()
                opcode=fields[1].replace(" ","").upper()
                instruction=fields[2].replace("\n","").upper()
                if len(fields)>3:
                    operands=fields[3].replace("\n","").upper()
                else:
                    operands=""
                if operands!="":
                    operands=" "+operands
                
                line_output=f"{('00000000'+address)[-8:]}:\t{opcode}\t{instruction}{operands}"
                line_output=line_output.replace(".WORD",".word")
                line_output=line_output.replace("0X","0x")
                objdump_lines+=[line_output]
    

    #Generate all 2^16 possible instructions
    data=[]
    for i in range(2**16):
        data+=[i>>8,i&0xFF]
    data=bytes(data)

    start=time.perf_counter()
    
    #TODO: faster now but still 0.75s
    lines=disassemble(data)

    end=time.perf_counter()
    print(end-start)

    with open("tests/gnu-as-comparison/test-output.txt","wt") as f:
        for i,line in enumerate(lines):
            #Write result to output file
            line_text=f"{hex32(line.address)[2:]}:\t{hex16(line.opcode)[2:]}\t{line.text}"
            f.write(line_text+"\n")

            #Compare result to objdump
            if objdump_lines[i]!=line_text:
                check_eq(objdump_lines[i],line_text)

#Exported to test runner
test_list=[
    test_inputs,
    #Manually testing instructions - replaced by test_automated
    #test_instructions,
    test_automated,
    ]

