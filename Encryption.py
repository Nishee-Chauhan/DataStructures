#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the encryption function below.
def encryption(s):
    s=s.replace(" ","")
    l=len(s)
    n=math.floor(math.sqrt(l))
    m=math.ceil(math.sqrt(l))
    print(n,m)
    if n*m<l:
        n=m
    t1=0
    t2=0
    em=[]
    while(t2<n):
        if t1+m<l:
            em.append(s[t1:t1+m])
        else:
            em.append(s[t1:])
        t1+=m
        t2+=1
    print(em)
    res=[]
    t2=0
    t1=0 
    while t2<m:
        t1=0
        w=""
        while t1<n:
            #print(em[t1])
            if len(em[t1])>0:
                i=em[t1][0]
                #print(i)
                em[t1]=em[t1][1:]
            else:
                break
            w+=i
            t1+=1
        t2+=1
        res.append(w)
    print(res)
    return " ".join(res)








if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
