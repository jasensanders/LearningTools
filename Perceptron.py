#!/usr/bin/python

import random

def perceptron_training (x1, y1, x2, y2, training_size):
    test_count = 100
    err = 0
    ##this makes a random data set in the form list of points [theX, theY, 1.0]
    train_ds = [[random.uniform (-1, 1),random.uniform (-1, 1), 1.0] for x in range (training_size)]
    ##This takes the training dataset and 2 x/y points passed in and generates a hypthesis function that solves for that data and returns the number of iterations it took to solve, and the weights derived
    iterations, perceptron = train (train_ds, x1, y1, x2, y2)
    ##This picks a point in the same space and tests the weights(Perceptron) against the target function 100 times. and counts the errors
    for t in range (test_count):
        test_p = [random.uniform (-1, 1),random.uniform (-1, 1), 1.0]
        function_out = actual_side (test_p, x1, y1, x2, y2)
        predict_out = predict_side (test_p, perceptron)
        if function_out != predict_out:
            err += 1
    return (iterations, float(err)/float(test_count))
## This finds the actual classification for a point from the target function(decribed as 2 points on the line (x1, y1, x2, y2))
## t is the test point described as a list where [theX, theY, 1]
def actual_side (t, x1, y1, x2, y2):
    res = ((x2 - x1) * (t[1] - y1)) - ((y2 - y1) * (t[0] - x1))
    if res >= 0:
        return 1
    else:
        return -1
    ##This runs the perceptron (Weights) against a test point outside the training data set
def predict_side (t, weights):
    s_prod = 0.0
    for i in range (len(weights)):
        s_prod += weights[i] * t[i]
    if s_prod >= 0:
        return 1
    else:
        return -1

def train (train_ds, x1, y1, x2, y2):
    convergence = False
    test_ds = []
    weights = [0.0, 0.0, 0.0]
    iterations = 0
    while not convergence:
        iterations += 1
        current_state = list()
        actual_out = list()
        for t in train_ds:
            function_out = actual_side (t, x1, y1, x2, y2)
            predict_out = predict_side (t, weights)
            current_state.append (abs (function_out - predict_out))
            actual_out.append (function_out)
        convergence = sum (current_state) == 0
        err = False
        k = random.randint (0, len(current_state) - 1)
        while not err and not convergence:
            if current_state[k] != 0:
                err = True
                for i in range (len (weights)):
                    weights[i] += actual_out[k] * train_ds[k][i]
            k = random.randint (0, len(current_state) - 1)
        convergence = not err
    return iterations, weights
