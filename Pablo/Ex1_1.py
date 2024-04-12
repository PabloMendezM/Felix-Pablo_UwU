#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 09:38:38 2024

@author: felixboschke
"""


import numpy as np
import random as rnd

#Initialize the seed for the random number generation
seed = 3517
rnd.seed(seed)

#Initialize a 6x6 matrix
size = 6
A=np.zeros((size,size))

#Fill matrix with random numbers
for i in range(size):
    for j in range(size):
        A[i][j] = rnd.uniform(-5.0,5.0)

print("The random entry matrix  A is:")
print(A)
print("\n")

#Initialize a vector for the maximum values of each column
max_column=np.zeros(6)

for i in range(size):
    max_column[i] = max(A[:,i])

print("Vector with maximum elements of each column:")
print(max_column, "\n")
#Initialize a vector for the maximum values of each row
max_row=np.zeros(6)

for i in range(size):
    max_row[i] = max(A[i])
    
print("Vector with maximum elements of each row:")
print(max_row, "\n")
    
#Find the maximum value of all matrix entries
max_val = max(max_column)

#Find the index of the maximum value in the matrix A
for i in range(size):
    for j in range(size):
        if A[i][j] == max_val:
            print("The maximum value is", max_val, "with indices", i, j, "\n")
            break


#Multiply both vectors
m = 0
for i in range(size):
    m += max_row[i]*max_column[i]

print("Scalar product of both vectors:")
print(m, "\n")

#Create second random matrix with same distribution
B=np.zeros((size,size))


#Fill matrix with random numbers
for i in range(size):
    for j in range(size):
        B[i][j] = rnd.uniform(-5.0,5.0)
        
print("Second random entry matrix B:")
print(B, "\n")


#Initialize matrices for multiplication
C = np.zeros((size,size))
D = np.zeros((size,size))

for i in range(size):
    for j in range(size):
        for k in range(size):
            C[i][j] += A[i][k]*B[k][j]

for i in range(size):
    for j in range(size):
        for k in range(size):
            D[i][j] += B[i][k]*A[k][j]
            
print("C=AB:")
print(C, "\n")

print("D=BA:")
print(D, "\n")

            
            


        








        
        




