import math
import random

def AVG(xlist):
    a = 0.0
    for i in xlist:
        a+=i
    return a/(len(xlist))


def SU(avg, value, SD):
    return (value-avg)/SD

def SUndo(avg, suValue, SD):
    return (suValue*SD) + avg


def SD(xlist):
    a = AVG(xlist)
    h = 0
    for i in xlist:
        h += math.pow((a - i), 2)
    l = h/(len(xlist))
    return math.sqrt(l)
def Var(xlist):
    return SD(xlist)**2


def R(xlist, ylist):
    ax = AVG(xlist)
    ay = AVG(ylist)
    sdx = SD(xlist)
    sdy = SD(ylist)
    suylist = []
    suxlist = []
    SUproducts = []
    for i in xlist:
        suxlist.append(SU(ax, i, sdx))
    for i in ylist:
        suylist.append(SU(ay, i, sdy))
    for i in range(len(xlist)):
        SUproducts.append(suxlist[i] * suylist[i])

    return AVG(SUproducts)

def RMSerror(r, SDy):
    return math.sqrt(1- math.pow(r, 2)) * SDy

def RegresLineEst(x, r, sdx, sdy, meanx, meany):
    slope = (r*sdy)/sdx
    intercept = meany - (slope*meanx)
    return slope*x + intercept

def addtoList(x, alist):
    for i in range(len(alist)):
        alist[i] += x
    return None


def F(x):
    factors = []
    for i in range(1, x+1):
        factors.append(i)
    ans = 1
    for i in factors:
        ans *= i
    return ans

def NchoK(n, k):
    ##    num = float(F(n))
    ##    den = F(k)*F(n-k)
    ##    ans = num/den
    ##    return ans
    # This is me cross cancelling F(n)/F(k) leaving just F(n-k)
    # in the denominator and the numerator is whatever was left
    # from cross canceling. This keeps numbers lower and thus faster. 
    x = n
    den = F(n-k)
    num = float(n)
    while(x>k+1):
        num *= x-1
        x -= 1
    return num/den

def binomial(n, p, k):
    a = NchoK(n, k)
    b = math.pow(p,k)
    c = math.pow(1-p, n-k)
    return a * b * c


def HyperGeo(N, G, n, g):
    num = NchoK(G,g) * NchoK(N-G, n-g)
    den = NchoK(N,n)
    return num/den

def RollDie(n):
    x =[]
    for i in range(n):
        x.append(random.randint(1,6))
    return x

def FlipCoin(n):
    x = []
    y = ['h','t']
    for i in range(n):
        x.append(random.choice(y))
    return (x, (x.count('h'), x.count('t')))

def eXlist(problist, valuesList):
    ex = 0
    for i in range(len(problist)):
        ex += (problist[i] * valuesList[i])
    return ex

def seXlist(problist, valuesList):
    ex = eX(problist, valuesList)
    total = 0.0
    for i in range(len(problist)):
        total += (math.pow(valuesList[i] - ex, 2) * problist[i])

    return math.sqrt(total)

def exSumDraws(boxList, numdraws):
    return AVG(boxList)*numdraws

def sexSumDraws(boxList, numdraws):
    return math.sqrt(float(numdraws)) * SD(boxList)

def exSum(avgORprob, draws):
    return avgORprob * float(draws)

def sexSum(numdraws, SDbox):
    return math.sqrt(float(numdraws)) * SDbox

def FinitePopCor(N, n):
    N = float(N)
    return math.sqrt((N-n)/(N-1))

def seM(SD, n):
    return float(SD)/math.sqrt(n)

def BinomialRange(n, p, GTEk=None , LTEk=None):
    gt = GTEk
    lt = LTEk
    ProbTotal = 0.0
    if (GTEk==None and LTEk == None):
        return None
    
    if (GTEk == LTEk):
        return binomial(n, p, GTEk)
    
    elif(LTEk==None):
        while(gt <= n):
            ProbTotal += binomial(n, p, gt)
            gt += 1
        return ProbTotal
    
    elif(GTEk==None):
        while(lt >= 0):
            ProbTotal += binomial(n, p, lt)
            lt -= 1
        return ProbTotal

    elif(GTEk > LTEk):
        probtop = 0.0
        probbottom = 0.0
        while(gt <= n):
            probtop += binomial(n, p, gt)
            gt +=1
        while(lt >= 0):
            probbottom += binomial(n, p, lt)
            lt -= 1
        ProbTotal = probtop + probbottom
        return ProbTotal

    elif(GTEk < LTEk):
        while(gt <= LTEk):
            ProbTotal += binomial(n, p, gt)
            gt += 1
        return ProbTotal


def SEDiffWithR(sdx, sdy, r):
    sdxs = math.pow(sdx, 2)
    sdys = math.pow(sdy, 2)
    correction = 2*r*sdx*sdy
    quot = (sdxs+sdys) -correction
    return math.sqrt(quot)

def DiffOfList(alist, blist):
    Result = []
    for i in range(len(alist)):
        Result.append(alist[i]-blist[i])
    return Result

def SDN1(xlist):
    a = AVG(xlist)
    h = 0
    for i in xlist:
        h += math.pow((a - i), 2)
    l = h/(len(xlist)-1)
    return math.sqrt(l)

def SDXSQ(DegOfFreedom):
    return math.sqrt(2*DegOfFreedom)
    
