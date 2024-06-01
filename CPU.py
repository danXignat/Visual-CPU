from utils import*
from UnitAlgLog import*
from interface import *

def add_frame(self, opcode, address, first):
    memory_lines = [0 for _ in range(16)]
    register_lines = [0 for _ in range(8)]
    alu_lines = False
    instruction_index = self.instruction_index-1
    memory = deepcopy(self.memory)
    registers = deepcopy(self.registers)
    if first:
        memory_lines[instruction_index] = 1
        Movie.append(cadru(memory, registers, instruction_index, memory[instruction_index], memory_lines, register_lines, alu_lines))
        memory_lines = [0 for _ in range(16)]
        register_lines = [0 for _ in range(8)]

    if opcode < 16:
        memory_lines[address] = 1
        register_lines[opcode % 8] = 1

        Movie.append(cadru(memory, registers, instruction_index, memory[instruction_index], memory_lines, register_lines, alu_lines))

    elif opcode == 16:
        print(self.instruction_index)
        memory_lines[instruction_index] = 1
        Movie.append(cadru(memory, registers, instruction_index, memory[instruction_index], memory_lines, register_lines, alu_lines))

    elif opcode < 20:
        address_code = (deepcopy(address) & SECOND_REG_ADDRESS)

        register_lines[address_code] = 1

        if opcode == 19:
            alu_lines = True
        Movie.append(cadru(memory, registers, instruction_index, memory[instruction_index], memory_lines, register_lines, alu_lines))

    elif opcode < 28:
        alu_lines = True
        address_1 = (deepcopy(address) & FIRST_REG_ADDRESS) >> REG_ADR_LENGTH
        address_2 = deepcopy(address) & SECOND_REG_ADDRESS

        register_lines[address_1] = 1 
        register_lines[address_2] = 1
        Movie.append(cadru(memory, registers, instruction_index, memory[self.instruction_index], memory_lines, register_lines, alu_lines))

    else:
        if(self.instruction_index <= len(memory_lines)):
            memory_lines[instruction_index] = 1
        Movie.append(cadru(memory, registers, instruction_index, memory[self.instruction_index - 1], memory_lines, register_lines, alu_lines))

class CPU:
    def __init__(self) :
        self.registers = [uint16()] * REG_COUNT                   
        self.memory    = [uint16()] * (2 ** ADR_CODE_LENGTH)                                        
        self.instruction_index = 0                                    
    
    def fetch(self) :
        instruction = self.memory[self.instruction_index]
        self.instruction_index += 1
        
        return instruction
    
    def decode(self, instruction) :
        opcode  = (deepcopy(instruction) & 0xFC00) >> 10
        address = deepcopy(instruction) & 0x3FF
        
        return opcode, address
        
    def execute(self, opcode, address) :
        instructions[opcode](self, address)
        print(f"Executing {opcode} with address {address}")
    
    def run(self) :
        while (self.instruction_index < len(self.memory)) :
            instruction = self.fetch()
            opcode, address = self.decode(instruction)
    
            add_frame(self, opcode, address, True)

            self.execute(opcode, address)

            add_frame(self, opcode, address, False)
    
    def get_registers(self):
        return [int(reg.value, 2) for reg in self.registers]

    def get_memory(self):
        return [int(mem.value, 2) for mem in self.memory]

    def get_current_instruction(self):
        if self.instruction_index < len(self.memory):
            return int(self.memory[self.instruction_index].value, 2)
        return 0
    
    def get_instruction_index(self):
        return self.instruction_index