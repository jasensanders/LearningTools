import math
import random
from decimal import *

def insamE(N, s, d):
    t1 = s**2
    t2 = (d+1)/float(N)
    t3 = 1-t2
    t4 = t1*t3
    return t4

def devroy(N, d, dvc, ep):
    N = Decimal(N)
    d = Decimal(d)
    dvc = Decimal(dvc)
    ep = Decimal(ep)
    t1 = 1/2*N
    t2 = t1*(4*ep*(1+ep))
    t3 = Decimal.ln((4*((N**2)**dvc))/d)
    t4 = Decimal.sqrt(t2 + t3)
    return t4

def PVB(N, d, dvc, ep):
    N = Decimal(N)
    d = Decimal(d)
    dvc = Decimal(dvc)
    ep = Decimal(ep)
    t1 = 1/N
    t2 = (2*ep) + Decimal.ln((6*(2*N**dvc)/d))
    t3 = Decimal.sqrt(t1*t2)
    return t3

def radPen(N, d, dvc):
    N = Decimal(N)
    d = Decimal(d)
    dvc = Decimal(dvc)
    t1 = 2*Decimal.ln(2*N*(N**dvc))
    t2 = Decimal.sqrt(t1/N)
    t3 = (Decimal(2)/N * Decimal.ln(Decimal(1)/d)) + 1/N
    t4 = Decimal.sqrt(t3)
    return t2 + t4

def VCIapprox(epsilon, dvc, N):
    epsilon = Decimal(epsilon)
    N = Decimal(N)
    dvc = Decimal(dvc)
    Exp = Decimal(-0.125)*(epsilon**2)*N
    result = 4*(N**dvc)*Decimal(math.e)**Exp
    return result

def omShort(N, d, dvc):
    N = Decimal(N)
    d = Decimal(d)
    t1 =8/N
    t1 = Decimal(t1)
    mh = pow(2*N,dvc)
    mh = Decimal(mh)
    t2 = Decimal.ln(4*mh/d)
    t3= Decimal.sqrt(t1*t2)
    return t3

def omega(N, d, k):
    N = Decimal(N)
    d = Decimal(d)
    t1 =8/N
    t1 = Decimal(t1)
    mh = grow(2*N, k)
    mh = Decimal(mh)
    t2 = Decimal.ln(4*mh/d)
    t3= Decimal.sqrt(t1*t2)
    return t3


def VCInequality(epsilon, k, N):
    exp = -0.125*pow(epsilon,2)*N
    result = 4*grow(2*N,k)*pow(math.e,exp)
    return result

def grow(n,k):
    summ = Decimal(0.0)
    for i in range(k):
        summ += NchoK(n,i)
    return summ


def F(x):
    factors = []
    for i in range(1, x+1):
        factors.append(i)
    ans = 1
    for i in factors:
        ans *= i
    return ans

def NchoK(n, k):
    n = Decimal(n)
    k = Decimal(k)
    if(n<k): return Decimal(0.0)
    num = F(n)
    den = F(k)*F(n-k)
    ans = num/den
    return ans
    # This is me cross cancelling F(n)/F(k) leaving just F(n-k)
    # in the denominator and the numerator is whatever was left
    # from cross canceling. This keeps numbers lower and thus faster.
    ##    if(n >= k):
    ##        x = n
    ##        den = F(n-k)
    ##        num = float(n)
    ##        while(x>k+1):
    ##            num *= x-1
    ##            x -= 1
    ##        return num/den
    ##    else:
    ##        return 0
