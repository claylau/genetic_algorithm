from yacs.config import CfgNode as CN

# Config definition
_C = CN()

_C.POPULATION = CN()
_C.POPULATION.GENERATION = 300
_C.POPULATION.POP_SIZE = 100
_C.POPULATION.PC = 1.0
_C.POPULATION.CINDEX = 15
_C.POPULATION.PM = 1/7
_C.POPULATION.MINDEX = 20
_C.POPULATION.CROSS_POINTS = 1
_C.POPULATION.CODE_MODE = "real"
_C.POPULATION.LENGTHS = 1
