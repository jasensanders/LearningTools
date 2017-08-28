import numpy as np
import random
import math
import os


def optest():
    
    inp = []
    outp = []
    fi = []
    '''read in the insample data'''
    os.chdir(r'E:\Desktop')
    infile = open('in.dta', "r")
    for line in infile:
         out = line.split()
         x = float(out[0])
         x2 = float(out[1])
         y = float(out[2])
         inp.append(([float(1),x,x2],y))
         fi.append(([float(1),x,x2,x**2,x2**2, x*x2, abs(x-x2), abs(x+x2)],y))
    infile.close()
    '''read in the outsample data'''
    outfile = open('out.dta', "r")
    for line in outfile:
        d = line.split()
        x = float(d[0])
        x2 = float(d[1])
        y = float(d[2])
        outp.append(([float(1),x,x2,x**2,x2**2, x*x2, abs(x-x2), abs(x+x2)],y))
    outfile.close()
    inpValid = fi[:25]
    inpTrain = fi[25:]
    k =[3,4,5,6,7]
    Results = []
    for i in k:
        ##Run Linear Regression after non-linear transformation
        wIn = linearRegressionTraining(inpTrain, i)
        
        ##Calculate in sample error
        wInE = calculateE(inpValid, i, wIn)
        ##Calculate out of sample error
        OutE = calculateE(outp, i, wIn)
        Results.append((i,wInE,OutE))
    
            
    return Results
            
def mt():
    m= [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
    mt = np.matrix(m)
    mtt = mt.transpose()
    mttm = np.dot(mtt,mt)
    return mttm
    
    
    
        


def Distance(x1,y1,x2,y2):
    t1 = pow(x1-x2, 2) + pow(y1-y2,2)
    t2 = math.sqrt(t1)
    return t2

#Define the h(x) value of a point for a given w
#return +1 or -1
def evaluateg(ex,w):
    r = sum(ex_i*w_i for ex_i,w_i in zip(ex,w))
    if r > 0:
        return 1
    elif r < 0:
        return -1

#Learning algorith of Linear Regression with regularization
#return weights w
def linearRegressionTrainingReg(N,L):
    #Separate the set of examples into X[][] and y[]
    X,y = zip(*N)
    #Calculate the pseudo-inverse Matrix of X, by using numpy
    X_d = np.matrix(X)
    Xdt =X_d.transpose()
    Xdtt = np.dot(X_d, Xdt)
    IM = Xdtt.shape[0]
    #Calculate lambda times the identity matrix and add that to X_d
    lam = np.multiply(L,np.identity(IM))
    XdttL = np.add(Xdtt, lam)
    XdttLI = np.linalg.inv(XdttL)
    PSinv = np.dot(Xdt, XdttLI)
    
    #Calculate the vector of weights w as multiplication of X_d and y
    w = np.dot(PSinv,y)
    w = w.tolist()
    
    return w[0]

#Learning algorith of Linear Regression
def linearRegressionTraining(N,transformLength):
    #adjust transformLength for index refrencing (add 1)
    transformLength += 1
    #Separate the set of examples into X[][] and y[]
    X,y = zip(*N)
    X1 = []
    #Set length of each X coordinate minimum 3 or default if transformLength == -1
    if(transformLength != -1 and transformLength >2):
        for i in range(len(X)):
            X1.append(X[i][:transformLength])
    
    #Calculate the pseudo-inverse Matrix of X1, by using numpy
    X_d = np.linalg.pinv(X1)
    #Calculate the vector of weights w as multiplication of X_d and y
    w = np.dot(X_d,y)
    
    return w

#Calculate the probability of getting a wrong classification
#return the probability of misclassification
def calculateE(points, transformLength, w):
    #Separate the set of examples into X[][] and y[]
    X,y = zip(*points)
    #adjust transformLength for index refrencing (add 1)
    transformLength += 1
    #Set length of each X coordinate minimum 3 or default if transformLength == -1
    X1 =[]
    if(transformLength != -1 and transformLength >2):
        for i in range(len(X)):
            X1.append(X[i][:transformLength])
    nWrong = 0
    #For every point, check if f(x) and h(x) values are egual
    for i in xrange(len(points)):
        if y[i] != evaluateg(X1[i],w):
            #Count the wrong classified cases
            nWrong += 1
    #misclassified points/ total number of points
    pWrong = float(nWrong) / len(points)
    return pWrong

def createExamples(nExamples, m, q):
    N = []
    for i in xrange(nExamples):
        #[artificial->1,x,y]
        x = [1,random.uniform(-1,1),random.uniform(-1,1)]
        #Set the label to +1 or -1
        if x[2] > (m*x[1]+q):
            label = 1
        else:
            label = -1
        #Insert the values into the list of examples
        N.append((x,label))
    return N
