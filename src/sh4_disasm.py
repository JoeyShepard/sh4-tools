#!/usr/bin/env python3

from src.sh4_instructions import *
from src.sh4_common import *

#Import instruction information
load_instructions()

class DisasmError(Exception):
    pass

def disassemble(data,address=0):
    try:
        #Convert input to bytes if it's something else like list or tuple
        data=bytes(data)
    except:
        #Could not convert to bytes
        raise DisasmError("Could not convert disasm input to bytes") from None
        
    #Must be even number of bytes
    if len(data)%2==1:
        raise DisasmError("Disasm input must be even number of bytes") from None

    #Address must by aligned by 2 bytes
    if address%2==1:
        raise DisasmError("Disasm starting address must be even") from None

    #Loop through instructions
    lines=[]
    for i in range(0,len(data),2):
        line=LineClass()
        line.opcode=(data[i]<<8)|data[i+1]
        line.address=address
        line.source="disasm"
        
        #Generate IR, tokens, and text
        line.verify_opcode()
        line.opcode_to_IR()
        line.IR_to_tokens()
        line.tokens_to_text()

        #Add finished line to output
        lines+=[line]

        #Increment address by size of instruction
        address+=2

    #Done - return disassembled instructions
    return lines
