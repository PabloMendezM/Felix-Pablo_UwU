#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 10:24:20 2024

@author: felixboschke
"""

import numpy as np
import matplotlib.pyplot as plt

#Generate points at which the functions are evaluated
x = np.linspace(-1, 1, 100)


#Function that generates the first N Chebyshev polynomials using the definition of the 0th
#and 1st polynomial and afterwards the recursion relation for the n>=1 polynomials
def cheby(x,N):
    #matrix to save the polynomials evaluations
    A = np.zeros((N+1, len(x)))
    T_0 = np.full(len(x),1)
    T_1 = x
    
    A[0] = T_0
    A[1] = T_1
    for i in range(2,N+1):
        T_n=2*x*T_1-T_0
        A[i]=T_n
        T_0 = T_1
        T_1 = T_n
    return A

#Matrix for plotting the first five polynomials
A = cheby(x,4)

#Parameters for plotting
plt.rcParams['font.size'] = 13
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = 'computer modern roman'
plt.rcParams['font.weight'] = 'normal'
plt.rcParams['axes.labelsize'] = 'medium'
plt.rcParams['axes.labelweight'] = 'medium'
plt.rcParams['axes.linewidth'] = 1.3
plt.rcParams['lines.linewidth'] = 1.8
plt.grid()

for i in range(5):
    plt.plot(x, A[i])

plt.xlim(-1.1,1.1)
plt.xlabel(r"$x$")
plt.ylabel(r"$y$")
plt.legend([r"$T_0$",r"$T_1$",r"$T_2$",r"$T_3$", r"$T_4$"], loc = "lower right")
plt.title(r"Chebyshev polynomials $T_0$ to $T_4$")
plt.savefig("Cheby.pdf", dpi=1000)
    
    