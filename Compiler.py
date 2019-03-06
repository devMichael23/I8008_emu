import random


def isInt(num):
    try:
        int(num)
        return True
    except ValueError:
        return False


class Compiler:
    def __init__(self, instructionstream):
        print("Intel 8008 Master")
        try:
            st = input()
        except KeyboardInterrupt:
            print("PROCESS STOP\n")
        try:
            while (st != "STOP" and st != "START"):
                print("Only 'START' or 'STOP'")
                st = input()
                if (st == "START"):
                    break
                elif (st == "STOP"):
                    break
                else:
                    continue
            if (st == "START"):
                print("Success Started")
                while True:
                    opcode = input("> ")
                    if isInt(opcode):
                        instructionstream.append(int(opcode))
                    elif opcode == "HLT0":
                        instructionstream.append(int(0x00))
                    elif opcode == "HLT1":
                        instructionstream.append(int(0x01))
                    elif opcode == "HLTF":
                        instructionstream.append(int(0xFF))
                    elif opcode == "OUT":
                        instructionstream.append(int(
                            random.randrange(0x51, 0x7F, 2)))
                    elif opcode == "IN":
                        instructionstream.append(int(
                            random.randrange(0x41, 0x4F, 2)))
                    elif opcode == "JMP":
                        instructionstream.append(int(
                            random.randrange(0x44, 0x7C, 8)))
                    elif opcode == "JFC":
                        instructionstream.append(int(0x40))
                    elif opcode == "JTC":
                        instructionstream.append(int(0x60))
                    elif opcode == "JTP":
                        instructionstream.append(int(0x78))
                    elif opcode == "JFP":
                        instructionstream.append(int(0x58))
                    elif opcode == "JFS":
                        instructionstream.append(int(0x50))
                    elif opcode == "JTS":
                        instructionstream.append(int(0x70))
                    elif opcode == "JFZ":
                        instructionstream.append(int(0x48))
                    elif opcode == "JTZ":
                        instructionstream.append(int(0x68))
                    elif opcode == "CAL":
                        instructionstream.append(int(
                            random.randrange(0x46, 0x7E, 8)))
                    elif opcode == "CFC":
                        instructionstream.append(int(0x42))
                    elif opcode == "CTC":
                        instructionstream.append(int(0x62))
                    elif opcode == "CTP":
                        instructionstream.append(int(0x7A))
                    elif opcode == "CFP":
                        instructionstream.append(int(0x5A))
                    elif opcode == "CFS":
                        instructionstream.append(int(0x52))
                    elif opcode == "CTS":
                        instructionstream.append(int(0x72))
                    elif opcode == "CFZ":
                        instructionstream.append(int(0x4A))
                    elif opcode == "CTZ":
                        instructionstream.append(int(0x6A))
                    elif opcode == "RET":
                        instructionstream.append(int(
                            random.randrange(0x07, 0x3F, 8)))
                    elif opcode == "RFC":
                        instructionstream.append(int(0x03))
                    elif opcode == "RTC":
                        instructionstream.append(int(0x23))
                    elif opcode == "RTP":
                        instructionstream.append(int(0x3B))
                    elif opcode == "RFP":
                        instructionstream.append(int(0x1B))
                    elif opcode == "RFS":
                        instructionstream.append(int(0x13))
                    elif opcode == "RTS":
                        instructionstream.append(int(0x33))
                    elif opcode == "RFZ":
                        instructionstream.append(int(0x0B))
                    elif opcode == "RTZ":
                        instructionstream.append(int(0x2B))
                    elif opcode == "RST":
                        instructionstream.append(int(
                            random.randrange(0x05, 0x3D, 8)))
                    elif opcode == "LAI":
                        instructionstream.append(int(0x06))
                    elif opcode == "LAA":
                        instructionstream.append(int(0xC0))
                    elif opcode == "LAB":
                        instructionstream.append(int(0xC1))
                    elif opcode == "LAC":
                        instructionstream.append(int(0xC2))
                    elif opcode == "LAD":
                        instructionstream.append(int(0xC3))
                    elif opcode == "LAE":
                        instructionstream.append(int(0xC4))
                    elif opcode == "LAH":
                        instructionstream.append(int(0xC5))
                    elif opcode == "LAL":
                        instructionstream.append(int(0xC6))
                    elif opcode == "LAM":
                        instructionstream.append(int(0xC7))
                    elif opcode == "LBI":
                        instructionstream.append(int(0x0E))
                    elif opcode == "LBA":
                        instructionstream.append(int(0xC8))
                    elif opcode == "LBB":
                        instructionstream.append(int(0xC9))
                    elif opcode == "LBC":
                        instructionstream.append(int(0xCA))
                    elif opcode == "LBD":
                        instructionstream.append(int(0xCB))
                    elif opcode == "LBE":
                        instructionstream.append(int(0xCC))
                    elif opcode == "LBH":
                        instructionstream.append(int(0xCD))
                    elif opcode == "LBL":
                        instructionstream.append(int(0xCE))
                    elif opcode == "LBM":
                        instructionstream.append(int(0xCF))
                    elif opcode == "LCI":
                        instructionstream.append(int(0x16))
                    elif opcode == "LCA":
                        instructionstream.append(int(0xD0))
                    elif opcode == "LCB":
                        instructionstream.append(int(0xD1))
                    elif opcode == "LCC":
                        instructionstream.append(int(0xD2))
                    elif opcode == "LCD":
                        instructionstream.append(int(0xD3))
                    elif opcode == "LCE":
                        instructionstream.append(int(0xD4))
                    elif opcode == "LCH":
                        instructionstream.append(int(0xD5))
                    elif opcode == "LCL":
                        instructionstream.append(int(0xD6))
                    elif opcode == "LCM":
                        instructionstream.append(int(0xD7))
                    elif opcode == "LDI":
                        instructionstream.append(int(0x1E))
                    elif opcode == "LDA":
                        instructionstream.append(int(0xD8))
                    elif opcode == "LDB":
                        instructionstream.append(int(0xD9))
                    elif opcode == "LDC":
                        instructionstream.append(int(0xDA))
                    elif opcode == "LDD":
                        instructionstream.append(int(0xDB))
                    elif opcode == "LDE":
                        instructionstream.append(int(0xDC))
                    elif opcode == "LDH":
                        instructionstream.append(int(0xDD))
                    elif opcode == "LDL":
                        instructionstream.append(int(0xDE))
                    elif opcode == "LDM":
                        instructionstream.append(int(0xDF))
                    elif opcode == "LEI":
                        instructionstream.append(int(0x26))
                    elif opcode == "LEA":
                        instructionstream.append(int(0xE0))
                    elif opcode == "LEB":
                        instructionstream.append(int(0xE1))
                    elif opcode == "LEC":
                        instructionstream.append(int(0xE2))
                    elif opcode == "LED":
                        instructionstream.append(int(0xE3))
                    elif opcode == "LEE":
                        instructionstream.append(int(0xE4))
                    elif opcode == "LEH":
                        instructionstream.append(int(0xE5))
                    elif opcode == "LEL":
                        instructionstream.append(int(0xE6))
                    elif opcode == "LEM":
                        instructionstream.append(int(0xE7))
                    elif opcode == "LHI":
                        instructionstream.append(int(0x2E))
                    elif opcode == "LHA":
                        instructionstream.append(int(0xE8))
                    elif opcode == "LHB":
                        instructionstream.append(int(0xE9))
                    elif opcode == "LHC":
                        instructionstream.append(int(0xEA))
                    elif opcode == "LHD":
                        instructionstream.append(int(0xEB))
                    elif opcode == "LHE":
                        instructionstream.append(int(0xEC))
                    elif opcode == "LHH":
                        instructionstream.append(int(0xED))
                    elif opcode == "LHL":
                        instructionstream.append(int(0xEE))
                    elif opcode == "LHM":
                        instructionstream.append(int(0xEF))
                    elif opcode == "LLI":
                        instructionstream.append(int(0x36))
                    elif opcode == "LLA":
                        instructionstream.append(int(0xF0))
                    elif opcode == "LLB":
                        instructionstream.append(int(0xF1))
                    elif opcode == "LLC":
                        instructionstream.append(int(0xF2))
                    elif opcode == "LLD":
                        instructionstream.append(int(0xF3))
                    elif opcode == "LLE":
                        instructionstream.append(int(0xF4))
                    elif opcode == "LLH":
                        instructionstream.append(int(0xF5))
                    elif opcode == "LLL":
                        instructionstream.append(int(0xF6))
                    elif opcode == "LLM":
                        instructionstream.append(int(0xF7))
                    elif opcode == "LMI":
                        instructionstream.append(int(0x3E))
                    elif opcode == "LMA":
                        instructionstream.append(int(0xF8))
                    elif opcode == "LMB":
                        instructionstream.append(int(0xF9))
                    elif opcode == "LMC":
                        instructionstream.append(int(0xFA))
                    elif opcode == "LMD":
                        instructionstream.append(int(0xFB))
                    elif opcode == "LME":
                        instructionstream.append(int(0xFC))
                    elif opcode == "LMH":
                        instructionstream.append(int(0xFD))
                    elif opcode == "LML":
                        instructionstream.append(int(0xFE))
                    elif opcode == "ACA":
                        instructionstream.append(int(0x88))
                    elif opcode == "ADA":
                        instructionstream.append(int(0x80))
                    elif opcode == "ACB":
                        instructionstream.append(int(0x89))
                    elif opcode == "ADB":
                        instructionstream.append(int(0x81))
                    elif opcode == "ACC":
                        instructionstream.append(int(0x8A))
                    elif opcode == "ADC":
                        instructionstream.append(int(0x82))
                    elif opcode == "ACD":
                        instructionstream.append(int(0x8B))
                    elif opcode == "ADD":
                        instructionstream.append(int(0x83))
                    elif opcode == "ACE":
                        instructionstream.append(int(0x8C))
                    elif opcode == "ADE":
                        instructionstream.append(int(0x84))
                    elif opcode == "ACH":
                        instructionstream.append(int(0x8D))
                    elif opcode == "ADH":
                        instructionstream.append(int(0x85))
                    elif opcode == "ADL":
                        instructionstream.append(int(0x86))
                    elif opcode == "ACL":
                        instructionstream.append(int(0x8E))
                    elif opcode == "ADI":
                        instructionstream.append(int(0x04))
                    elif opcode == "ACM":
                        instructionstream.append(int(0x8F))
                    elif opcode == "ADM":
                        instructionstream.append(int(0x87))
                    elif opcode == "ACI":
                        instructionstream.append(int(0x0C))
                    elif opcode == "SBA":
                        instructionstream.append(int(0x98))
                    elif opcode == "SUA":
                        instructionstream.append(int(0x90))
                    elif opcode == "SBB":
                        instructionstream.append(int(0x99))
                    elif opcode == "SUB":
                        instructionstream.append(int(0x91))
                    elif opcode == "SBC":
                        instructionstream.append(int(0x9A))
                    elif opcode == "SUC":
                        instructionstream.append(int(0x92))
                    elif opcode == "SBD":
                        instructionstream.append(int(0x9B))
                    elif opcode == "SUD":
                        instructionstream.append(int(0x93))
                    elif opcode == "SBE":
                        instructionstream.append(int(0x9C))
                    elif opcode == "SUE":
                        instructionstream.append(int(0x94))
                    elif opcode == "SBH":
                        instructionstream.append(int(0x9D))
                    elif opcode == "SUH":
                        instructionstream.append(int(0x95))
                    elif opcode == "SUL":
                        instructionstream.append(int(0x96))
                    elif opcode == "SBL":
                        instructionstream.append(int(0x9E))
                    elif opcode == "SUI":
                        instructionstream.append(int(0x14))
                    elif opcode == "SBM":
                        instructionstream.append(int(0x9F))
                    elif opcode == "SUM":
                        instructionstream.append(int(0x97))
                    elif opcode == "SBI":
                        instructionstream.append(int(0x1C))
                    elif opcode == "NDA":
                        instructionstream.append(int(0xA0))
                    elif opcode == "NDB":
                        instructionstream.append(int(0xA1))
                    elif opcode == "NDC":
                        instructionstream.append(int(0xA2))
                    elif opcode == "NDD":
                        instructionstream.append(int(0xA3))
                    elif opcode == "NDE":
                        instructionstream.append(int(0xA4))
                    elif opcode == "NDH":
                        instructionstream.append(int(0xA5))
                    elif opcode == "NDL":
                        instructionstream.append(int(0xA6))
                    elif opcode == "NDI":
                        instructionstream.append(int(0x24))
                    elif opcode == "NDM":
                        instructionstream.append(int(0xA7))
                    elif opcode == "XRA":
                        instructionstream.append(int(0xA8))
                    elif opcode == "XRB":
                        instructionstream.append(int(0xA9))
                    elif opcode == "XRC":
                        instructionstream.append(int(0xAA))
                    elif opcode == "XRD":
                        instructionstream.append(int(0xAB))
                    elif opcode == "XRE":
                        instructionstream.append(int(0xAC))
                    elif opcode == "XRH":
                        instructionstream.append(int(0xAD))
                    elif opcode == "XRL":
                        instructionstream.append(int(0xAE))
                    elif opcode == "XRI":
                        instructionstream.append(int(0x2C))
                    elif opcode == "XRM":
                        instructionstream.append(int(0xAF))
                    elif opcode == "ORA":
                        instructionstream.append(int(0xB0))
                    elif opcode == "ORB":
                        instructionstream.append(int(0xB1))
                    elif opcode == "ORC":
                        instructionstream.append(int(0xB2))
                    elif opcode == "ORD":
                        instructionstream.append(int(0xB3))
                    elif opcode == "ORE":
                        instructionstream.append(int(0xB4))
                    elif opcode == "ORH":
                        instructionstream.append(int(0xB5))
                    elif opcode == "ORL":
                        instructionstream.append(int(0xB6))
                    elif opcode == "ORI":
                        instructionstream.append(int(0x34))
                    elif opcode == "ORM":
                        instructionstream.append(int(0xB7))
                    elif opcode == "CPA":
                        instructionstream.append(int(0xB8))
                    elif opcode == "CPB":
                        instructionstream.append(int(0xB9))
                    elif opcode == "CPC":
                        instructionstream.append(int(0xBA))
                    elif opcode == "CPD":
                        instructionstream.append(int(0xBB))
                    elif opcode == "CPE":
                        instructionstream.append(int(0xBC))
                    elif opcode == "CPH":
                        instructionstream.append(int(0xBD))
                    elif opcode == "CPL":
                        instructionstream.append(int(0xBE))
                    elif opcode == "CPI":
                        instructionstream.append(int(0x3C))
                    elif opcode == "CPM":
                        instructionstream.append(int(0xBF))
                    elif opcode == "INB":
                        instructionstream.append(int(0x08))
                    elif opcode == "INC":
                        instructionstream.append(int(0x10))
                    elif opcode == "IND":
                        instructionstream.append(int(0x18))
                    elif opcode == "INE":
                        instructionstream.append(int(0x20))
                    elif opcode == "ICH":
                        instructionstream.append(int(0x28))
                    elif opcode == "INL":
                        instructionstream.append(int(0x30))
                    elif opcode == "DCB":
                        instructionstream.append(int(0x09))
                    elif opcode == "DCC":
                        instructionstream.append(int(0x11))
                    elif opcode == "DCD":
                        instructionstream.append(int(0x19))
                    elif opcode == "DCE":
                        instructionstream.append(int(0x21))
                    elif opcode == "DCH":
                        instructionstream.append(int(0x29))
                    elif opcode == "DCL":
                        instructionstream.append(int(0x31))
                    elif opcode == "RAL":
                        instructionstream.append(int(0x12))
                    elif opcode == "RLC":
                        instructionstream.append(int(0x02))
                    elif opcode == "RAR":
                        instructionstream.append(int(0x1A))
                    elif opcode == "RRC":
                        instructionstream.append(int(0x0A))
                    elif opcode == "STOP":
                        print("OK")
                        break
                    elif opcode == "START":
                        print("ALREADY STARTED")
                        continue
                    else:
                        print("ERROR: UNIMPLEMENTED INSTRUCTION")
                        continue
            elif (st == "STOP"):
                print("OK")
            if not instructionstream:
                instructionstream.append(int(0))
        except UnboundLocalError:
            instructionstream.append(int(0))

    def startTest(instructionstream):
        try:
            print("Intel 8008 Test")
            print("Test 2+2=4")
            instructionstream.append(0x06)
            instructionstream.append(2)
            instructionstream.append(0x0E)
            instructionstream.append(2)
            instructionstream.append(0x81)
            print("Test Success")
        except Exception:
            print("Test Failed")
