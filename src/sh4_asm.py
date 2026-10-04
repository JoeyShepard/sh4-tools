#!/usr/bin/env python3

from src.sh4_instructions import *
from src.sh4_common import *

#Import instruction information
load_instructions()

class AsmError(Exception):
    pass

def assemble(text):
    #Loop through lines of text
    lines=[]
    textlines=text.splitlines()
    for textline in textlines:
        line=LineClass()
        line.text=textline
        line.source="asm"

        #Generate tokens, IR, and opcode
        line.text_to_tokens()
        line.tokens_to_IR()
        line.IR_to_opcode()
        
        #TODO: find .org etc
        #TODO: handle labels

        #Add finished line to output
        lines+=[line]

    #Done - return assembled instructions
    return lines

