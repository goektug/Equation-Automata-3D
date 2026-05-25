# Equation Automata 3D is developed by Goktug Islamoglu
# goktugislamoglu@gmail.com
#
# Equation Automata 3D uses
# PyCX 0.3 Realtime Visualization Template
##
# Written by:
# Chun Wong
# email@chunwong.net
##
# Revised by:
# Hiroki Sayama
# sayama@binghamton.edu
##
# Equation Automata 3D runs on the simulator package "pycxsimulator.py"
# Realtime Simulation GUI for PyCX
##
# Developed by:
# Chun Wong
# email@chunwong.net
##


import matplotlib
matplotlib.use('TkAgg')

from pylab import *
import numpy as np

L = 100  # size of space: LxL
#p = float(0.5 - (1 / (2 * sqrt(2))))
#p = 0.1464

#p = 1/(1+np.exp(-1/sqrt(2)))   # sigmoid of sigmoid of 2 * Ising critical temperature 
#p = 1/sqrt(2)                  # sigmoid of 2 * Ising critical temperature
#p = np.log(1 + sqrt(2)) / 2    # Ising critical temperature 

#p = 1/3
#p = 2/3

p = 6 / 27

#p = float(0.5 + (1 / (2 * sqrt(2))))
#p = 0.8536
#print p
print(p)
# initializing randomly assigned states with probability p


def init():
    global c, nc, slope0, slope1, delta, o
    c = zeros([L, L, L])
    for x in range(L):
        for y in range(L):
            for q in range(L):
                c[x, y, q] = 1 if random() < p else 0
    nc = zeros([L, L, L])
    o = 0
    slope0 = []
    slope1 = []
    delta = []

# visualizing the content of an array


def draw():
    cla()
    imshow(c[:, :, L//2])

# count of upper neighbors of a live cell's Moore neighborhood


def number_of_upper_neighbors(x, y, q):
    upper_count = 0
    for dx in range(-1, 2):
        for dq in range(-1, 2):
            upper_count += c[(x + dx) % L, (y + 1) % L, (q + dq) % L]
        # print upper_count
    return upper_count

# count of lower neighbors of a live cell's Moore neighborhood


def number_of_lower_neighbors(x, y, q):
    lower_count = 0
    for dx in range(-1, 2):
        for dq in range(-1, 2):
            lower_count += c[(x + dx) % L, (y - 1) % L, (q + dq) % L]
        # print lower_count
    return lower_count

# count of right neighbors of a live cell's Moore neighborhood


def number_of_right_neighbors(x, y, q):
    right_count = 0
    for dy in range(-1, 2):
        for dq in range(-1, 2):
            right_count += c[(x + 1) % L, (y + dy) % L, (q + dq) % L]
    return right_count

# count of left neighbors of a live cell's Moore neighborhood


def number_of_left_neighbors(x, y, q):
    left_count = 0
    for dy in range(-1, 2):
        for dq in range(-1, 2):
            left_count += c[(x - 1) % L, (y + dy) % L, (q + dq) % L]
        # print left_count
    return left_count

# count of von Neumann neighbors of a live cell


def number_of_Neumann_neighbors(x, y, q):
    return int(
        c[(x+1)%L, y, q] + c[(x-1)%L, y, q] +
        c[x, (y+1)%L, q] + c[x, (y-1)%L, q] +
        c[x, y, (q+1)%L] + c[x, y, (q-1)%L]
    )

# count of Moore neighbors of an alive cell


def number_of_Moore_neighbors(x, y, q):
    Moore_count = 0
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            for dq in range(-1, 2):
                Moore_count += c[(x + dx) % L, (y + dy) % L, (q + dq) % L]
            # print Moore_count
    return Moore_count - c[x, y, q]


def step():
    global c, nc, slope0, slope1, delta, o
    count0 = 0
    count1 = 0
    count = 0
    ratio1 = 0
    ratio = 0
    i = 0
    j = 0
    array0 = []
    array1 = []
    for x in range(L):
        for y in range(L):
            for q in range(L):
                g = number_of_Moore_neighbors(x, y, q)
                if c[x, y, q] == 0:
                    nc[x, y, q] = 0 if g <= 27 else 1
                    array0.append(c[x, y, q])
                elif c[x, y, q] == 1:
                    array1.append(c[x, y, q])
                    for z in range(-1, 2):
                        # block generation from randomly distributed points
                        m = number_of_upper_neighbors(x, y, q)
                        if m == 3:
                            nc[x, (y + 1) % L, q] = 1
                        n = number_of_lower_neighbors(x, y, q)
                        if n == 3:
                            nc[x, (y - 1) % L, q] = 1
    
                        k = number_of_right_neighbors(x, y, q)
                        if k == 3 and (m <= 3 or n <= 3):
                            nc[(x + 1) % L, (y + z) % L, q] = 1
    
                        l = number_of_left_neighbors(x, y, q)
                        if l == 3 and (m > 3 or n > 3):
                            nc[(x - 1) % L, (y + z) % L, q] = 0
    
                        h = number_of_Neumann_neighbors(x, y, q)
                        if h >= 4.5:
                            nc[x, y, q] = 1 if g <= 27 else 0
    
                        if g / 27 > (1-p) * p: 
                            nc[(x + 1) % L, y, q] = 1
                        elif g / 27 < (1-p) * p:
                            nc[(x - 1) % L, y, q] = 1
                        else:
                            nc[x, y, q] = 1
                i += 1
                j += g
    count0 = len(array0)
    # print count0
    count1 = len(array1)
    print(count1)
    o += 1
    #print o
    #print(j)
    if o == 1:
        # print count
        slope0.append(float(count0))
        slope1.append(float(count1))
        delta.append(float(j))
    elif o > 1:
        slope0.append(float(count0))
        # print slope0[o-1]
        # print slope0[o-2]
        slope1.append(float(count1))
        # print slope1[o-1]
        # print slope1[o-2]
        delta.append(float(j))
        # print delta[o-1]
        # print delta[o-2]
        ratio = count0 / float(count1)
        ratio0 = (j / i)
        ratio1 = ratio0 / ratio
        #print(ratio1)
        ratio2 = (slope0[o - 1] / float(slope1[o - 1])) - (slope0[o - 2] / float(slope1[o - 2]))
        ratio3 = (delta[o - 2] - delta[o - 1]) / i
        ratio4 = ratio2 * ratio0
        ratio5 = ratio3 * ratio

        if ratio1 != 1:
            print (ratio3 / float(ratio1 * ratio1) + (1 / float(ratio1)) - ratio2)
    c, nc = nc, c

import pycxsimulator
pycxsimulator.GUI(title='Simulator', interval=0,
                  parameterSetters=[]).start(func=[init, draw, step])
