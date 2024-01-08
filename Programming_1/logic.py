# Logicgatter bauen

def AND(a: int, b: int) -> int:
    match((a, b)):
        case (0, 0): return 0
        case (0, 1): return 0
        case (1, 0): return 0
        case (1, 1): return 1
    
def OR(a: int, b: int) -> int:
    match((a, b)):
        case (0, 0): return 0
        case (0, 1): return 1
        case (1, 0): return 1
        case (1, 1): return 1

def NOT(a: int) -> int:
    return not a

def NAND(a: int, b: int) -> int:
    match((a, b)):
        case (0, 0): return 1
        case (0, 1): return 1
        case (1, 0): return 1
        case (1, 1): return 0
    
def XOR(a: int, b: int) -> int:
    match((a, b)):
        case (0, 0): return 0
        case (0, 1): return 1
        case (1, 0): return 1
        case (1, 1): return 0

print(AND(1,0))