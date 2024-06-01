from utils import *


def load_a(self, address_code):
    self.registers[REGISTER_A] = self.memory[address_code]

def load_b(self, address_code):
    
    self.registers[REGISTER_B] = self.memory[address_code]

def load_c(self, address_code):
    self.registers[REGISTER_C] = self.memory[address_code]

def load_d(self, address_code):
    self.registers[REGISTER_D] = self.memory[address_code]

def load_e(self, address_code):
    self.registers[REGISTER_E] = self.memory[address_code]

def load_f(self, address_code):
    self.registers[REGISTER_F] = self.memory[address_code]

def load_g(self, address_code):
    self.registers[REGISTER_G] = self.memory[address_code]

def load_h(self, address_code):
    self.registers[REGISTER_H] = self.memory[address_code]

def store_a(self, address_code):
    self.memory[address_code] = self.registers[REGISTER_A]

def store_b(self, address_code):
    self.memory[address_code] = self.registers[REGISTER_B]

def store_c(self, address_code):
    self.memory[address_code] = self.registers[REGISTER_C]

def store_d(self, address_code):
    self.memory[address_code] = self.registers[REGISTER_D]

def store_e(self, address_code):
    self.memory[address_code] = self.registers[REGISTER_E]

def store_f(self, address_code):
    self.memory[address_code] = self.registers[REGISTER_F]

def store_g(self, address_code):
    self.memory[address_code] = self.registers[REGISTER_G]

def store_h(self, address_code):
    self.memory[address_code] = self.registers[REGISTER_H]

def jump(self, address_code):
    self.instruction_index = address_code

def increment(self, address_code):
    address = (deepcopy(address_code) & SECOND_REG_ADDRESS)

    self.registers[address] += 1

def decrement(self, address_code):
    address = (deepcopy(address_code) & SECOND_REG_ADDRESS)

    self.registers[address] -= 1

def b_not(self, address_code):
    address = (deepcopy(address_code) & SECOND_REG_ADDRESS)

    self.registers[address] = ~self.registers[address]

def add(self, address_code):
    address_1 = (deepcopy(address_code) & FIRST_REG_ADDRESS) >> REG_ADR_LENGTH
    address_2 = deepcopy(address_code) & SECOND_REG_ADDRESS

    self.registers[address_2] = self.registers[address_1] + self.registers[address_2]

def subtract(self, address_code):
    address_1 = (deepcopy(address_code) & FIRST_REG_ADDRESS) >> REG_ADR_LENGTH
    address_2 = deepcopy(address_code) & SECOND_REG_ADDRESS

    self.registers[address_2] = self.registers[address_1] - self.registers[address_2]

def b_and(self, address_code):
    address_1 = (deepcopy(address_code) & FIRST_REG_ADDRESS) >> REG_ADR_LENGTH
    address_2 = deepcopy(address_code) & SECOND_REG_ADDRESS

    self.registers[address_2] = self.registers[address_1] & self.registers[address_2]

def b_or(self, address_code):
    address_1 = (deepcopy(address_code) & FIRST_REG_ADDRESS) >> REG_ADR_LENGTH
    address_2 = deepcopy(address_code) & SECOND_REG_ADDRESS

    self.registers[address_2] = self.registers[address_1] | self.registers[address_2]

def b_xor(self, address_code):
    address_1 = (deepcopy(address_code) & FIRST_REG_ADDRESS) >> REG_ADR_LENGTH
    address_2 = deepcopy(address_code) & SECOND_REG_ADDRESS

    self.registers[address_2] = (self.registers[address_1] | self.registers[address_2]) & ~(self.registers[address_1] & self.registers[address_2])

def b_nand(self, address_code):
    address_1 = (deepcopy(address_code) & FIRST_REG_ADDRESS) >> REG_ADR_LENGTH
    address_2 = deepcopy(address_code) & SECOND_REG_ADDRESS

    self.registers[address_2] = ~(self.registers[address_1] & self.registers[address_2])

def b_nor(self, address_code):
    address_1 = (deepcopy(address_code) & FIRST_REG_ADDRESS) >> REG_ADR_LENGTH
    address_2 = deepcopy(address_code) & SECOND_REG_ADDRESS

    self.registers[address_2] = ~(self.registers[address_1] | self.registers[address_2])

def b_xnor(self, address_code):
    address_1 = (deepcopy(address_code) & FIRST_REG_ADDRESS) >> REG_ADR_LENGTH
    address_2 = deepcopy(address_code) & SECOND_REG_ADDRESS

    self.registers[address_2] = ~((self.registers[address_1] | self.registers[address_2]) & ~(self.registers[address_1] & self.registers[address_2]))

def kill(self, address_code) :
    self.instruction_index = (2 ** 10)









instructions = [ load_a,
    load_b,
    load_c,
    load_d,
    load_e,
    load_f,
    load_g,
    load_h,
    store_a,
    store_b,
    store_c,
    store_d,
    store_e,
    store_f,
    store_g,
    store_h,
    jump,
    increment,
    decrement,
    b_not,
    add,
    subtract,
    b_and,
    b_or,
    b_xor,
    b_nand,
    b_nor,
    b_xnor,
    kill,
]