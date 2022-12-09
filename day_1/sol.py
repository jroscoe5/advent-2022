import re
# q1
print(max([sum(int(i) for i in re.findall(r'\d+', s)) for s in str(open('input.txt').readlines()).split(" '\\n', ")]))

# q2
print(sum(sorted([sum(int(i) for i in re.findall(r'\d+', s)) for s in str(open('input.txt').readlines()).split(" '\\n', ")])[-3:]))