#q1
def orrd(a): return ord(a) - (38, 96)[a == a.lower()]
print(sum([orrd(list(set(l[len(l)//2:]) & set(l[:len(l)//2]))[0]) for l in open('input.txt').read().splitlines()]))

#q2