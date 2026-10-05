.text

    #mov #42,R0

    #mov.l foo1,R0
    #.align 2
    #foo1: .long 0x12345678

    #mov.l @(4,PC),R0
    #.align 2
    #.long 0x12345678

    #.short 0x1234
    #.short 0x5678

    #MOV.W @(4,PC),R0
    #MOV.W @(4,PC),R3
    #MOV.W @(8,PC),R7
    #MOV.W @(14,PC),R9
    #MOV.W @(256,PC),R12
    #MOV.W @(514,PC),R15

    #MOV.L @(4,PC),R0
    #MOV.L @(6,PC),R3
    #MOV.L @(8,PC),R7
    #MOV.L @(14,PC),R9
    #MOV.L @(256,PC),R12
    #MOV.L @(1022,PC),R15

    #MOV R0,R1
    #MOV R2,R3
    #MOV R4,R5
    #MOV R6,R7
    #MOV R8,R9
    #MOV R10,R11
    #MOV R12,R13
    #MOV R14,R15

    #MOV.B R0,@R2
    #MOV.B R3,@R5
    #MOV.B R6,@R8
    #MOV.B R9,@R12

    #MOV.W R0,@R2
    #MOV.W R3,@R5
    #MOV.W R6,@R8
    #MOV.W R9,@R12

    #MOV.L R0,@R2
    #MOV.L R3,@R5
    #MOV.L R6,@R8
    #MOV.L R9,@R12


    #MOV.B @R0,R2
    #MOV.B @R3,R5
    #MOV.B @R6,R8
    #MOV.B @R9,R12

    #MOV.W @R0,R2
    #MOV.W @R3,R5
    #MOV.W @R6,R8
    #MOV.W @R9,R12

    #MOV.L @R0,R2
    #MOV.L @R3,R5
    #MOV.L @R6,R8
    #MOV.L @R9,R12
    
    #MOV.B R0,@-R2
    #MOV.B R3,@-R5
    #MOV.B R6,@-R8
    #MOV.B R9,@-R12

    #MOV.W R0,@-R2
    #MOV.W R3,@-R5
    #MOV.W R6,@-R8
    #MOV.W R9,@-R12

    #MOV.L R0,@-R2
    #MOV.L R3,@-R5
    #MOV.L R6,@-R8
    #MOV.L R9,@-R12

    #MOV.B @R0+,R2
    #MOV.B @R3+,R5
    #MOV.B @R6+,R8
    #MOV.B @R9+,R12

    #MOV.W @R0+,R2
    #MOV.W @R3+,R5
    #MOV.W @R6+,R8
    #MOV.W @R9+,R12

    #MOV.L @R0+,R2
    #MOV.L @R3+,R5
    #MOV.L @R6+,R8
    #MOV.L @R9+,R12

    #MOV.B R0,@(0,R2)
    #MOV.B R0,@(5,R4)
    #MOV.B R0,@(10,R6)
    #MOV.B R0,@(15,R8)

    #MOV.W R0,@(0,R2)
    #MOV.W R0,@(10,R4)
    #MOV.W R0,@(20,R6)
    #MOV.W R0,@(30,R8)

    #MOV.L R0,@(0,R1)
    #MOV.L R3,@(4,R4)
    #MOV.L R8,@(32,R9)
    #MOV.L R11,@(48,R12)
    #MOV.L R14,@(60,R15)

    #MOV.B @(0,R1),R0
    #MOV.B @(4,R2),R0
    #MOV.B @(8,R4),R0
    #MOV.B @(15,R6),R0

    #MOV.W @(0,R1),R0
    #MOV.W @(10,R2),R0
    #MOV.W @(20,R4),R0
    #MOV.W @(30,R6),R0

    #MOV.L @(0,R1),R4
    #MOV.L @(32,R2),R5
    #MOV.L @(60,R3),R6

    #MOV.B R1,@(R0,R4)
    #MOV.B R2,@(R0,R5)
    #MOV.B R3,@(R0,R6)

    #MOV.W R1,@(R0,R4)
    #MOV.W R2,@(R0,R5)
    #MOV.W R3,@(R0,R6)

    #MOV.L R1,@(R0,R4)
    #MOV.L R2,@(R0,R5)
    #MOV.L R3,@(R0,R6)

    #MOV.B @(R0,R4),R1
    #MOV.B @(R0,R5),R2
    #MOV.B @(R0,R6),R3

    #MOV.W @(R0,R4),R1
    #MOV.W @(R0,R5),R2
    #MOV.W @(R0,R6),R3

    #MOV.L @(R0,R4),R1
    #MOV.L @(R0,R5),R2
    #MOV.L @(R0,R6),R3

    #MOV.B R0,@(0,GBR)
    #MOV.B R0,@(128,GBR)
    #MOV.B R0,@(255,GBR)

    #MOV.W R0,@(0,GBR)
    #MOV.W R0,@(256,GBR)
    #MOV.W R0,@(510,GBR)

    #MOV.L R0,@(0,GBR)
    #MOV.L R0,@(512,GBR)
    #MOV.L R0,@(1020,GBR)

    #MOV.B @(0,GBR),R0
    #MOV.B @(128,GBR),R0
    #MOV.B @(255,GBR),R0

    #MOV.W @(0,GBR),R0
    #MOV.W @(256,GBR),R0
    #MOV.W @(510,GBR),R0

    #MOV.L @(0,GBR),R0
    #MOV.L @(512,GBR),R0
    #MOV.L @(1020,GBR),R0

    #MOVA @(4,PC),R0
    #MOVA @(6,PC),R0
    #MOVA @(8,PC),R0
    #MOVA @(14,PC),R0
    #MOVA @(1020,PC),R0

    #MOVT R0
    #MOVT R5
    #MOVT R15

    #SWAP.B R1,R2
    #SWAP.B R3,R4

    #SWAP.W R1,R2
    #SWAP.W R3,R4

    #XTRCT R1,R2
    #XTRCT R3,R4

    #ADD R1,R2
    #ADD R3,R4

    #ADD #42,R1
    #ADD #-42,R2
    #ADD #-1,R3
    #ADD #255,R4

    #ADDC R1,R2
    #ADDC R3,R4

    #ADDV R1,R2
    #ADDV R3,R4

    #CMP/EQ #0,R0
    #CMP/EQ #42,R0
    #CMP/EQ #-1,R0

    #CMP/EQ R1,R2
    #CMP/EQ R3,R4

    #CMP/HS R1,R2
    #CMP/HS R3,R4

    #CMP/GE R1,R2
    #CMP/GE R3,R4
    
    #CMP/HI R1,R2
    #CMP/HI R3,R4
    
    #CMP/GT R1,R2
    #CMP/GT R3,R4
    
    #CMP/PZ R1
    #CMP/PZ R3
    
    #CMP/PL R1
    #CMP/PL R3
    
    #CMP/STR R1,R2
    #CMP/STR R3,R4

    #DIV1 R1,R2
    #DIV1 R3,R3

    #DIV0S R1,R2
    #DIV0S R3,R4

    #DIV0U
    #DIV0U

    #DMULS.L R1,R2
    #DMULS.L R3,R4

    #DMULU.L R1,R2
    #DMULU.L R3,R4

    #DT R1
    #DT R2

    #EXTS.B R1,R2
    #EXTS.B R3,R4

    #EXTS.W R1,R2
    #EXTS.W R3,R4

    #EXTU.B R1,R2
    #EXTU.B R3,R4

    #EXTU.W R1,R2
    #EXTU.W R3,R4

    #MAC.L @R1+,@R2+
    #MAC.L @R3+,@R4+

    #MAC.W @R1+,@R2+
    #MAC.W @R3+,@R4+

    #MUL.L R1,R2
    #MUL.L R3,R4

    #MULS.W R1,R2
    #MULS.W R3,R4

    #MULU.W R1,R2
    #MULU.W R3,R4

    #NEG R1,R2
    #NEG R3,R4

    #NEGC R1,R2
    #NEGC R3,R4

    #SUB R1,R2
    #SUB R3,R4

    #SUBC R1,R2
    #SUBC R3,R4

    #SUBV R1,R2
    #SUBV R3,R4

    #AND R1,R2
    #AND R3,R4

    #AND #-1,R0
    #AND #0,R0
    #AND #127,R0
    #AND #128,R0
    #AND #255,R0

    #AND.B #-1,@(R0,GBR)
    #AND.B #0,@(R0,GBR)
    #AND.B #127,@(R0,GBR)
    #AND.B #128,@(R0,GBR)
    #AND.B #255,@(R0,GBR)

    #NOT R1,R2
    #NOT R3,R4

    #OR R1,R2
    #OR R3,R4

    #OR #-1,R0
    #OR #0,R0
    #OR #127,R0
    #OR #128,R0
    #OR #255,R0

    #OR.B #-1,@(R0,GBR)
    #OR.B #0,@(R0,GBR)
    #OR.B #127,@(R0,GBR)
    #OR.B #128,@(R0,GBR)
    #OR.B #255,@(R0,GBR)

    #TAS.B @R1
    #TAS.B @R2

    #TST R1,R2
    #TST R3,R4

    #TST #-1,R0
    #TST #0,R0
    #TST #127,R0
    #TST #128,R0
    #TST #255,R0

    #TST.B #-1,@(R0,GBR)
    #TST.B #0,@(R0,GBR)
    #TST.B #127,@(R0,GBR)
    #TST.B #128,@(R0,GBR)
    #TST.B #255,@(R0,GBR)

    #XOR R1,R2
    #XOR R3,R4

    #XOR #-1,R0
    #XOR #0,R0
    #XOR #127,R0
    #XOR #128,R0
    #XOR #255,R0

    #XOR.B #-1,@(R0,GBR)
    #XOR.B #0,@(R0,GBR)
    #XOR.B #127,@(R0,GBR)
    #XOR.B #128,@(R0,GBR)
    #XOR.B #255,@(R0,GBR)

    #ROTL R1
    #ROTL R2

    #ROTR R1
    #ROTR R2

    #ROTCL R1
    #ROTCL R2

    #ROTCR R1
    #ROTCR R2

    #SHAD R1,R2
    #SHAD R3,R4

    #SHAL R1
    #SHAL R2

    #SHAR R1
    #SHAR R2

    #SHLD R1,R2
    #SHLD R3,R4

    #SHLL R1
    #SHLL R2

    #SHLR R1
    #SHLR R2

    #SHLL2 R1
    #SHLL2 R2

    #SHLR2 R1
    #SHLR2 R2

    #SHLL8 R1
    #SHLL8 R2

    #SHLR8 R1
    #SHLR8 R2

    #SHLL16 R1
    #SHLL16 R2

    #SHLR16 R1
    #SHLR16 R2

    #0x262 is where these instructions appear in test file so need to start here
        #for final addresses to come out the same
    #.org 0x262
    #BF 0x250
    #BF 0x300
    #BF/S 0x250
    #BF/S 0x300
    #BT 0x250
    #BT 0x300
    #BT/S 0x250
    #BT/S 0x300
    
    #0x272 is where these instructions appear in test file so need to start here
        #for final addresses to come out the same here and there
    #.org 0x272
    #BRA 0x250
    #BRA 0x300
    #BSR 0x250
    #BSR 0x300

    #BRAF R0
    #BRAF R5
    #BRAF R9

    #BSRF R1
    #BSRF R2
    #BSRF R3

    #JMP @R4
    #JMP @R5
    #JMP @R6

    #JSR @R7
    #JSR @R8
    #JSR @R9

    #RTS

    #CLRMAC

    #CLRS

    #CLRT

    #LDC R1,GBR
    #LDC R2,GBR
    #LDC R3,GBR

    #LDC.L @R4+,GBR
    #LDC.L @R5+,GBR
    #LDC.L @R6+,GBR

    #LDS R1,MACH
    #LDS R2,MACH
    #LDS R3,MACH

    #LDS R4,MACL
    #LDS R5,MACL
    #LDS R6,MACL

    #LDS R7,PR
    #LDS R8,PR
    #LDS R9,PR

    #LDS.L @R0+,MACH
    #LDS.L @R1+,MACH
    #LDS.L @R2+,MACH

    #LDS.L @R3+,MACL
    #LDS.L @R4+,MACL
    #LDS.L @R5+,MACL

    #LDS.L @R6+,PR
    #LDS.L @R7+,PR
    #LDS.L @R8+,PR

    #MOVCA.L R0,@R1
    #MOVCA.L R0,@R2
    #MOVCA.L R0,@R3

    #NOP

    #OCBI @R4
    #OCBI @R5
    #OCBI @R6

    #OCBP @R7
    #OCBP @R8
    #OCBP @R9

    #OCBWB @R1
    #OCBWB @R2
    #OCBWB @R3

    #PREF @R4
    #PREF @R5
    #PREF @R6

    #SETS

    #SETT

    #STC GBR,R7
    #STC GBR,R8
    #STC GBR,R9

    #STC.L GBR,@-R1
    #STC.L GBR,@-R2
    #STC.L GBR,@-R3

    #STS MACH,R4
    #STS MACH,R5
    #STS MACH,R6

    #STS MACL,R7
    #STS MACL,R8
    #STS MACL,R9

    #STS PR,R1
    #STS PR,R2
    #STS PR,R3

    #STS.L MACH,@-R4
    #STS.L MACH,@-R5
    #STS.L MACH,@-R6

    #STS.L MACL,@-R7
    #STS.L MACL,@-R8
    #STS.L MACL,@-R9

    #STS.L PR,@-R1
    #STS.L PR,@-R2
    #STS.L PR,@-R3

    #STC SR,R1
    #STC SR,R2
    #STC SR,R3

    #STC VBR,R4
    #STC VBR,R5
    #STC VBR,R6

    #STC SSR,R7
    #STC SSR,R8
    #STC SSR,R9

    #STC SPC,R1
    #STC SPC,R2
    #STC SPC,R3

    #STC SGR,R4
    #STC SGR,R5
    #STC SGR,R6

    #STC DBR,R7
    #STC DBR,R8
    #STC DBR,R9

    #STC R5_BANK,R1
    #STC R6_BANK,R2
    #STC R7_BANK,R3

    #STC.L SR,@-R4
    #STC.L SR,@-R5
    #STC.L SR,@-R6

    #STC.L VBR,@-R7
    #STC.L VBR,@-R8
    #STC.L VBR,@-R9

    #STC.L SSR,@-R1
    #STC.L SSR,@-R2
    #STC.L SSR,@-R3

    #STC.L SPC,@-R4
    #STC.L SPC,@-R5
    #STC.L SPC,@-R6

    #STC.L SGR,@-R1
    #STC.L SGR,@-R2
    #STC.L SGR,@-R3

    #STC.L DBR,@-R4
    #STC.L DBR,@-R5
    #STC.L DBR,@-R6

    #STC.L R1_BANK,@-R7
    #STC.L R2_BANK,@-R8
    #STC.L R3_BANK,@-R9

    #TRAPA #0
    #TRAPA #128
    #TRAPA #255

    #FLDI0 FR4
    #FLDI0 FR5
    #FLDI0 FR6

    #FLDI1 FR7
    #FLDI1 FR8
    #FLDI1 FR9

    #FMOV FR1,FR7
    #FMOV FR2,FR8
    #FMOV FR3,FR9

    #FMOV.S @R1,FR4
    #FMOV.S @R2,FR5
    #FMOV.S @R3,FR6

    #FMOV.S @(R0,R1),FR4
    #FMOV.S @(R0,R2),FR5
    #FMOV.S @(R0,R3),FR6

    #FMOV.S @R1+,FR4
    #FMOV.S @R2+,FR5
    #FMOV.S @R3+,FR6

    #FMOV.S FR1,@R7
    #FMOV.S FR2,@R8
    #FMOV.S FR3,@R9

    #FMOV.S FR4,@-R1
    #FMOV.S FR5,@-R2
    #FMOV.S FR6,@-R3

    #FMOV.S FR7,@(R0,R4)
    #FMOV.S FR8,@(R0,R5)
    #FMOV.S FR9,@(R0,R6)

    #FMOV DR0,DR6
    #FMOV DR2,DR8
    #FMOV DR4,DR10

    #FMOV @R4,DR2
    #FMOV @R5,DR4
    #FMOV @R6,DR6

    #FMOV @(R0,R7),DR8
    #FMOV @(R0,R8),DR10
    #FMOV @(R0,R9),DR12

    #FMOV @R1+,DR2
    #FMOV @R2+,DR4
    #FMOV @R3+,DR6

    #FMOV DR0,@R1
    #FMOV DR2,@R2
    #FMOV DR4,@R3

    #FMOV DR6,@-R4
    #FMOV DR8,@-R5
    #FMOV DR10,@-R6

    #FMOV DR12,@(R0,R7)
    #FMOV DR14,@(R0,R8)
    #FMOV DR0,@(R0,R9)

    #FLDS FR1,FPUL
    #FLDS FR2,FPUL
    #FLDS FR3,FPUL

    #FSTS FPUL,FR4
    #FSTS FPUL,FR5
    #FSTS FPUL,FR6

    #FABS FR7
    #FABS FR8
    #FABS FR9

    #FADD FR1,FR7
    #FADD FR2,FR8
    #FADD FR3,FR9

    #FCMP/EQ FR4,FR1
    #FCMP/EQ FR5,FR2
    #FCMP/EQ FR6,FR3

    #FCMP/GT FR7,FR4
    #FCMP/GT FR8,FR5
    #FCMP/GT FR9,FR6

    #FDIV FR1,FR7
    #FDIV FR2,FR8
    #FDIV FR3,FR9

    #FLOAT FPUL,FR4
    #FLOAT FPUL,FR5
    #FLOAT FPUL,FR6

    #FMAC FR0,FR7,FR1
    #FMAC FR0,FR8,FR2
    #FMAC FR0,FR9,FR3

    #FMUL FR1,FR4
    #FMUL FR2,FR5
    #FMUL FR3,FR6

    #FNEG FR4
    #FNEG FR5
    #FNEG FR6

    #FSQRT FR7
    #FSQRT FR8
    #FSQRT FR9

    #FSUB FR1,FR7
    #FSUB FR2,FR8
    #FSUB FR3,FR9

    #FTRC FR4,FPUL
    #FTRC FR5,FPUL
    #FTRC FR6,FPUL

    #FABS DR2
    #FABS DR4
    #FABS DR6

    #FADD DR0,DR6
    #FADD DR2,DR8
    #FADD DR4,DR10

    #FCMP/EQ DR0,DR6
    #FCMP/EQ DR2,DR8
    #FCMP/EQ DR4,DR10

    #FCMP/GT DR0,DR6
    #FCMP/GT DR2,DR8
    #FCMP/GT DR4,DR10

    #FDIV DR4,DR10
    #FDIV DR6,DR12
    #FDIV DR8,DR14

    #FCNVDS DR2,FPUL
    #FCNVDS DR4,FPUL
    #FCNVDS DR6,FPUL

    #FCNVSD FPUL,DR8
    #FCNVSD FPUL,DR10
    #FCNVSD FPUL,DR12

    #FLOAT FPUL,DR0
    #FLOAT FPUL,DR2
    #FLOAT FPUL,DR4

    #FMUL DR4,DR10
    #FMUL DR6,DR12
    #FMUL DR8,DR14

    #FNEG DR2
    #FNEG DR4
    #FNEG DR6

    #FSQRT DR4
    #FSQRT DR6
    #FSQRT DR8

    #FSUB DR0,DR6
    #FSUB DR2,DR8
    #FSUB DR4,DR10

    #FTRC DR2,FPUL
    #FTRC DR4,FPUL
    #FTRC DR6,FPUL

    #LDS R1,FPSCR
    #LDS R2,FPSCR
    #LDS R3,FPSCR

    #LDS R4,FPUL
    #LDS R5,FPUL
    #LDS R6,FPUL

    #LDS.L @R7+,FPSCR
    #LDS.L @R8+,FPSCR
    #LDS.L @R9+,FPSCR

    #LDS.L @R1+,FPUL
    #LDS.L @R2+,FPUL
    #LDS.L @R3+,FPUL

    #STS FPSCR,R4
    #STS FPSCR,R5
    #STS FPSCR,R6

    #STS FPUL,R7
    #STS FPUL,R8
    #STS FPUL,R9

    #STS.L FPSCR,@-R1
    #STS.L FPSCR,@-R2
    #STS.L FPSCR,@-R3

    #STS.L FPUL,@-R4
    #STS.L FPUL,@-R5
    #STS.L FPUL,@-R6

    #FMOV DR2,XD6
    #FMOV DR4,XD8
    #FMOV DR6,XD10

    #FMOV XD2,DR10
    #FMOV XD4,DR12
    #FMOV XD6,DR14

    #FMOV XD8,XD14
    #FMOV XD10,XD2
    #FMOV XD12,XD4

    #FMOV @R1,XD6
    #FMOV @R2,XD8
    #FMOV @R3,XD10

    #FMOV @R4+,XD0
    #FMOV @R5+,XD2
    #FMOV @R6+,XD4

    #FMOV @(R0,R7),DR6
    #FMOV @(R0,R8),DR8
    #FMOV @(R0,R9),DR10

    #FMOV XD10,@R1
    #FMOV XD12,@R2
    #FMOV XD14,@R3

    #FMOV XD0,@-R4
    #FMOV XD2,@-R5
    #FMOV XD4,@-R6

    #FMOV XD6,@(R0,R7)
    #FMOV XD8,@(R0,R8)
    #FMOV XD10,@(R0,R9)

    #FIPR FV0,FV12
    #FIPR FV4,FV0
    #FIPR FV8,FV4

    #FTRV XMTRX,FV0
    #FTRV XMTRX,FV4
    #FTRV XMTRX,FV8

    #FRCHG
    #FRCHG
    #FRCHG

    #FSCHG
    #FSCHG
    #FSCHG

    #Repeat - objdump shows FMOV not FMOV.S
    #FMOV @R1,FR4
    #FMOV @R2,FR5
    #FMOV @R3,FR6

    #FMOV @(R0,R1),FR4
    #FMOV @(R0,R2),FR5
    #FMOV @(R0,R3),FR6

    #FMOV @R1+,FR4
    #FMOV @R2+,FR5
    #FMOV @R3+,FR6

    #FMOV FR1,@R7
    #FMOV FR2,@R8
    #FMOV FR3,@R9

    #FMOV FR4,@-R1
    #FMOV FR5,@-R2
    #FMOV FR6,@-R3

    #FMOV FR7,@(R0,R4)
    #FMOV FR8,@(R0,R5)
    #FMOV FR9,@(R0,R6)
    
    #.org 0x4F8
    #MOV.L 0x500,R5
    #MOV.L 0x500,R5

    #.org 0x11000
    #BT 0x11004

    #mov # - 42,R1

    mov #255,R0
