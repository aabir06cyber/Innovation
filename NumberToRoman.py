# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 11:54:39 2024

@author: Aabir Bhattacharya
"""
#INPUT ANY NUMBER TO DISPLAY ITS ROMAN EQUIVALENT
#############################################################################################
#How does this work?
"""
E.g.- 1994 = 1000 + 900 + 90 + 4
              M     CM    XC  IV
===>Calculate no. of digits. Divide the number by 10 raised to power i, and again multiply by
10^i, so that the desired quotient (i.e. 1000,900,90,4) is obtained. Next are some simple
conditions. The loops in the 'if' blocks are for nos. which lie in an interval, e.g. 700,
then it will print 'D' for 500 and two 'C's for 600 & 700. Same for others. The loop START 
value depends on the condition, STOP value is increased by 1,10,100,1000 because it is not
counted in the last iteration. STEP value depends on condition. E.g.- for 300, it is 
(100, 300+100=400, 100). 3 Cs are printed with 'C' for 400 being not printed. Same for others.
'end=""' is given to print in one line.
.............................This is a 46-lines program code.................................
"""##########################################################################################
print("This program converts a number from the Hindu-Arabic Numeral"+
      " System into it's Roman Numerals equivalent.")
d=int(input("Number to be converted: "))
conv=str(d)
x=len(conv)
print("Equivalent Roman Number: ",end="")
for i in range (x-1,-1,-1):
    k=d//(10**i)
    k1=k*(10**i)
    d=d-(k1)
    if(k1>=1000):
        for i in range(1000,k1+1000,1000):
            print("M",end="")
    if(k1==900):
        print("CM",end="")
    if(k1>=500 and k1<=800):
        print("D",end="")
        for i in range(600,k1+100,100):
            print("C",end="")
    if(k1==400):
        print("CD",end="")
    if(k1>=100 and k1<400):
        for i in range(100,k1+100,100):
            print("C",end="")
    if(k1==90):
        print("XC",end="")
    if(k1>=50 and k1<=80):
        print("L",end="")
        for i in range(60,k1+10,10):
            print("X",end="")
    if(k1==40):
        print("XL",end="")
    if(k1>=10 and k1<40):
        for i in range(10,k1+10,10):
            print("X",end="")
    if(k1==9):
        print("IX",end="")
    if(k1>=5 and k1<9):
        print("V",end="")
        for i in range(6,k1+1,1):
            print("I",end="")
    if(k1==4):
        print("IV",end="")
    if(k1>=1 and k1<4):
        for i in range(1,k1+1,1):
            print("I",end="")
#--------------------------THE END---------------------------#