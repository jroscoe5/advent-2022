#q1
def orrd(a): return ord(a) - (38, 96)[a == a.lower()]
print(sum([orrd(list(set(l[len(l)//2:])&set(l[:len(l)//2]))[0]) for l in open('input.txt').read().splitlines()]))

#q2
from more_itertools import grouper
print(sum([orrd(list(set(l[0]).intersection(set(l[1]),set(l[2])))[0]) for l in grouper(open('input.txt').read().splitlines(),3)]))
