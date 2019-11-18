
from bisect import *
n = int(input())
scores = list(set(map(int,input().split())))
l = len(scores)
scores.sort()
m = int(input())
alice = map(int,input().split())
for i in alice:
    print (l - bisect_right(scores, i) + 1)
                
        