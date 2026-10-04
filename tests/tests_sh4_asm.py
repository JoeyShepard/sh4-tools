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


#Exported to test runner
test_list=[
    test_inputs,
    test_text_to_tokens,
    test_tokens,
    #test_instructions,
    ]

