# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 16:58:10 2023

@author: jbsousa
"""

def opn(n):
    import csv
    with open(n, newline = '') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        m = [row for row in spamreader]
        return m
m = opn('BIGGESTTEST.csv')
v = opn('VTEST.csv')
#v = [] #For vectors written in excel and downloaded as a csv
#with open('BIGGESTTEST.csv', newline = '') as csvfile:
#    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
#    v = [row for row in spamreader]


#Input a vector, v, and a matrix, m, and output a vector
def matvec(m, v):
    vdim = len(v)
    mrows = len(m)
    mcols = len(m[0])
    product = [0 for i in range(mrows)]
    if vdim != mcols:
        print('dimension mismatch')
        return -1
    for i in range(mrows):
        s = 0
        for j in range(mcols):
            s += int(m[i][j])*int(str(map(str,v[i])))
        product[i] = s
    return product


#input 2 matrices and output a matrix
def matmat(m, a):
    arows = len(a)
    acols = len(a[0])
    mrows = len(m)
    mcols = len(m[0])
    if arows != mcols:
        print('dimension mismatch')
        return -1
    product = [[0 for i in range(acols)]for i in range(mrows)]
    for i in range(mrows):#gets to the coordinate i
        
        for j in range(acols):#gets to the coordinate j
            #print("i: " + str(i)) used to check i index
            #print("j: " + str(j)) used to check j index
            for x in range(mcols):#adds and multiply the elements
                #print("x: " + str(x)) used to check if calculations are being done correctly
                product[i][j] += int(m[i][x])*int(a[x][j])
    return product


#m0 = input("Insert row one of your matrix\n").split(" ")
#m1 = input("Insert row two of your matrix\n").split(" ")
#m2 = input("Insert row three of your matrix\n").split(" ")
#x = input("Insert elements of your vector\n").split(" ")
#print(row0)
#m = [m0, m1, m2]
#b0 = int(m[0][0])*int(x[0]) + int(m[0][1])*int(x[1]) + int(m[0][2])*int(x[2])
#b1 = int(m[1][0])*int(x[0]) + int(m[1][1])*int(x[1]) + int(m[1][2])*int(x[2])
#b2 = int(m[2][0])*int(x[0]) + int(m[2][1])*int(x[1]) + int(m[2][2])*int(x[2])
#b = [b0, b1, b2]
#print(b)

#input: 2d array matrix and 1d array vector
#output: product of the input matrix and input vector
#print(matvec(m, x))
print(matmat(m, v))
#print(matvec(m, v))

print(v)
print(m)