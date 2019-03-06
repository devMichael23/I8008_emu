class Memory:
    def __init__(self):
        self.__mem = []

    def write(self, address: int, value):
        """Записывает value по адресу address"""
        if address > 0x3FFF:
            raise MemoryError("Адресуются только 0x3FFF байт")
        if len(self.__mem) >= address:
            self.__mem[address] = value
        else:
            self.__mem += [None for _ in range(
                0, address + 1 - len(self.__mem))]
            self.__mem[address] = value

    def read(self, address):
        """Возвращает копию значения по адресу address"""
        if address > 0x3FFF:
            raise MemoryError("Адресуются только 0x3FFF байт")
        if len(self.__mem) >= address:
            return self.__mem[address]
        else:
            return None

    def firstEmpty(self):
        return len(self.__mem)

    def loadfs(self, path):
        """Загружает файл в бинарном режиме из файловой системы.
        Возвращает адрес начала записи и число занятых ячеек.
        По смещению 0 от начала хранится число занятых ячеек"""
        startIndex = self.firstEmpty()
        cellCounter = 0
        self.write(startIndex, 0)  # записываем фиктивный размер
        with open(path, mode="rb") as file:
            byteBuffer = True
            while byteBuffer:
                byteBuffer = file.read(1)
                self.write(startIndex + cellCounter + 1, ord(byteBuffer))
                cellCounter += 1
        return (startIndex, cellCounter)
