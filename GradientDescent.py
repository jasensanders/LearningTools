import math
import random
from decimal import *

def E(u,v):
    u = Decimal(u)
    v = Decimal(v)
    e = Decimal(math.e)
    t1 =u*e**v
    t2 = 2*v*e**-u
    t3 = (t1-t2)**2
    return t3

def pdervU(u,v):
    u = Decimal(u)
    v = Decimal(v)
    e = Decimal(math.e)
    t1 = (e**v + 2*v*(e**-u))
    t2 = (u*(e**v) - 2*v*(e**-u))
    t3 = 2*t1*t2
    return t3

def pdervV(u,v):
    u = Decimal(u)
    v = Decimal(v)
    e = Decimal(math.e)
    t1 = 2*(e**-2*u)
    t2 = (u*e**(u+v)) - 2
    t3 = (u*e**(u+v)) - 2*v
    t4 = t1*t2*t3
    return t4

def nextU(currentu, currentv, n):
    currentu = Decimal(currentu)
    currentv = Decimal(currentv)
    n = Decimal(n)
    t1 = currentu - pdervU(currentu, currentv)*n
    return t1

def nextV(currentu, currentv, n):
    currentu = Decimal(currentu)
    currentv = Decimal(currentv)
    n = Decimal(n)
    t1 = currentv - pdervV(currentu, currentv)*n
    return t1
def computeGD(startu, startv, n):
    ep = 10**-14
    u = Decimal(startu)
    v = Decimal(startv)
    n = Decimal(n)
    Er = E(u,v)
    count = 0
    while(Er>ep or count < 11):
        u1 = nextU(u,v,n)
        v1 = nextV(u,v,n)
        print Er, u1,v1
        u = u1
        v = v1
        count+=1
        Er = E(u,v)

    return (u,v), count, Er
