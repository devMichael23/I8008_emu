import Memory
import Compiler


class MotherBoard:
    def __init__(self):
        self.instructionstream = []
        self.compiler =\
            Compiler.Compiler(self.instructionstream)
        self.instructionStreamOffset = 0
        self.pcTest = 0
        self.pc = 0
        self.memory = Memory.Memory()
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

    def writeToData(self, data: int):
        if data > 255:
            raise ValueError("Only one byte at one time")
        self.pins["D0"] = (data & 0b00_000_001) >> 0
        self.pins["D1"] = (data & 0b00_000_010) >> 1
        self.pins["D2"] = (data & 0b00_000_100) >> 2
        self.pins["D3"] = (data & 0b00_001_000) >> 3
        self.pins["D4"] = (data & 0b00_010_000) >> 4
        self.pins["D5"] = (data & 0b00_100_000) >> 5
        self.pins["D6"] = (data & 0b01_000_000) >> 6
        self.pins["D7"] = (data & 0b10_000_000) >> 7

    def tick(self):
        if len(self.instructionstream) > self.pc:
            self.writeToData(self.instructionstream[self.pc])
            self.pc += 1
        return

    def nextbyte(self) -> int:
        self.pc += 1
        return self.instructionstream[self.pc - 1]

    def byteat(self, pc: int) -> int:
        return self.instructionstream[pc]

    def setPins(self, pins: dict):
        self.pins = pins


if __name__ == "__main__":
    m = MotherBoard()
