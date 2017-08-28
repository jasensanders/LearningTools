import random
import math
import pylab

def hofdinger(atestvalue, Nsamples, epsilon, expectedProb):
    flag = False
    hof = 2*math.pow(math.e, (-2*math.pow(epsilon,2)*Nsamples))
    flag = abs(expectedProb -atestvalue) <= hof
    return flag, hof

def FlipSim():
    c1 = 0.0
    crand = 0.0
    cmin = 0.0
    for i in range(100000):
        it = Flips1000x10()
        c1 += it[0]
        crand += it[1]
        cmin += it[2]
        if(i%1000==0):
            print i
    v1 = c1/100000.00
    vrand = crand/100000.00
    vmin = cmin/100000.00
    return v1, vrand, vmin
        

def Flips1000x10():
    listKilo =[]
    for i in range(1000):
        listKilo.append(FlipCoin(10))
    c1 = listKilo[0]
    cRand = random.choice(listKilo)
    
    ##Find the min heads coin.
    cmin = listKilo[0]
    for i in listKilo:
        if(i<cmin):
            ##print i
            cmin = i
    
    return (c1, cRand, cmin)
    
    
    

def FlipCoin(n):
    random.seed()
    x = []
    y = ['h','t']
    for i in range(n):
        x.append(random.choice(y))
        
    return x.count('h')/float(n)
