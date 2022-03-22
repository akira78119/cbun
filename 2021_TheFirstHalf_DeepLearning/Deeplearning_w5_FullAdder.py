import numpy as np

def AND(x1, x2):
    x = np.array([x1,x2])
    w = np.array([0.5,0.5])
    b = -0.7
    tmp = np.sum(w*x) + b
    
    if tmp <= 0 :
        return 0
    else :
        return 1
    
def NAND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5])
    b = 0.7
    tmp = np.sum(w * x) + b

    if tmp <= 0:
        return 0
    else:
        return 1
    
def OR(x1, x2):
    x = np.array([x1,x2])
    w = np.array([0.5,0.5])
    b = -0.2
    tmp = np.sum(w*x) + b
    if tmp <= 0 :
        return 0
    else :
        return 1   
    
def XOR(x1, x2):
    s1 = NAND(x1,x2)
    s2 = OR(x1,x2)
    return AND(s1, s2)


def FullAdder(a,b,z):
    Sum = XOR(XOR(a,b),z)
    Carry = OR(AND(XOR(a,b),z),AND(a,b))
    result = np.array([Sum,Carry])
    return result

print('[a b z] = [s c]')
print('[0 0 0] =',FullAdder(0,0,0))
print('[0 0 1] =',FullAdder(0,0,1))
print('[0 1 0] =',FullAdder(0,1,0))
print('[0 1 1] =',FullAdder(0,1,1))
print('[1 0 0] =',FullAdder(1,0,0))
print('[1 0 1] =',FullAdder(1,0,1))
print('[1 1 0] =',FullAdder(1,1,0))
print('[1 1 1] =',FullAdder(1,1,1))