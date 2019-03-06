from MotherBoard import MotherBoard
import Memory


def mask(mask: int, tale: int, offset=0):
    return (mask & tale) >> offset


def pc_add(pcx: int, n: int):
    pc = pcx + n
    if pc < 0:
        pc += 16384
    pc %= 16384
    return pc


def sp_add(spx: int, n: int):
    sp = spx + n
    if sp == 8:
        sp = 0
    if sp == (-1):
        sp = 7
    return sp


class i8008:
    def __init__(self):
        self.A = 0  # аккумулятор
        self.B = 0
        self.C = 0
        self.D = 0  # Data
        self.E = 0
        self.H = 0  # Memory
        self.L = 0  # Pointer
        self.M = 0

        self.SP = 0
        self.stack_ = 0
        self.stack = [0, 0, 0, 0, 0, 0, 0, 0]

        self.motherBoard = MotherBoard()
        self.memory = Memory.Memory()

        self.carry = 0  # переполнение при операции
        self.zero = 0
        self.parity = 0  # четность/нечетность
        self.sign = 0  # положительный/отрицательный

        self.states = {
            "Wait": 0b000,  # Ожидание медленной памяти
            "T3": 0b001,  # Ввод/вывод данных (доступ к памяти)
            "T1": 0b010,  # Менее значимый адресный байт
            "Stop": 0b011,  # Ожидание прерывания (HLT)
            "T2": 0b100,  # Более значимый адрес byte + cc2 + cc1
            "T5": 0b101,  # Внутренняя передача данных
            "T1l": 0b110,  # Как и T1, но распознанное прерывание
            "T4": 0b111  # Внутренняя передача данных
        }

        self.pins = {
            "Vdd": 0,
            "D7": 0,
            "D6": 0,
            "D5": 0,
            "D4": 0,
            "D3": 0,
            "D2": 0,
            "D1": 0,
            "D0": 0,
            "Vcc": 0,
            "S2": 0,
            "S1": 0,
            "S0": 0,
            "Sync": 0,
            "Phase 2": 0,
            "Phase 1": 0,
            "Ready": 0,
            "Interrupt": 0,
        }

    @property
    def M(self):
        self._M = (self.H << 8) + self.L
        return self._M

    @M.getter
    def M(self):
        self._M = (self.H << 8) + self.L
        return self._M

    @M.setter
    def M(self, value):
        self._M = (self.H << 8) + self.L
        self._M = value

    def instruction(self, opcode):
        #                               CPU control
        if opcode == 0x00:
            self.HLT()
        elif opcode == 0x01:
            self.HLT()
        elif opcode == 0xFF:
            self.HLT()

        #                               Input/Output
        elif opcode == 0x51:
            self.OUT()
        elif opcode == 0x53:
            self.OUT()
        elif opcode == 0x55:
            self.OUT()
        elif opcode == 0x57:
            self.OUT()
        elif opcode == 0x59:
            self.OUT()
        elif opcode == 0x5B:
            self.OUT()
        elif opcode == 0x5D:
            self.OUT()
        elif opcode == 0x5F:
            self.OUT()
        elif opcode == 0x61:
            self.OUT()
        elif opcode == 0x63:
            self.OUT()
        elif opcode == 0x65:
            self.OUT()
        elif opcode == 0x67:
            self.OUT()
        elif opcode == 0x69:
            self.OUT()
        elif opcode == 0x6B:
            self.OUT()
        elif opcode == 0x6D:
            self.OUT()
        elif opcode == 0x6F:
            self.OUT()
        elif opcode == 0x71:
            self.OUT()
        elif opcode == 0x73:
            self.OUT()
        elif opcode == 0x77:
            self.OUT()
        elif opcode == 0x79:
            self.OUT()
        elif opcode == 0x7B:
            self.OUT()
        elif opcode == 0x7D:
            self.OUT()
        elif opcode == 0x7F:
            self.OUT()
        elif opcode == 0x41:
            self.INP()
        elif opcode == 0x43:
            self.INP()
        elif opcode == 0x45:
            self.INP()
        elif opcode == 0x47:
            self.INP()
        elif opcode == 0x49:
            self.INP()
        elif opcode == 0x4B:
            self.INP()
        elif opcode == 0x4D:
            self.INP()
        elif opcode == 0x4F:
            self.INP()

        #                               Jump
        elif opcode == 0x44:
            self.JMP()
        elif opcode == 0x4C:
            self.JMP()
        elif opcode == 0x54:
            self.JMP()
        elif opcode == 0x5C:
            self.JMP()
        elif opcode == 0x64:
            self.JMP()
        elif opcode == 0x6C:
            self.JMP()
        elif opcode == 0x74:
            self.JMP()
        elif opcode == 0x7C:
            self.JMP()
        elif (opcode == 0x40) & (self.carry == 0):
            self.JFC()
        elif (opcode == 0x60) & (self.carry == 1):
            self.JTC()
        elif (opcode == 0x78) & (self.parity % 2 == 0):
            self.JTP()
        elif (opcode == 0x58) & (self.parity % 2 != 0):
            self.JFP()
        elif (opcode == 0x50) & (self.sign == 0):
            self.JFS()
        elif (opcode == 0x70) & (self.sign == 1):
            self.JTS()
        elif (opcode == 0x48) & (self.zero == 0):
            self.JFZ()
        elif (opcode == 0x68) & (self.zero == 1):
            self.JTZ()

        #                               Call
        elif opcode == 0x46:
            self.CAL()
        elif opcode == 0x4E:
            self.CAL()
        elif opcode == 0x56:
            self.CAL()
        elif opcode == 0x5E:
            self.CAL()
        elif opcode == 0x66:
            self.CAL()
        elif opcode == 0x6E:
            self.CAL()
        elif opcode == 0x76:
            self.CAL()
        elif opcode == 0x7E:
            self.CAL()
        elif (opcode == 0x42) & (self.carry == 0):
            self.CFC()
        elif (opcode == 0x62) & (self.carry == 1):
            self.CTC()
        elif (opcode == 0x7A) & (self.parity % 2 == 0):
            self.CTP()
        elif (opcode == 0x5A) & (self.parity % 2 != 0):
            self.CFP()
        elif (opcode == 0x52) & (self.sign == 0):
            self.CFS()
        elif (opcode == 0x72) & (self.sign == 1):
            self.CTS()
        elif (opcode == 0x4A) & (self.zero == 0):
            self.CFZ()
        elif (opcode == 0x6A) & (self.zero == 1):
            self.CTZ()

        #                               Return
        elif opcode == 0x07:
            self.RET()
        elif opcode == 0x0F:
            self.RET()
        elif opcode == 0x17:
            self.RET()
        elif opcode == 0x1F:
            self.RET()
        elif opcode == 0x27:
            self.RET()
        elif opcode == 0x2F:
            self.RET()
        elif opcode == 0x37:
            self.RET()
        elif opcode == 0x3F:
            self.RET()
        elif (opcode == 0x03) & (self.carry == 0):
            self.RFC()
        elif (opcode == 0x23) & (self.carry == 1):
            self.RTC()
        elif (opcode == 0x3B) & (self.parity % 2 == 0):
            self.RTP()
        elif (opcode == 0x1B) & (self.parity % 2 != 0):
            self.RFP()
        elif (opcode == 0x13) & (self.sign == 0):
            self.RFS()
        elif (opcode == 0x33) & (self.sign == 1):
            self.RTS()
        elif (opcode == 0x0B) & (self.zero == 0):
            self.RFZ()
        elif (opcode == 0x3B) & (self.zero == 1):
            self.RTZ()
        elif opcode == 0x05:
            self.RST()
        elif opcode == 0x0D:
            self.RST()
        elif opcode == 0x15:
            self.RST()
        elif opcode == 0x1D:
            self.RST()
        elif opcode == 0x25:
            self.RST()
        elif opcode == 0x2D:
            self.RST()
        elif opcode == 0x35:
            self.RST()
        elif opcode == 0x3D:
            self.RST()

        #                               Load
        elif opcode == 0x06:
            self.LAI()
        elif opcode == 0xC0:
            self.LAA()
        elif opcode == 0xC1:
            self.LAB()
        elif opcode == 0xC2:
            self.LAC()
        elif opcode == 0xC3:
            self.LAD()
        elif opcode == 0xC4:
            self.LAE()
        elif opcode == 0xC5:
            self.LAH()
        elif opcode == 0xC6:
            self.LAL()
        elif opcode == 0xC7:
            self.LAM()
        elif opcode == 0x0E:
            self.LBI()
        elif opcode == 0xC8:
            self.LBA()
        elif opcode == 0xC9:
            self.LBB()
        elif opcode == 0xCA:
            self.LBC()
        elif opcode == 0xCB:
            self.LBD()
        elif opcode == 0xCC:
            self.LBE()
        elif opcode == 0xCD:
            self.LBH()
        elif opcode == 0xCE:
            self.LBL()
        elif opcode == 0xCF:
            self.LBM()
        elif opcode == 0x16:
            self.LCI()
        elif opcode == 0xD0:
            self.LCA()
        elif opcode == 0xD1:
            self.LCB()
        elif opcode == 0xD2:
            self.LCC()
        elif opcode == 0xD3:
            self.LCD()
        elif opcode == 0xD4:
            self.LCE()
        elif opcode == 0xD5:
            self.LCH()
        elif opcode == 0xD6:
            self.LCL()
        elif opcode == 0xD7:
            self.LDM()
        elif opcode == 0x1E:
            self.LDI()
        elif opcode == 0xD8:
            self.LDA()
        elif opcode == 0xD9:
            self.LDB()
        elif opcode == 0xDA:
            self.LDC()
        elif opcode == 0xDB:
            self.LDD()
        elif opcode == 0xDC:
            self.LDE()
        elif opcode == 0xDD:
            self.LDH()
        elif opcode == 0xDE:
            self.LDL()
        elif opcode == 0xDF:
            self.LDM()
        elif opcode == 0x26:
            self.LEI()
        elif opcode == 0xE0:
            self.LEA()
        elif opcode == 0xE1:
            self.LEB()
        elif opcode == 0xE2:
            self.LEC()
        elif opcode == 0xE3:
            self.LED()
        elif opcode == 0xE4:
            self.LEE()
        elif opcode == 0xE5:
            self.LEH()
        elif opcode == 0xE6:
            self.LEL()
        elif opcode == 0xE7:
            self.LEM()
        elif opcode == 0x2E:
            self.LHI()
        elif opcode == 0xE8:
            self.LHA()
        elif opcode == 0xE9:
            self.LHB()
        elif opcode == 0xEA:
            self.LHC()
        elif opcode == 0xEB:
            self.LHD()
        elif opcode == 0xEC:
            self.LHE()
        elif opcode == 0xED:
            self.LHH()
        elif opcode == 0xEE:
            self.LHL()
        elif opcode == 0xEF:
            self.LHM()

        elif opcode == 0x36:
            self.LLI()
        elif opcode == 0xF0:
            self.LLA()
        elif opcode == 0xF1:
            self.LLB()
        elif opcode == 0xF2:
            self.LLC()
        elif opcode == 0xF3:
            self.LLD()
        elif opcode == 0xF4:
            self.LLE()
        elif opcode == 0xF5:
            self.LLH()
        elif opcode == 0xF6:
            self.LLL()
        elif opcode == 0xF7:
            self.LLM()
        elif opcode == 0x3E:
            self.LMI()
        elif opcode == 0xF8:
            self.LMA()
        elif opcode == 0xF9:
            self.LMB()
        elif opcode == 0xFA:
            self.LMC()
        elif opcode == 0xFB:
            self.LMD()
        elif opcode == 0xFC:
            self.LME()
        elif opcode == 0xFD:
            self.LMH()
        elif opcode == 0xFE:
            self.LML()

        #                               Arithmetic
        elif opcode == 0x88:
            self.ACA()
        elif opcode == 0x80:
            self.ADA()
        elif opcode == 0x89:
            self.ACB()
        elif opcode == 0x81:
            self.ADB()
        elif opcode == 0x8A:
            self.ACC()
        elif opcode == 0x82:
            self.ADC()
        elif opcode == 0x8B:
            self.ACD()
        elif opcode == 0x83:
            self.ADD()
        elif opcode == 0x8C:
            self.ACE()
        elif opcode == 0x84:
            self.ADE()
        elif opcode == 0x8D:
            self.ACH()
        elif opcode == 0x85:
            self.ADH()
        elif opcode == 0x86:
            self.ADL()
        elif opcode == 0x8E:
            self.ACL()
        elif opcode == 0x04:
            self.ADI()
        elif opcode == 0x8F:
            self.ACM()
        elif opcode == 0x87:
            self.ADM()
        elif opcode == 0x0C:
            self.ACI()
        elif opcode == 0x98:
            self.SBA()
        elif opcode == 0x90:
            self.SUA()
        elif opcode == 0x99:
            self.SBB()
        elif opcode == 0x91:
            self.SUB()
        elif opcode == 0x9A:
            self.SBC()
        elif opcode == 0x92:
            self.SUC()
        elif opcode == 0x9B:
            self.SBD()
        elif opcode == 0x93:
            self.SUD()
        elif opcode == 0x9C:
            self.SBE()
        elif opcode == 0x94:
            self.SUE()
        elif opcode == 0x9D:
            self.SBH()
        elif opcode == 0x95:
            self.SUH()
        elif opcode == 0x9E:
            self.SBL()
        elif opcode == 0x96:
            self.SUL()
        elif opcode == 0x14:
            self.SUI()
        elif opcode == 0x1C:
            self.SBI()
        elif opcode == 0x9F:
            self.SBM()
        elif opcode == 0x97:
            self.SUM()
        elif opcode == 0xA0:
            self.NDA()
        elif opcode == 0xA1:
            self.NDB()
        elif opcode == 0xA2:
            self.NDC()
        elif opcode == 0xA3:
            self.NDD()
        elif opcode == 0xA4:
            self.NDE()
        elif opcode == 0xA5:
            self.NDH()
        elif opcode == 0xA6:
            self.NDL()
        elif opcode == 0x24:
            self.NDI()
        elif opcode == 0xA7:
            self.NDM()
        elif opcode == 0xA8:
            self.XRA()
        elif opcode == 0xA9:
            self.XRB()
        elif opcode == 0xAA:
            self.XRC()
        elif opcode == 0xAB:
            self.XRD()
        elif opcode == 0xAC:
            self.XRE()
        elif opcode == 0xAD:
            self.XRH()
        elif opcode == 0xAE:
            self.XRL()
        elif opcode == 0x2C:
            self.XRI()
        elif opcode == 0xAF:
            self.XRM()
        elif opcode == 0xB0:
            self.ORA()
        elif opcode == 0xB1:
            self.ORB()
        elif opcode == 0xB2:
            self.ORC()
        elif opcode == 0xB3:
            self.ORD()
        elif opcode == 0xB4:
            self.ORE()
        elif opcode == 0xB5:
            self.ORH()
        elif opcode == 0xB6:
            self.ORL()
        elif opcode == 0x34:
            self.ORI()
        elif opcode == 0xB7:
            self.ORM()
        elif opcode == 0xB8:
            self.CPA()
        elif opcode == 0xB9:
            self.CPB()
        elif opcode == 0xBA:
            self.CPC()
        elif opcode == 0xBB:
            self.CPD()
        elif opcode == 0xBC:
            self.CPE()
        elif opcode == 0xBD:
            self.CPH()
        elif opcode == 0xBE:
            self.CPL()
        elif opcode == 0x3C:
            self.CPI()
        elif opcode == 0xBF:
            self.CPM()
        elif opcode == 0x08:
            self.INB()
        elif opcode == 0x10:
            self.INC()
        elif opcode == 0x18:
            self.IND()
        elif opcode == 0x20:
            self.INE()
        elif opcode == 0x28:
            self.ICH()
        elif opcode == 0x30:
            self.INL()
        elif opcode == 0x09:
            self.DCB()
        elif opcode == 0x11:
            self.DCC()
        elif opcode == 0x19:
            self.DCD()
        elif opcode == 0x21:
            self.DCE()
        elif opcode == 0x29:
            self.DCH()
        elif opcode == 0x31:
            self.DCL()

        #                               Rotate
        elif opcode == 0x12:
            self.RAL()
        elif opcode == 0x02:
            self.RLC()
        elif opcode == 0x1A:
            self.RAR()
        elif opcode == 0x0A:
            self.RRC()

        #                               Unimplemented
        elif opcode == 0x22:
            pass
        elif opcode == 0x2A:
            pass
        elif opcode == 0x32:
            pass
        elif opcode == 0x38:
            pass
        elif opcode == 0x39:
            pass
        elif opcode == 0x3A:
            pass

    def getOpcode(self):  # Читаем из шины данных
        opcode = self.motherBoard.nextbyte()
        return opcode

    def getOperand(self):  # 2-ой байт
        operand = self.motherBoard.nextbyte()
        return operand

    def getHighAddress(self):  # 3-ий байт
        highAddress = mask(self.motherBoard.nextbyte(), 0b00_111_111, 0)
        return highAddress

    def getAddress(self):  # получение полного адреса из памяти
        address = self.getOperand() + (self.getHighAddress() << 8)
        return address

    def startUpTest(self):
        while True:
            try:
                insTest = self.motherBoard.nextbyteTest()
            except IndexError:
                print("STOP REACHED")
                break
            print(f"EX: {hex(insTest)}", end=" ")
            self.instruction(inTest1)
            print(f"REG: A:{self.A} B:{self.B} C:{self.C} "
                  f"D:{self.D} E:{self.E} H:{self.H} L:{self.L} M:{self.M}")
        print(f"\nRESULT:{self.A}")

    def startUp(self):
        while True:
            try:
                ins = self.motherBoard.nextbyte()
            except IndexError:
                print("STOP REACHED")
                break
            print(f"EX: {hex(ins)}", end=" ")
            self.instruction(ins)
            print(f"REG: A:{self.A} B:{self.B} C:{self.C} "
                  f"D:{self.D} E:{self.E} H:{self.H} L:{self.L} M:{self.M}")
        print(f"\nRESULT:{self.A}")

    # region Instructions

    # CPU Control
    def HLT(self):
        self.motherBoard.instructionStreamOffset = \
            pc_add(self.motherBoard.instructionStreamOffset, 2)
        self.stack[self.stack_] = self.motherBoard.instructionStreamOffset

    # Input
    def INP(self):
        port = mask(self.getOpcode(), 0b00_001_110, 0)
        self.A = port
        self.motherBoard.instructionStreamOffset =\
            pc_add(self.motherBoard.instructionStreamOffset, 2)

    # Output
    def OUT(self):
        if mask(self.getOpcode(), 0b00_110_000) != 0:
            port = mask(self.getOpcode(), 0b00_111_110, 0)
            port += self.A
        self.motherBoard.instructionStreamOffset =\
            pc_add(self.motherBoard.instructionStreamOffset, 2)

    # Jump
    def JMP(self):
        self.motherBoard.instructionStreamOffset = self.getAddress()

    def JFC(self):
        self.motherBoard.instructionStreamOffset = self.getAddress()

    def JTC(self):
        self.motherBoard.instructionStreamOffset = self.getAddress()

    def JTP(self):
        self.motherBoard.instructionStreamOffset = self.getAddress()

    def JFP(self):
        self.motherBoard.instructionStreamOffset = self.getAddress()

    def JFS(self):
        self.motherBoard.instructionStreamOffset = self.getAddress()

    def JTS(self):
        self.motherBoard.instructionStreamOffset = self.getAddress()

    def JFZ(self):
        self.motherBoard.instructionStreamOffset = self.getAddress()

    def JTZ(self):
        self.motherBoard.instructionStreamOffset = self.getAddress()

    # Call
    def CAL(self):
        self.stack.append(self.motherBoard.instructionStreamOffset)
        self.motherBoard.instructionStreamOffset = self.getAddress()

    def CFC(self):
        self.stack.append(self.motherBoard.instructionStreamOffset)
        self.motherBoard.instructionStreamOffset = self.getAddress()

    def CTC(self):
        self.stack.append(self.motherBoard.instructionStreamOffset)
        self.motherBoard.instructionStreamOffset = self.getAddress()

    def CTP(self):
        self.stack.append(self.motherBoard.instructionStreamOffset)
        self.motherBoard.instructionStreamOffset = self.getAddress()

    def CFP(self):
        self.stack.append(self.motherBoard.instructionStreamOffset)
        self.motherBoard.instructionStreamOffset = self.getAddress()

    def CFS(self):
        self.stack.append(self.motherBoard.instructionStreamOffset)
        self.motherBoard.instructionStreamOffset = self.getAddress()

    def CTS(self):
        self.stack.append(self.motherBoard.instructionStreamOffset)
        self.motherBoard.instructionStreamOffset = self.getAddress()

    def CFZ(self):
        self.stack.append(self.motherBoard.instructionStreamOffset)
        self.motherBoard.instructionStreamOffset = self.getAddress()

    def CTZ(self):
        self.stack.append(self.motherBoard.instructionStreamOffset)
        self.motherBoard.instructionStreamOffset = self.getAddress()

    # Return
    def RET(self):
        self.A = self.memory.read(self.SP)
        self.SP += 2

    def RFC(self):
        self.A = self.memory.read(self.SP)
        self.SP += 2

    def RTC(self):
        self.A = self.memory.read(self.SP)
        self.SP += 2

    def RTP(self):
        self.A = self.memory.read(self.SP)
        self.SP += 2

    def RFP(self):
        self.A = self.memory.read(self.SP)
        self.SP += 2

    def RFS(self):
        self.A = self.memory.read(self.SP)
        self.SP += 2

    def RTS(self):
        self.A = self.memory.read(self.SP)
        self.SP += 2

    def RFZ(self):
        self.A = self.memory.read(self.SP)
        self.SP += 2

    def RTZ(self):
        self.A = self.memory.read(self.SP)
        self.SP += 2

    def RST(self):
        self.SP -= 2
        self.memory.write(self.SP, self.A)
        self.motherBoard.instructionStreamOffset = \
            pc_add(self.motherBoard.instructionStreamOffset, 2)

    # Load
    def LAI(self):
        self.motherBoard.instructionStreamOffset =\
            pc_add(self.motherBoard.instructionStreamOffset, 2)
        self.A = self.getOperand()

    def LAA(self):
        self.motherBoard.instructionStreamOffset =\
            pc_add(self.motherBoard.instructionStreamOffset, 2)
        self.A = self.A

    def LAB(self):
        self.motherBoard.instructionStreamOffset =\
            pc_add(self.motherBoard.instructionStreamOffset, 2)
        self.A = self.B

    def LAC(self):
        self.motherBoard.instructionStreamOffset =\
            pc_add(self.motherBoard.instructionStreamOffset, 2)
        self.A = self.С

    def LAD(self):
        self.motherBoard.instructionStreamOffset =\
            pc_add(self.motherBoard.instructionStreamOffset, 2)
        self.A = self.D

    def LAE(self):
        self.motherBoard.instructionStreamOffset =\
            pc_add(self.motherBoard.instructionStreamOffset, 2)
        self.A = self.E

    def LAH(self):
        self.motherBoard.instructionStreamOffset =\
            pc_add(self.motherBoard.instructionStreamOffset, 2)
        self.A = self.H

    def LAL(self):
        self.motherBoard.instructionStreamOffset =\
            pc_add(self.motherBoard.instructionStreamOffset, 2)
        self.A = self.L

    def LAM(self):
        self.motherBoard.instructionStreamOffset =\
            pc_add(self.motherBoard.instructionStreamOffset, 2)
        self.A = self.M

    def LBI(self):
        self.motherBoard.instructionStreamOffset =\
            pc_add(self.motherBoard.instructionStreamOffset, 2)
        self.B = self.getOperand()

    def LBA(self):
        self.motherBoard.instructionStreamOffset =\
            pc_add(self.motherBoard.instructionStreamOffset, 2)
        self.B = self.A

    def LBB(self):
        self.motherBoard.instructionStreamOffset =\
            pc_add(self.motherBoard.instructionStreamOffset, 2)
        self.B = self.B

    def LBC(self):
        self.motherBoard.instructionStreamOffset =\
            pc_add(self.motherBoard.instructionStreamOffset, 2)
        self.B = self.C

    def LBD(self):
        self.motherBoard.instructionStreamOffset =\
            pc_add(self.motherBoard.instructionStreamOffset, 2)
        self.B = self.D

    def LBE(self):
        self.motherBoard.instructionStreamOffset =\
            pc_add(self.motherBoard.instructionStreamOffset, 2)
        self.B = self.E

    def LBH(self):
        self.motherBoard.instructionStreamOffset =\
            pc_add(self.motherBoard.instructionStreamOffset, 2)
        self.B = self.H

    def LBL(self):
        self.motherBoard.instructionStreamOffset =\
            pc_add(self.motherBoard.instructionStreamOffset, 2)
        self.B = self.L

    def LBM(self):
        self.motherBoard.instructionStreamOffset =\
            pc_add(self.motherBoard.instructionStreamOffset, 2)
        self.B = self.M

    def LCI(self):
        self.motherBoard.instructionStreamOffset =\
            pc_add(self.motherBoard.instructionStreamOffset, 2)
        self.C = self.getOperand()

    def LCA(self):
        self.motherBoard.instructionStreamOffset =\
            pc_add(self.motherBoard.instructionStreamOffset, 2)
        self.C = self.A

    def LCB(self):
        self.motherBoard.instructionStreamOffset =\
            pc_add(self.motherBoard.instructionStreamOffset, 2)
        self.C = self.B

    def LCC(self):
        self.motherBoard.instructionStreamOffset =\
            pc_add(self.motherBoard.instructionStreamOffset, 2)
        self.C = self.C

    def LCD(self):
        self.motherBoard.instructionStreamOffset =\
            pc_add(self.motherBoard.instructionStreamOffset, 2)
        self.C = self.D

    def LCE(self):
        self.motherBoard.instructionStreamOffset =\
            pc_add(self.motherBoard.instructionStreamOffset, 2)
        self.C = self.E

    def LCH(self):
        self.motherBoard.instructionStreamOffset =\
            pc_add(self.motherBoard.instructionStreamOffset, 2)
        self.C = self.H

    def LCL(self):
        self.motherBoard.instructionStreamOffset =\
            pc_add(self.motherBoard.instructionStreamOffset, 2)
        self.C = self.L

    def LCM(self):
        self.motherBoard.instructionStreamOffset =\
            pc_add(self.motherBoard.instructionStreamOffset, 2)
        self.C = self.M

    def LDI(self):
        self.motherBoard.instructionStreamOffset =\
            pc_add(self.motherBoard.instructionStreamOffset, 2)
        self.D = self.getOperand()

    def LDA(self):
        self.motherBoard.instructionStreamOffset =\
            pc_add(self.motherBoard.instructionStreamOffset, 2)
        self.D = self.A

    def LDB(self):
        self.motherBoard.instructionStreamOffset =\
            pc_add(self.motherBoard.instructionStreamOffset, 2)
        self.D = self.B

    def LDC(self):
        self.motherBoard.instructionStreamOffset =\
            pc_add(self.motherBoard.instructionStreamOffset, 2)
        self.D = self.C

    def LDD(self):
        self.motherBoard.instructionStreamOffset =\
            pc_add(self.motherBoard.instructionStreamOffset, 2)
        self.D = self.D

    def LDE(self):
        self.motherBoard.instructionStreamOffset =\
            pc_add(self.motherBoard.instructionStreamOffset, 2)
        self.D = self.E

    def LDH(self):
        self.motherBoard.instructionStreamOffset =\
            pc_add(self.motherBoard.instructionStreamOffset, 2)
        self.D = self.H

    def LDL(self):
        self.motherBoard.instructionStreamOffset =\
            pc_add(self.motherBoard.instructionStreamOffset, 2)
        self.D = self.L

    def LDM(self):
        self.motherBoard.instructionStreamOffset =\
            pc_add(self.motherBoard.instructionStreamOffset, 2)
        self.D = self.M

    def LEI(self):
        self.motherBoard.instructionStreamOffset =\
            pc_add(self.motherBoard.instructionStreamOffset, 2)
        self.E = self.getOperand()

    def LEA(self):
        self.motherBoard.instructionStreamOffset =\
            pc_add(self.motherBoard.instructionStreamOffset, 2)
        self.E = self.A

    def LEB(self):
        self.motherBoard.instructionStreamOffset =\
            pc_add(self.motherBoard.instructionStreamOffset, 2)
        self.E = self.B

    def LEC(self):
        self.motherBoard.instructionStreamOffset =\
            pc_add(self.motherBoard.instructionStreamOffset, 2)
        self.E = self.C

    def LED(self):
        self.motherBoard.instructionStreamOffset =\
            pc_add(self.motherBoard.instructionStreamOffset, 2)
        self.E = self.D

    def LEE(self):
        self.motherBoard.instructionStreamOffset =\
            pc_add(self.motherBoard.instructionStreamOffset, 2)
        self.E = self.E

    def LEH(self):
        self.motherBoard.instructionStreamOffset =\
            pc_add(self.motherBoard.instructionStreamOffset, 2)
        self.E = self.H

    def LEL(self):
        self.motherBoard.instructionStreamOffset =\
            pc_add(self.motherBoard.instructionStreamOffset, 2)
        self.E = self.L

    def LEM(self):
        self.motherBoard.instructionStreamOffset =\
            pc_add(self.motherBoard.instructionStreamOffset, 2)
        self.E = self.M

    def LHI(self):
        self.motherBoard.instructionStreamOffset =\
            pc_add(self.motherBoard.instructionStreamOffset, 2)
        self.H = self.getOperand()

    def LHA(self):
        self.motherBoard.instructionStreamOffset =\
            pc_add(self.motherBoard.instructionStreamOffset, 2)
        self.H = self.A

    def LHB(self):
        self.motherBoard.instructionStreamOffset =\
            pc_add(self.motherBoard.instructionStreamOffset, 2)
        self.H = self.B

    def LHC(self):
        self.motherBoard.instructionStreamOffset =\
            pc_add(self.motherBoard.instructionStreamOffset, 2)
        self.H = self.C

    def LHD(self):
        self.motherBoard.instructionStreamOffset =\
            pc_add(self.motherBoard.instructionStreamOffset, 2)
        self.H = self.D

    def LHE(self):
        self.motherBoard.instructionStreamOffset =\
            pc_add(self.motherBoard.instructionStreamOffset, 2)
        self.H = self.E

    def LHH(self):
        self.motherBoard.instructionStreamOffset =\
            pc_add(self.motherBoard.instructionStreamOffset, 2)
        self.H = self.H

    def LHL(self):
        self.motherBoard.instructionStreamOffset =\
            pc_add(self.motherBoard.instructionStreamOffset, 2)
        self.H = self.L

    def LHM(self):
        self.motherBoard.instructionStreamOffset =\
            pc_add(self.motherBoard.instructionStreamOffset, 2)
        self.H = self.M

    def LLI(self):
        self.motherBoard.instructionStreamOffset =\
            pc_add(self.motherBoard.instructionStreamOffset, 2)
        self.L = self.getOperand()

    def LLA(self):
        self.motherBoard.instructionStreamOffset =\
            pc_add(self.motherBoard.instructionStreamOffset, 2)
        self.L = self.A

    def LLB(self):
        self.motherBoard.instructionStreamOffset =\
            pc_add(self.motherBoard.instructionStreamOffset, 2)
        self.L = self.B

    def LLC(self):
        self.motherBoard.instructionStreamOffset =\
            pc_add(self.motherBoard.instructionStreamOffset, 2)
        self.L = self.C

    def LLD(self):
        self.motherBoard.instructionStreamOffset =\
            pc_add(self.motherBoard.instructionStreamOffset, 2)
        self.L = self.D

    def LLE(self):
        self.motherBoard.instructionStreamOffset =\
            pc_add(self.motherBoard.instructionStreamOffset, 2)
        self.L = self.E

    def LLH(self):
        self.motherBoard.instructionStreamOffset =\
            pc_add(self.motherBoard.instructionStreamOffset, 2)
        self.L = self.H

    def LLL(self):
        self.motherBoard.instructionStreamOffset =\
            pc_add(self.motherBoard.instructionStreamOffset, 2)
        self.L = self.L

    def LLM(self):
        self.motherBoard.instructionStreamOffset =\
            pc_add(self.motherBoard.instructionStreamOffset, 2)
        self.L = self.M

    def LMI(self):
        self.motherBoard.instructionStreamOffset =\
            pc_add(self.motherBoard.instructionStreamOffset, 2)
        self.M = self.getOperand()

    def LMA(self):
        self.motherBoard.instructionStreamOffset =\
            pc_add(self.motherBoard.instructionStreamOffset, 2)
        self.M = self.A

    def LMB(self):
        self.motherBoard.instructionStreamOffset =\
            pc_add(self.motherBoard.instructionStreamOffset, 2)
        self.M = self.B

    def LMC(self):
        self.motherBoard.instructionStreamOffset =\
            pc_add(self.motherBoard.instructionStreamOffset, 2)
        self.M = self.C

    def LMD(self):
        self.motherBoard.instructionStreamOffset =\
            pc_add(self.motherBoard.instructionStreamOffset, 2)
        self.M = self.D

    def LME(self):
        self.motherBoard.instructionStreamOffset =\
            pc_add(self.motherBoard.instructionStreamOffset, 2)
        self.M = self.E

    def LMH(self):
        self.motherBoard.instructionStreamOffset =\
            pc_add(self.motherBoard.instructionStreamOffset, 2)
        self.M = self.H

    def LML(self):
        self.motherBoard.instructionStreamOffset =\
            pc_add(self.motherBoard.instructionStreamOffset, 2)
        self.M = self.L

    # Arithmetic
    def ACA(self):
        A = self.A + self.carry
        self.A = self.A + A
        self.sign = (1 if (self.A >= 128) else 0)
        self.motherBoard.instructionStreamOffset =\
            pc_add(self.motherBoard.instructionStreamOffset, 1)

    def ADA(self):
        self.A = self.A + self.A
        self.sign = (1 if (self.A >= 128) else 0)
        self.motherBoard.instructionStreamOffset =\
            pc_add(self.motherBoard.instructionStreamOffset, 1)

    def ACB(self):
        B = self.B + self.carry
        self.A = self.A + B
        self.sign = (1 if (self.A >= 128) else 0)
        self.motherBoard.instructionStreamOffset =\
            pc_add(self.motherBoard.instructionStreamOffset, 1)

    def ADB(self):
        self.A = self.A + self.B
        self.sign = (1 if (self.A >= 128) else 0)
        self.motherBoard.instructionStreamOffset =\
            pc_add(self.motherBoard.instructionStreamOffset, 1)

    def ACC(self):
        C = self.C + self.carry
        self.A = self.A + C
        self.sign = (1 if (self.A >= 128) else 0)
        self.motherBoard.instructionStreamOffset =\
            pc_add(self.motherBoard.instructionStreamOffset, 1)

    def ADC(self):
        self.A = self.A + self.C
        self.sign = (1 if (self.A >= 128) else 0)
        self.motherBoard.instructionStreamOffset =\
            pc_add(self.motherBoard.instructionStreamOffset, 1)

    def ACD(self):
        D = self.D + self.carry
        self.A = self.A + D
        self.sign = (1 if (self.A >= 128) else 0)
        self.motherBoard.instructionStreamOffset =\
            pc_add(self.motherBoard.instructionStreamOffset, 1)

    def ADD(self):
        self.A = self.A + self.D
        self.sign = (1 if (self.A >= 128) else 0)
        self.motherBoard.instructionStreamOffset =\
            pc_add(self.motherBoard.instructionStreamOffset, 1)

    def ACE(self):
        E = self.E + self.carry
        self.A = self.A + E
        self.sign = (1 if (self.A >= 128) else 0)
        self.motherBoard.instructionStreamOffset =\
            pc_add(self.motherBoard.instructionStreamOffset, 1)

    def ADE(self):
        self.A = self.A + self.E
        self.sign = (1 if (self.A >= 128) else 0)
        self.motherBoard.instructionStreamOffset =\
            pc_add(self.motherBoard.instructionStreamOffset, 1)

    def ACH(self):
        H = self.H + self.carry
        self.A = self.A + H
        self.sign = (1 if (self.A >= 128) else 0)
        self.motherBoard.instructionStreamOffset =\
            pc_add(self.motherBoard.instructionStreamOffset, 1)

    def ADH(self):
        self.A = self.A + self.H
        self.sign = (1 if (self.A >= 128) else 0)
        self.motherBoard.instructionStreamOffset =\
            pc_add(self.motherBoard.instructionStreamOffset, 1)

    def ADL(self):
        self.A = self.A + self.L
        self.sign = (1 if (self.A >= 128) else 0)
        self.motherBoard.instructionStreamOffset =\
            pc_add(self.motherBoard.instructionStreamOffset, 1)

    def ACL(self):
        L = self.L + self.carry
        self.A = self.A + L
        self.sign = (1 if (self.A >= 128) else 0)
        self.motherBoard.instructionStreamOffset =\
            pc_add(self.motherBoard.instructionStreamOffset, 1)

    def ADI(self):
        self.A = self.A + self.getOperand()
        self.sign = (1 if (self.A >= 128) else 0)
        self.motherBoard.instructionStreamOffset =\
            pc_add(self.motherBoard.instructionStreamOffset, 1)

    def ACM(self):
        M = self.M + self.carry
        self.A = self.A + M
        self.sign = (1 if (self.A >= 128) else 0)
        self.motherBoard.instructionStreamOffset =\
            pc_add(self.motherBoard.instructionStreamOffset, 1)

    def ADM(self):
        self.A = self.A + self.M
        self.sign = (1 if (self.A >= 128) else 0)
        self.motherBoard.instructionStreamOffset =\
            pc_add(self.motherBoard.instructionStreamOffset, 1)

    def ACI(self):
        I = self.getOperand() + self.carry
        self.A = self.A + I
        self.sign = (1 if (self.A >= 128) else 0)
        self.motherBoard.instructionStreamOffset =\
            pc_add(self.motherBoard.instructionStreamOffset, 1)

    def SBA(self):
        B = self.A + self.carry
        self.A = self.A - B
        self.sign = (1 if (self.A >= 128) else 0)
        self.motherBoard.instructionStreamOffset =\
            pc_add(self.motherBoard.instructionStreamOffset, 1)

    def SUA(self):
        self.A = self.A - self.A
        self.sign = (1 if (self.A >= 128) else 0)
        self.motherBoard.instructionStreamOffset =\
            pc_add(self.motherBoard.instructionStreamOffset, 1)

    def SBB(self):
        B = self.B + self.carry
        self.A = self.A - B
        self.sign = (1 if (self.A >= 128) else 0)
        self.motherBoard.instructionStreamOffset =\
            pc_add(self.motherBoard.instructionStreamOffset, 1)

    def SUB(self):
        self.A = self.A - self.B
        self.sign = (1 if (self.A >= 128) else 0)
        self.motherBoard.instructionStreamOffset =\
            pc_add(self.motherBoard.instructionStreamOffset, 1)

    def SBC(self):
        C = self.C + self.carry
        self.A = self.A - C
        self.sign = (1 if (self.A >= 128) else 0)
        self.motherBoard.instructionStreamOffset =\
            pc_add(self.motherBoard.instructionStreamOffset, 1)

    def SUC(self):
        self.A = self.A - self.C
        self.sign = (1 if (self.A >= 128) else 0)
        self.motherBoard.instructionStreamOffset =\
            pc_add(self.motherBoard.instructionStreamOffset, 1)

    def SBD(self):
        D = self.D + self.carry
        self.A = self.A - D
        self.sign = (1 if (self.A >= 128) else 0)
        self.motherBoard.instructionStreamOffset =\
            pc_add(self.motherBoard.instructionStreamOffset, 1)

    def SUD(self):
        self.A = self.A - self.D
        self.sign = (1 if (self.A >= 128) else 0)
        self.motherBoard.instructionStreamOffset =\
            pc_add(self.motherBoard.instructionStreamOffset, 1)

    def SBE(self):
        E = self.E + self.carry
        self.A = self.A - E
        self.sign = (1 if (self.A >= 128) else 0)
        self.motherBoard.instructionStreamOffset =\
            pc_add(self.motherBoard.instructionStreamOffset, 1)

    def SUE(self):
        self.A = self.A - self.E
        self.sign = (1 if (self.A >= 128) else 0)
        self.motherBoard.instructionStreamOffset =\
            pc_add(self.motherBoard.instructionStreamOffset, 1)

    def SBH(self):
        H = self.H + self.carry
        self.A = self.A - H
        self.sign = (1 if (self.A >= 128) else 0)
        self.motherBoard.instructionStreamOffset =\
            pc_add(self.motherBoard.instructionStreamOffset, 1)

    def SUH(self):
        self.A = self.A - self.H
        self.sign = (1 if (self.A >= 128) else 0)
        self.motherBoard.instructionStreamOffset =\
            pc_add(self.motherBoard.instructionStreamOffset, 1)

    def SBL(self):
        L = self.L + self.carry
        self.A = self.A - L
        self.sign = (1 if (self.A >= 128) else 0)
        self.motherBoard.instructionStreamOffset =\
            pc_add(self.motherBoard.instructionStreamOffset, 1)

    def SUL(self):
        self.A = self.A - self.L
        self.sign = (1 if (self.A >= 128) else 0)
        self.motherBoard.instructionStreamOffset =\
            pc_add(self.motherBoard.instructionStreamOffset, 1)

    def SBI(self):
        I = self.getOperand() + self.carry
        self.A = self.A - I
        self.sign = (1 if (self.A >= 128) else 0)
        self.motherBoard.instructionStreamOffset =\
            pc_add(self.motherBoard.instructionStreamOffset, 1)

    def SUI(self):
        self.A = self.A - self.getOperand()
        self.sign = (1 if (self.A >= 128) else 0)
        self.motherBoard.instructionStreamOffset =\
            pc_add(self.motherBoard.instructionStreamOffset, 1)

    def SBM(self):
        M = self.M + self.carry
        self.A = self.A - M
        self.sign = (1 if (self.A >= 128) else 0)
        self.motherBoard.instructionStreamOffset =\
            pc_add(self.motherBoard.instructionStreamOffset, 1)

    def SUM(self):
        self.A = self.A - self.M
        self.sign = (1 if (self.A >= 128) else 0)
        self.motherBoard.instructionStreamOffset =\
            pc_add(self.motherBoard.instructionStreamOffset, 1)

    def NDA(self):
        self.A = self.A & self.A
        self.sign = (1 if (self.A >= 128) else 0)
        self.motherBoard.instructionStreamOffset =\
            pc_add(self.motherBoard.instructionStreamOffset, 1)

    def NDB(self):
        self.A = self.A & self.B
        self.sign = (1 if (self.A >= 128) else 0)
        self.motherBoard.instructionStreamOffset =\
            pc_add(self.motherBoard.instructionStreamOffset, 1)

    def NDC(self):
        self.A = self.A & self.C
        self.sign = (1 if (self.A >= 128) else 0)
        self.motherBoard.instructionStreamOffset =\
            pc_add(self.motherBoard.instructionStreamOffset, 1)

    def NDD(self):
        self.A = self.A & self.D
        self.sign = (1 if (self.A >= 128) else 0)
        self.motherBoard.instructionStreamOffset =\
            pc_add(self.motherBoard.instructionStreamOffset, 1)

    def NDE(self):
        self.A = self.A & self.E
        self.sign = (1 if (self.A >= 128) else 0)
        self.motherBoard.instructionStreamOffset =\
            pc_add(self.motherBoard.instructionStreamOffset, 1)

    def NDH(self):
        self.A = self.A & self.H
        self.sign = (1 if (self.A >= 128) else 0)
        self.motherBoard.instructionStreamOffset =\
            pc_add(self.motherBoard.instructionStreamOffset, 1)

    def NDL(self):
        self.A = self.A & self.L
        self.sign = (1 if (self.A >= 128) else 0)
        self.motherBoard.instructionStreamOffset =\
            pc_add(self.motherBoard.instructionStreamOffset, 1)

    def NDI(self):
        self.A = self.A & self.getOperand()
        self.sign = (1 if (self.A >= 128) else 0)
        self.motherBoard.instructionStreamOffset =\
            pc_add(self.motherBoard.instructionStreamOffset, 1)

    def NDM(self):
        self.A = self.A & self.M
        self.sign = (1 if (self.A >= 128) else 0)
        self.motherBoard.instructionStreamOffset =\
            pc_add(self.motherBoard.instructionStreamOffset, 1)

    def XRA(self):
        self.A = self.A ^ self.A
        self.sign = (1 if (self.A >= 128) else 0)
        self.motherBoard.instructionStreamOffset =\
            pc_add(self.motherBoard.instructionStreamOffset, 1)

    def XRB(self):
        self.A = self.A ^ self.B
        self.sign = (1 if (self.A >= 128) else 0)
        self.motherBoard.instructionStreamOffset =\
            pc_add(self.motherBoard.instructionStreamOffset, 1)

    def XRC(self):
        self.A = self.A ^ self.C
        self.sign = (1 if (self.A >= 128) else 0)
        self.motherBoard.instructionStreamOffset =\
            pc_add(self.motherBoard.instructionStreamOffset, 1)

    def XRD(self):
        self.A = self.A ^ self.D
        self.sign = (1 if (self.A >= 128) else 0)
        self.motherBoard.instructionStreamOffset =\
            pc_add(self.motherBoard.instructionStreamOffset, 1)

    def XRE(self):
        self.A = self.A ^ self.E
        self.sign = (1 if (self.A >= 128) else 0)
        self.motherBoard.instructionStreamOffset =\
            pc_add(self.motherBoard.instructionStreamOffset, 1)

    def XRH(self):
        self.A = self.A ^ self.H
        self.sign = (1 if (self.A >= 128) else 0)
        self.motherBoard.instructionStreamOffset =\
            pc_add(self.motherBoard.instructionStreamOffset, 1)

    def XRL(self):
        self.A = self.A ^ self.L
        self.sign = (1 if (self.A >= 128) else 0)
        self.motherBoard.instructionStreamOffset =\
            pc_add(self.motherBoard.instructionStreamOffset, 1)

    def XRI(self):
        self.A = self.A ^ self.getOperand()
        self.sign = (1 if (self.A >= 128) else 0)
        self.motherBoard.instructionStreamOffset =\
            pc_add(self.motherBoard.instructionStreamOffset, 1)

    def XRM(self):
        self.A = self.A ^ self.M
        self.sign = (1 if (self.A >= 128) else 0)
        self.motherBoard.instructionStreamOffset =\
            pc_add(self.motherBoard.instructionStreamOffset, 1)

    def ORA(self):
        self.A = self.A | self.A
        self.sign = (1 if (self.A >= 128) else 0)
        self.motherBoard.instructionStreamOffset =\
            pc_add(self.motherBoard.instructionStreamOffset, 1)

    def ORB(self):
        self.A = self.A | self.B
        self.sign = (1 if (self.A >= 128) else 0)
        self.motherBoard.instructionStreamOffset =\
            pc_add(self.motherBoard.instructionStreamOffset, 1)

    def ORC(self):
        self.A = self.A | self.C
        self.sign = (1 if (self.A >= 128) else 0)
        self.motherBoard.instructionStreamOffset =\
            pc_add(self.motherBoard.instructionStreamOffset, 1)

    def ORD(self):
        self.A = self.A | self.D
        self.sign = (1 if (self.A >= 128) else 0)
        self.motherBoard.instructionStreamOffset =\
            pc_add(self.motherBoard.instructionStreamOffset, 1)

    def ORE(self):
        self.A = self.A | self.E
        self.sign = (1 if (self.A >= 128) else 0)
        self.motherBoard.instructionStreamOffset =\
            pc_add(self.motherBoard.instructionStreamOffset, 1)

    def ORH(self):
        self.A = self.A | self.H
        self.sign = (1 if (self.A >= 128) else 0)
        self.motherBoard.instructionStreamOffset =\
            pc_add(self.motherBoard.instructionStreamOffset, 1)

    def ORL(self):
        self.A = self.A | self.L
        self.sign = (1 if (self.A >= 128) else 0)
        self.motherBoard.instructionStreamOffset =\
            pc_add(self.motherBoard.instructionStreamOffset, 1)

    def ORI(self):
        self.A = self.A | self.getOperand()
        self.sign = (1 if (self.A >= 128) else 0)
        self.motherBoard.instructionStreamOffset =\
            pc_add(self.motherBoard.instructionStreamOffset, 1)

    def ORM(self):
        self.A = self.A | self.M
        self.sign = (1 if (self.A >= 128) else 0)
        self.motherBoard.instructionStreamOffset =\
            pc_add(self.motherBoard.instructionStreamOffset, 1)

    def CPA(self):
        if (self.A == self.A):
            self.zero == 1
            self.sign = (1 if (self.A >= 128) else 0)
        elif (self.A < self.A):
            self.carry == 1
            self.sign = (1 if (self.A >= 128) else 0)
        self.motherBoard.instructionStreamOffset =\
            pc_add(self.motherBoard.instructionStreamOffset, 1)

    def CPB(self):
        if (self.A == self.B):
            self.zero = 1
            self.sign = (1 if (self.A >= 128) else 0)
        elif (self.A < self.B):
            self.carry = 1
            self.sign = (1 if (self.A >= 128) else 0)
        self.motherBoard.instructionStreamOffset =\
            pc_add(self.motherBoard.instructionStreamOffset, 1)

    def CPC(self):
        if (self.A == self.C):
            self.zero = 1
            self.sign = (1 if (self.A >= 128) else 0)
        elif (self.A < self.C):
            self.carry = 1
            self.sign = (1 if (self.A >= 128) else 0)
        self.motherBoard.instructionStreamOffset =\
            pc_add(self.motherBoard.instructionStreamOffset, 1)

    def CPD(self):
        if (self.A == self.D):
            self.zero = 1
            self.sign = (1 if (self.A >= 128) else 0)
        elif (self.A < self.D):
            self.carry = 1
            self.sign = (1 if (self.A >= 128) else 0)
        self.motherBoard.instructionStreamOffset =\
            pc_add(self.motherBoard.instructionStreamOffset, 1)

    def CPE(self):
        if (self.A == self.E):
            self.zero = 1
            self.sign = (1 if (self.A >= 128) else 0)
        elif (self.A < self.E):
            self.carry = 1
            self.sign = (1 if (self.A >= 128) else 0)
        self.motherBoard.instructionStreamOffset =\
            pc_add(self.motherBoard.instructionStreamOffset, 1)

    def CPH(self):
        if (self.A == self.H):
            self.zero = 1
            self.sign = (1 if (self.A >= 128) else 0)
        elif (self.A < self.H):
            self.carry = 1
            self.sign = (1 if (self.A >= 128) else 0)
        self.motherBoard.instructionStreamOffset =\
            pc_add(self.motherBoard.instructionStreamOffset, 1)

    def CPL(self):
        if (self.A == self.L):
            self.zero = 1
            self.sign = (1 if (self.A >= 128) else 0)
        elif (self.A < self.L):
            self.carry = 1
            self.sign = (1 if (self.A >= 128) else 0)
        self.motherBoard.instructionStreamOffset =\
            pc_add(self.motherBoard.instructionStreamOffset, 1)

    def CPI(self):
        if (self.A == self.getOperand()):
            self.zero = 1
            self.sign = (1 if (self.A >= 128) else 0)
        elif (self.A < self.getOperand()):
            self.carry = 1
            self.sign = (1 if (self.A >= 128) else 0)
        self.motherBoard.instructionStreamOffset =\
            pc_add(self.motherBoard.instructionStreamOffset, 1)

    def CPM(self):
        if (self.A == self.M):
            self.zero = 1
            self.sign = (1 if (self.A >= 128) else 0)
        elif (self.A < self.M):
            self.carry = 1
            self.sign = (1 if (self.A >= 128) else 0)
        self.motherBoard.instructionStreamOffset =\
            pc_add(self.motherBoard.instructionStreamOffset, 1)

    def INB(self):
        self.B += 1
        self.sign = (1 if (self.B >= 128) else 0)
        self.motherBoard.instructionStreamOffset =\
            pc_add(self.motherBoard.instructionStreamOffset, 1)

    def INC(self):
        self.C += 1
        self.sign = (1 if (self.C >= 128) else 0)
        self.motherBoard.instructionStreamOffset =\
            pc_add(self.motherBoard.instructionStreamOffset, 1)

    def IND(self):
        self.D += 1
        self.sign = (1 if (self.D >= 128) else 0)
        self.motherBoard.instructionStreamOffset =\
            pc_add(self.motherBoard.instructionStreamOffset, 1)

    def INE(self):
        self.E += 1
        self.sign = (1 if (self.E >= 128) else 0)
        self.motherBoard.instructionStreamOffset =\
            pc_add(self.motherBoard.instructionStreamOffset, 1)

    def ICH(self):
        self.H += 1
        self.sign = (1 if (self.H >= 128) else 0)
        self.motherBoard.instructionStreamOffset =\
            pc_add(self.motherBoard.instructionStreamOffset, 1)

    def INL(self):
        self.L += 1
        self.sign = (1 if (self.L >= 128) else 0)
        self.motherBoard.instructionStreamOffset =\
            pc_add(self.motherBoard.instructionStreamOffset, 1)

    def DCB(self):
        self.B -= 1
        self.sign = (1 if (self.B >= 128) else 0)
        self.motherBoard.instructionStreamOffset =\
            pc_add(self.motherBoard.instructionStreamOffset, 1)

    def DCC(self):
        self.C -= 1
        self.sign = (1 if (self.C >= 128) else 0)
        self.motherBoard.instructionStreamOffset =\
            pc_add(self.motherBoard.instructionStreamOffset, 1)

    def DCD(self):
        self.D -= 1
        self.sign = (1 if (self.D >= 128) else 0)
        self.motherBoard.instructionStreamOffset =\
            pc_add(self.motherBoard.instructionStreamOffset, 1)

    def DCE(self):
        self.E -= 1
        self.sign = (1 if (self.E >= 128) else 0)
        self.motherBoard.instructionStreamOffset =\
            pc_add(self.motherBoard.instructionStreamOffset, 1)

    def DCH(self):
        self.H -= 1
        self.sign = (1 if (self.H >= 128) else 0)
        self.motherBoard.instructionStreamOffset =\
            pc_add(self.motherBoard.instructionStreamOffset, 1)

    def DCL(self):
        self.L -= 1
        self.sign = (1 if (self.L >= 128) else 0)
        self.motherBoard.instructionStreamOffset =\
            pc_add(self.motherBoard.instructionStreamOffset, 1)

    # Rotate
    def RLC(self):
        self.A >> mask(self.carry, 0b00_000_001, 0)
        self.motherBoard.instructionStreamOffset =\
            pc_add(self.motherBoard.instructionStreamOffset, 1)

    def RRC(self):
        self.A << mask(self.carry, 0b10_000_000, 0)
        self.motherBoard.instructionStreamOffset =\
            pc_add(self.motherBoard.instructionStreamOffset, 1)

    def RAL(self):
        self.A >> self.carry
        self.motherBoard.instructionStreamOffset =\
            pc_add(self.motherBoard.instructionStreamOffset, 1)

    def RAR(self):
        self.A << self.carry
        self.motherBoard.instructionStreamOffset =\
            pc_add(self.motherBoard.instructionStreamOffset, 1)

    # endregion


def main():
    p = i8008()
    p.startUp()


if __name__ == '__main__':
    main()
