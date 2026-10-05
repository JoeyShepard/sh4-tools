from src.sh4_instructions import *

def hex16(num):
    return "0x"+("0000"+hex(num).upper()[2:])[-4:]

def hex32(num):
    return "0x"+("00000000"+hex(num).upper()[2:])[-8:]

class OperandClass:
    def __init__(self):
        self.type=None
        self.values=[None]

    def __eq__(self,other):
        def guard(val):
            if type(val)==str:
                return val.upper()
            else:
                return None
        if len(self.values)!=len(other.values):
            return False
        else:
            r1=(guard(self.type)==guard(other.type))
            r2=(guard(self.values[0])==guard(other.values[0]))
            if len(self.values)==1:
                return r1 and r2
            else:
                return r1 and r2 and (guard(self.values[1])==guard(other.values[1]))

    def __repr__(self):
        return f"({self.type}, {self.values})"

class TokenClass:
    def __init__(self,token_type=None,value=None):
        self.type=token_type
        self.value=value

    def __repr__(self):
        return f'TokenClass("{self.type}","{self.value}")'

    def __eq__(self,other):
        return self.type==other.type and self.value==other.value

    def __hash__(self):
        return hash((self.type,self.value))

class LineClass:
    def __init__(self):
        #Source - disassembler, assembler, etc
        self.source=None

        #Opcode
        self.opcode=None
        self.address=None
        self.group=None
        self.mask_raw=None
        self.mask=None
        self.id=None
        self.operand_masks={}
        self.valid_opcode=False

        #IR
        self.key=None
        self.inst=None
        self.src=OperandClass()
        self.dest=OperandClass()
        self.valid_IR=False

        #Tokens
        self.tokens=[]
        self.valid_tokens=False

        #Text
        self.text=None

    #Extract value from opcode given mask letter(d, n, m, or i)
    def __extract(self,letter):
        start,_,mask=self.operand_masks[letter]
        return (self.opcode&mask)>>start

    def IR_equal(self,other):
        def guard(val):
            if type(val)==str:
                return val.upper()
            else:
                return None
        return guard(self.inst)==guard(other.inst) and \
            self.src==other.src and \
            self.dest==other.dest

    def show_IR(self):
        return f"{self.inst} {self.src}, {self.dest}"

    def tokens_no_spaces(self):
        return tuple([token for token in self.tokens if token.type!=" "])

    def verify_opcode(self):
        if self.opcode not in opcode_lookup:
            #No match found
            self.valid_opcode=False
        else:
            #Match found
            match=opcode_lookup[self.opcode]
            self.key=match.key
            self.mask_raw=match.mask_raw
            self.mask=match.mask
            self.id=match.id
            self.operand_masks=match.operand_masks
            self.valid_opcode=True

    #Generate IR from opcode
    def opcode_to_IR(self):
        if self.valid_opcode==False:
            #Invalid opcode - no IR to generate
            self.valid_IR=False
        else:
            #Valid opcode - generate IR

            #Extract operands from opcode
            self.inst=self.key[0]
            if self.key[1]!="":
                self.src.type=self.key[1]
            if self.key[2]!="":
                self.dest.type=self.key[2]

            #Loop through src and dest
            for i in range(2):
                src=(i==0)
                dest=(i==1)
                arg_type=[self.src.type,self.dest.type][i]
                
                #Adjust operand types according to data width
                    #ie REG_IND becomes REG_IND_L, REG_IND_W, or REG_IND_B
                if arg_type in ["REG_IND_DISP","GBR_IND_DISP","PC_REL_DISP","PC_REL_ABS"]:
                    if self.inst in ["MOV.L","MOVA"]:
                        arg_type+="_L"
                    elif self.inst in ["MOV.W"]:
                        arg_type+="_W"
                    elif self.inst in ["MOV.B"]:
                        arg_type+="_B"

                    if src==True:
                        self.src.type=arg_type
                    elif dest==True:
                        self.dest.type=arg_type

                #Adjust for Rm or Rn
                if src==True:
                    reg_letter="m"
                elif dest==True:
                    reg_letter="n"

                #Extract operands
                new_values=[]
                if arg_type=="IMM8_SIGNED":
                    val=self.__extract("i")
                    if val>=0x80:
                        #Convert to signed
                        val=-(0x100-val)
                    new_values+=[val]
                elif arg_type=="IMM8_UNSIGNED":
                    val=self.__extract("i")
                    new_values+=[val]
                elif arg_type in ["REG_R0","REG_GBR","REG_MACH","REG_MACL","REG_PR","REG_SR","REG_VBR","REG_SSR",
                                    "REG_SPC","REG_SGR","REG_DBR","REG_FPUL","REG_FPSCR","REG_XMTRX"]:
                    #No values to set
                    pass
                elif arg_type in ["REG_DIR","REG_IND","REG_IND_PRE","REG_IND_POST","IND_REG_IND",
                                    "FREG_DIR","FREG_FR0_DIR"]:
                    reg=self.__extract(reg_letter)
                    new_values+=[reg]
                elif arg_type=="DREG_DIR":
                    reg=self.__extract(reg_letter)*2
                    new_values+=[reg]
                elif arg_type=="XREG_DIR":
                    reg=self.__extract(reg_letter)*2-1
                    new_values+=[reg]
                elif arg_type=="FVREG_DIR":
                    reg=self.__extract(reg_letter)*4
                    new_values+=[reg]
                elif arg_type=="PC_REL_ABS_L":
                    disp=self.__extract("d")*4+4+self.address-self.address%4
                    new_values+=[disp]
                elif arg_type=="PC_REL_DISP_L":
                    #Confirmed working but disassembler finds PC_REL_ABS_L first
                    disp=self.__extract("d")*4+4
                    disp-=self.address%4 
                    new_values+=[disp]
                elif arg_type=="PC_REL_ABS_W":
                    disp=self.__extract("d")*2+4+self.address
                    new_values+=[disp]
                elif arg_type=="PC_REL_DISP_W":
                    #Confirmed working but disassembler finds PC_REL_ABS_W first
                    disp=self.__extract("d")*2+4
                    new_values+=[disp]
                elif arg_type=="REG_IND_DISP_L":
                    disp=self.__extract("d")*4
                    new_values+=[disp]
                    reg=self.__extract(reg_letter)
                    new_values+=[reg]
                elif arg_type=="REG_IND_DISP_W":
                    disp=self.__extract("d")*2
                    new_values+=[disp]
                    reg=self.__extract(reg_letter)
                    new_values+=[reg]
                elif arg_type=="REG_IND_DISP_B":
                    disp=self.__extract("d")
                    new_values+=[disp]
                    reg=self.__extract(reg_letter)
                    new_values+=[reg]
                elif arg_type=="GBR_IND_DISP_L":
                    disp=self.__extract("d")*4
                    new_values+=[disp]
                elif arg_type=="GBR_IND_DISP_W":
                    disp=self.__extract("d")*2
                    new_values+=[disp]
                elif arg_type=="GBR_IND_DISP_B":
                    disp=self.__extract("d")
                    new_values+=[disp]
                elif arg_type=="IND_GBR_IND":
                    #No values to set for @(R0,GBR)
                    pass
                elif arg_type=="PC_REL_8":
                    disp=self.__extract("d")
                    if disp>=0x80:
                        #Convert to signed
                        disp=-(0x100-disp)
                    disp=self.address+disp*2+4
                    if disp<0:
                        disp+=0x100000000
                    new_values+=[disp]
                elif arg_type=="PC_REL_12":
                    disp=self.__extract("d")
                    if disp>=0x800:
                        #Convert to signed
                        disp=-(0x1000-disp)
                    disp=self.address+disp*2+4
                    if disp<0:
                        disp+=0x100000000
                    new_values+=[disp]
                elif arg_type=="REG_BANK":
                    reg=self.__extract(reg_letter)
                    new_values+=[reg]
                    
                if new_values!=[]:
                    if src==True:
                        self.src.values=new_values[:]
                    elif dest==True:
                        self.dest.values=new_values[:]

            #Mark IR as valid
            self.valid_IR=True

    #Generate tokens from IR
    def IR_to_tokens(self):
        if self.valid_IR==False:
            #Unrecognized opcode - display as .word
            self.tokens=[]
            self.tokens+=[TokenClass("directive",".word")]
            self.tokens+=[TokenClass(" "," ")]
            self.tokens+=[TokenClass("hex",hex16(self.opcode))]
        else:
            #Recognized opcode - create tokens
            self.tokens=[]
            self.tokens+=[TokenClass("instruction",self.inst)]

            space_added=False
            last_added=False
            for i in range(2):
                new_tokens=[]
                if i==0:
                    arg_type=self.src.type
                    arg_values=self.src.values
                elif i==1:
                    arg_type=self.dest.type
                    arg_values=self.dest.values

                if arg_type=="IMM8_SIGNED":
                    new_tokens+=[TokenClass("#","#")]
                    new_tokens+=[TokenClass("num",str(arg_values[0]))]
                elif arg_type=="IMM8_UNSIGNED":
                    new_tokens+=[TokenClass("#","#")]
                    new_tokens+=[TokenClass("num",str(arg_values[0]))]
                elif arg_type=="REG_R0":
                    new_tokens+=[TokenClass("reg","R0")]

                elif arg_type in ["REG_GBR","REG_MACH","REG_MACL","REG_PR","REG_SR","REG_VBR","REG_SSR",
                                    "REG_SPC","REG_SGR","REG_DBR","REG_FPUL","REG_FPSCR","REG_XMTRX"]:
                    #Load reg name from modes look up
                    new_tokens+=[TokenClass("reg_special",modes[arg_type][0])]
                elif arg_type=="REG_DIR":
                    new_tokens+=[TokenClass("reg","R"+str(arg_values[0]))]
                elif arg_type=="REG_IND":
                    new_tokens+=[TokenClass("@","@")]
                    new_tokens+=[TokenClass("reg","R"+str(arg_values[0]))]
                elif arg_type=="REG_IND_PRE":
                    new_tokens+=[TokenClass("@","@")]
                    new_tokens+=[TokenClass("-","-")]
                    new_tokens+=[TokenClass("reg","R"+str(arg_values[0]))]
                elif arg_type=="REG_IND_POST":
                    new_tokens+=[TokenClass("@","@")]
                    new_tokens+=[TokenClass("reg","R"+str(arg_values[0]))]
                    new_tokens+=[TokenClass("+","+")]
                elif arg_type=="IND_REG_IND":
                    new_tokens+=[TokenClass("@","@")]
                    new_tokens+=[TokenClass("(","(")]
                    new_tokens+=[TokenClass("reg","R0")]
                    new_tokens+=[TokenClass(",",",")]
                    new_tokens+=[TokenClass("reg","R"+str(arg_values[0]))]
                    new_tokens+=[TokenClass(")",")")]
                elif arg_type in ["PC_REL_ABS_L","PC_REL_ABS_W"]:
                    new_tokens+=[TokenClass("hex","0x"+(hex(arg_values[0]).upper())[2:])]
                elif arg_type in ["PC_REL_DISP_L","PC_REL_DISP_W"]:
                    new_tokens+=[TokenClass("@","@")]
                    new_tokens+=[TokenClass("(","(")]
                    new_tokens+=[TokenClass("num",str(arg_values[0]))]
                    new_tokens+=[TokenClass(",",",")]
                    new_tokens+=[TokenClass("reg_special","PC")]
                    new_tokens+=[TokenClass(")",")")]
                elif arg_type in ["GBR_IND_DISP_L","GBR_IND_DISP_W","GBR_IND_DISP_B"]:
                    new_tokens+=[TokenClass("@","@")]
                    new_tokens+=[TokenClass("(","(")]
                    new_tokens+=[TokenClass("num",str(arg_values[0]))]
                    new_tokens+=[TokenClass(",",",")]
                    new_tokens+=[TokenClass("reg_special","GBR")]
                    new_tokens+=[TokenClass(")",")")]
                elif arg_type in ["REG_IND_DISP_L","REG_IND_DISP_W","REG_IND_DISP_B"]:
                    new_tokens+=[TokenClass("@","@")]
                    new_tokens+=[TokenClass("(","(")]
                    new_tokens+=[TokenClass("num",str(arg_values[0]))]
                    new_tokens+=[TokenClass(",",",")]
                    new_tokens+=[TokenClass("reg","R"+str(arg_values[1]))]
                    new_tokens+=[TokenClass(")",")")]
                elif arg_type=="IND_GBR_IND":
                    new_tokens+=[TokenClass("@","@")]
                    new_tokens+=[TokenClass("(","(")]
                    new_tokens+=[TokenClass("reg","R0")]
                    new_tokens+=[TokenClass(",",",")]
                    new_tokens+=[TokenClass("reg_special","GBR")]
                    new_tokens+=[TokenClass(")",")")]
                elif arg_type in ["PC_REL_8","PC_REL_12"]:
                    new_tokens+=[TokenClass("hex","0x"+(hex(arg_values[0]).upper())[2:])]
                elif arg_type=="REG_BANK":
                    new_tokens+=[TokenClass("reg_bank","R"+str(arg_values[0])+"_BANK")]
                elif arg_type=="FREG_DIR":
                    new_tokens+=[TokenClass("freg","FR"+str(arg_values[0]))]
                elif arg_type=="FREG_FR0_DIR":
                    new_tokens+=[TokenClass("freg","FR0")]
                    new_tokens+=[TokenClass(",",",")]
                    new_tokens+=[TokenClass("freg","FR"+str(arg_values[0]))]
                elif arg_type=="DREG_DIR":
                    new_tokens+=[TokenClass("dreg","DR"+str(arg_values[0]))]
                elif arg_type=="XREG_DIR":
                    new_tokens+=[TokenClass("xreg","XD"+str(arg_values[0]))]
                elif arg_type=="FVREG_DIR":
                    new_tokens+=[TokenClass("fvreg","FV"+str(arg_values[0]))]

                if new_tokens!=[]:
                    if space_added==False:
                        self.tokens+=[TokenClass(" "," ")]
                        space_added=True
                    if last_added==True:
                        self.tokens+=[TokenClass(",",",")]
                    self.tokens+=new_tokens
                    last_added=True

        self.valid_tokens=True

    #Generate text from tokens
    def tokens_to_text(self):
        if self.valid_tokens==False:
            #No valid tokens which only happens in disassembly if forgot to call IR_to_tokens
            self.text="#Unknown!"
        else:
            self.text=""
            last_type=None
            for token in self.tokens:
                self.text+=token.value

    def text_to_tokens(self):
        #Separate into tokens before classifying
        separators="@#(),-+ "
        tokens=[]
        current=""
        for c in self.text:
            if c in separators:
                if current!="":
                    tokens+=[current]
                    current=""
                if c==" " and len(tokens)>0 and tokens[-1]==len(tokens[-1])*" ":
                    tokens[-1]+=" " 
                else:
                    tokens+=[c]
            else:
                current+=c
        if current!="":
            tokens+=[current]

        #Token lists for classifying
        regs=["R0","R1","R2","R3","R4","R5","R6","R7","R8",
                "R9","R10","R11","R12","R13","R14","R15"]
        regs_special=["GBR","MACH","MACL","PR","SR","VBR","SSR",
                        "SPC","SGR","DBR","FPUL","FPSCR","XMTRX"]
        reg_banks=["R0_BANK","R1_BANK","R2_BANK","R3_BANK",
                "R4_BANK","R5_BANK","R6_BANK","R7_BANK"]
        fregs=["FR0","FR1","FR2","FR3","FR4","FR5","FR6","FR7","FR8",
                "FR9","FR10","FR11","FR12","FR13","FR14","FR15"]
        dregs=["DR0","DR2","DR4","DR6","DR8","DR10","DR12","DR14"]
        xregs=["XD0","XD2","XD4","XD6","XD8","XD10","XD12","XD14"]
        fvregs=["FV0","FV4","FV8","FV12"]
        directives=[".WORD"]
        instructions=["ADD","ADDC","ADDV","AND","AND.B","BF","BF.S","BF/S","BRA","BRAF",
                        "BSR","BSRF","BT","BT.S","BT/S","CLRMAC","CLRS","CLRT","CMP/EQ",
                        "CMP/GE","CMP/GT","CMP/HI","CMP/HS","CMP/PL","CMP/PZ","CMP/STR",
                        "DIV0S","DIV0U","DIV1","DMULS.L","DMULU.L","DT","EXTS.B","EXTS.W",
                        "EXTU.B","EXTU.W","FABS","FADD","FCMP/EQ","FCMP/GT","FCNVDS",
                        "FCNVSD","FDIV","FIPR","FLDI0","FLDI1","FLDS","FLOAT","FMAC",
                        "FMOV","FMOV.S","FMUL","FNEG","FPCHG","FRCHG","FSCA","FSCHG",
                        "FSQRT","FSRRA","FSTS","FSUB","FTRC","FTRV","ICBI","JMP","JSR",
                        "LDC","LDC.L","LDS","LDS.L","LDTLB","MAC.L","MAC.W","MOV","MOV.B",
                        "MOV.L","MOV.W","MOVA","MOVCA.L","MOVCO.L","MOVLI.L","MOVT",
                        "MOVUA.L","MUL.L","MULS.W","MULU.W","NEG","NEGC","NOP","NOT",
                        "OCBI","OCBP","OCBWB","OR","OR.B","PREF","PREFI","ROTCL","ROTCR",
                        "ROTL","ROTR","RTE","RTS","SETS","SETT","SHAD","SHAL","SHAR",
                        "SHLD","SHLL","SHLL16","SHLL2","SHLL8","SHLR","SHLR16","SHLR2",
                        "SHLR8","SLEEP","STC","STC.L","STS","STS.L","SUB","SUBC","SUBV",
                        "SWAP.B","SWAP.W","SYNCO","TAS.B","TRAPA","TST","TST.B","XOR",
                        "XOR.B","XTRCT"]

        #Classify all tokens
        last_minus_index=None
        for token in tokens:
            token_added=False
            if token==len(token)*" ":
                self.tokens+=[TokenClass(" ",token)]
            elif token in separators:
                self.tokens+=[TokenClass(token,token)]
                token_added=True
            elif token.upper() in regs:
                self.tokens+=[TokenClass("reg",token)]
                token_added=True
            elif token.upper() in regs_special:
                self.tokens+=[TokenClass("reg_special",token)]
                token_added=True
            elif token.upper() in reg_banks:
                self.tokens+=[TokenClass("reg_bank",token)]
                token_added=True
            elif token.upper() in fregs:
                self.tokens+=[TokenClass("freg",token)]
                token_added=True
            elif token.upper() in dregs:
                self.tokens+=[TokenClass("dreg",token)]
                token_added=True
            elif token.upper() in fvregs:
                self.tokens+=[TokenClass("fvreg",token)]
                token_added=True
            elif token.upper() in directives:
                self.tokens+=[TokenClass("directive",token)]
                token_added=True
            elif token.upper() in instructions:
                self.tokens+=[TokenClass("instruction",token)]
                token_added=True
            else:
                #Check if hex
                if len(token)>=3 and token[:2]=="0x":
                    for c in token[2:]:
                        if c.upper() not in "0123456789ABCDEF":
                            #Not hex
                            break
                    else:
                        self.tokens+=[TokenClass("hex",token)]
                        token_added=True

                #Check if number
                if token_added==False:
                    for c in token:
                        if c not in "0123456789":
                            #Not number
                            break
                    else:
                        self.tokens+=[TokenClass("num",token)]
                        token_added=True

                #Otherwise, mark as other
                if token_added==False:
                    self.tokens+=[TokenClass("other",token)]
                    token_added=True

            #Keep track of minus in case belongs to number
            if token_added==True:
                if self.tokens[-1]==TokenClass("-","-"):
                    #Just added a minus - record location
                    last_minus_index=len(self.tokens)-1
                elif self.tokens[-1].type in ("num","hex"):
                    #Add minus to number if exists
                    if last_minus_index!=None:
                        #Remove minus token
                        self.tokens=self.tokens[:last_minus_index]+self.tokens[last_minus_index+1:]
                        last_minus_index=None

                        #Add minus to last added value
                        self.tokens[-1].value="-"+self.tokens[-1].value
                elif self.tokens[-1].type!=" ":
                    #Mark that last token wasn't minus but ignore spaces
                    last_minus_index=None


    def tokens_to_IR(self):
        tokens=self.tokens_no_spaces()

        if tokens not in token_lookup:
            self.valid_IR=False
        else:
            self.opcode=token_lookup[tokens]
            self.verify_opcode()
            self.opcode_to_IR()

    def IR_to_opcode(self):
        return

def load_instructions():
    #Load instruction information
    for k,v in instructions_raw.items():
        instruction=InstructionClass(k,v)
        instructions[k]=instruction

        #Add to opcode lookup
        fields=extract_fields(instruction.mask_raw)
        if fields==[]:
            #No operands - add to opcode lookup
            opcode_lookup[instruction.id]=instruction
        else:
            #Add all variants of instruction to lookup
            field_count=len(fields)
            counters=[0]*field_count
            limits=[2**length for _,_,length in fields]
            offsets=[start for _,start,_ in fields]
            #Iterate through all possible operand values
            carry=0
            while carry==0:
                opcode=instruction.id
                carry=1
                #Generate opcode
                for i in range(field_count):
                    opcode|=counters[i]<<offsets[i]
                    if opcode not in opcode_lookup:
                        #Only add to lookup if doesn't exist yet. Some instructions have multiple
                            #representations but first one is preferred (ie FMOV vs FMOV.S).
                        opcode_lookup[opcode]=instruction
                    #Propagate carry through permutation counters
                    if carry==1:
                        counters[i]+=1
                        if counters[i]==limits[i]:
                            counters[i]=0
                            carry=1
                        else:
                            carry=0

    #Load token lookup
    for i in range(2**16):
        line=LineClass()
        line.opcode=i
        #Address not used for lookup but need to set to something
        line.address=i*2
        line.verify_opcode()
        line.opcode_to_IR()
        line.IR_to_tokens()

        #TODO: don't add if argument depends on address
        if line.valid_opcode:
            token_lookup[line.tokens_no_spaces()]=i

