from numpy import uint16, uint8
from copy import deepcopy

progmemory = "path"

BYTE_SIZE = 8

OP_CODE_LENGTH = 6
ADR_CODE_LENGTH = 10

REG_ADR_LENGTH = 5
REG_COUNT = 8

RAM_CAPACITY = 16

FIRST_REG_ADDRESS = 224
SECOND_REG_ADDRESS = 7

REGISTER_A = 0
REGISTER_B = 1
REGISTER_C = 2
REGISTER_D = 3
REGISTER_E = 4
REGISTER_F = 5
REGISTER_G = 6
REGISTER_H = 7