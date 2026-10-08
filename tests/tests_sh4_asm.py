#!/usr/bin/env python3

from tests.tests_util import *
from tests.test_sh4_asm_instructions import *
from src.sh4_asm import *

def test_inputs():
    pass

def test_text_to_tokens():
    #Check minus sign handled correctly
    test_list=(
        ("mov 42",(("instruction","mov"),(" "," "),("num","42"))),
        ("mov     42",(("instruction","mov"),(" ","     "),("num","42"))),
        ("mov -42",(("instruction","mov"),(" "," "),("num","-42"))),
        ("mov -    42",(("instruction","mov"),(" "," "),(" ","    "),("num","-42"))),
        ("mov  -   42",(("instruction","mov"),(" ","  "),(" ","   "),("num","-42"))),
        ("mov   -  42",(("instruction","mov"),(" ","   "),(" ","  "),("num","-42"))),
        ("mov    - 42",(("instruction","mov"),(" ","    "),(" "," "),("num","-42"))),
        ("mov     -42",(("instruction","mov"),(" ","     "),("num","-42"))),

        ("mov 0x42",(("instruction","mov"),(" "," "),("hex","0x42"))),
        ("mov     0x42",(("instruction","mov"),(" ","     "),("hex","0x42"))),
        ("mov -0x42",(("instruction","mov"),(" "," "),("hex","-0x42"))),
        ("mov -    0x42",(("instruction","mov"),(" "," "),(" ","    "),("hex","-0x42"))),
        ("mov  -   0x42",(("instruction","mov"),(" ","  "),(" ","   "),("hex","-0x42"))),
        ("mov   -  0x42",(("instruction","mov"),(" ","   "),(" ","  "),("hex","-0x42"))),
        ("mov    - 0x42",(("instruction","mov"),(" ","    "),(" "," "),("hex","-0x42"))),
        ("mov     -0x42",(("instruction","mov"),(" ","     "),("hex","-0x42"))),

        ("mov R0",(("instruction","mov"),(" "," "),("reg","R0"))),
        ("mov -R0",(("instruction","mov"),(" "," "),("-","-"),("reg","R0"))),
        ("mov - R0",(("instruction","mov"),(" "," "),("-","-"),(" "," "),("reg","R0"))),
        ("mov R0-",(("instruction","mov"),(" "," "),("reg","R0"),("-","-"))),
        ("mov R0 -",(("instruction","mov"),(" "," "),("reg","R0"),(" "," "),("-","-"))),
    )
    for test in test_list:
        #Test text
        text,tokens=test
        test_line=LineClass()
        test_line.text=text
        test_line.text_to_tokens()

        #Expected tokens
        expected=[]
        for token in tokens:
            token_type,value=token
            expected+=[TokenClass(token_type,value)]

        #Check if matches
        check(test_line.tokens,expected)

#Convert instruction text to tokens, IR, and opcode and compare to expected
def test_instructions():
    for test in instruction_test_list:
        opcode,text=test

        #Create IR, tokens, and text from opcode to compare to assembly
        line_disasm=LineClass()
        line_disasm.opcode=opcode
        line_disasm.address=opcode*2
        line_disasm.verify_opcode()
        line_disasm.opcode_to_IR()
        line_disasm.IR_to_tokens()

        #Convert assembly text to tokens
        line_asm=LineClass()
        line_asm.text=text
        line_asm.text_to_tokens()

        #Check tokens
        check_true(line_asm.valid_tokens)
        check(line_asm.tokens,line_disasm.tokens)

        #Create IR from tokens
        line_asm.tokens_to_IR()

        #Check IR
        check_true(line_asm.IR_equal(line_disasm))

        #Make sure lowercase token names also work
        new_tokens=[]
        for token in line_asm.tokens:
            token.value=token.value.lower()
            new_tokens+=[token]
        line_asm.tokens=new_tokens

        #Create IR from lowercase tokens
        line_asm.tokens_to_IR()

        #Check IR
        check_true(line_asm.IR_equal(line_disasm))

        #print(f"{hex16(opcode)[2:]} disasm: {line_disasm.show_IR()}")
        #print(f"{hex16(opcode)[2:]}    asm: {line_asm.show_IR()}")
        #print(line_asm.valid_opcode)
        #print()

        #Create opcode
        if line_disasm.valid_opcode==True:
            line_asm.address=opcode*2
            line_asm.IR_to_opcode()

            print(f"expected:  {hex16(opcode)[2:]} from ({line_asm.show_IR()})")
            print(f"generated: {None if line_asm.opcode==None else hex16(line_asm.opcode)[2:]} ")
            print()
            
            #Check opcode
            check_true(line_asm.valid_opcode)
            check(line_asm.opcode,opcode)




#Exported to test runner
test_list=[
    test_inputs,
    test_text_to_tokens,
    test_instructions,

    #Need to finish assembly first
    #test_instructions_alt,
    ]

