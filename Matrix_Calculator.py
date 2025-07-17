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




#input: 2d array matrix and 1d array vector
#output: product of the input matrix and input vector

print(matmat(m, v))


print(v)
print(m)
