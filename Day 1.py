from itertools import combinations
import itertools as it

f = open('trial','r')

g = []
for line in f:
    g.append (int(line))

combo = list(it.combinations(g,2))
for x in combo:
    if sum(x) == 2020:
        print('Part 1 =',x[0]*x[1])
combo2 = list(it.combinations(g,3))
for x in combo2:
    if sum(x) == 2020:
        print('Part 2 =',x[0]*x[1]*x[2])
