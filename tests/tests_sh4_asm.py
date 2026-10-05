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

#TODO: test alternate instructions like FMOV.S and CMP/EQ

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
        line_disasm.tokens_to_text()

        #Convert assembly text to tokens and check
        line_asm=LineClass()
        line_asm.text=text
        line_asm.text_to_tokens()
        check(line_asm.tokens,line_disasm.tokens)

        #Create IR from tokens and check
        line_asm.tokens_to_IR()

        #TODO: remove
        print(f"{hex16(opcode)[2:]} disasm: {line_disasm.show_IR()}")
        print(f"{hex16(opcode)[2:]}    asm: {line_asm.show_IR()}")
        print()
        #input()

        check_true(line_asm.IR_equal(line_disasm))

#Exported to test runner
test_list=[
    test_inputs,
    test_text_to_tokens,
    test_instructions,
    #test_instructions,
    ]

