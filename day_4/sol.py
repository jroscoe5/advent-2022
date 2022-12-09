#q1
import re
print(sum([(int(s[0])<=int(s[2])and int(s[1])>=int(s[3]))or(int(s[2])<=int(s[0])and int(s[3])>=int(s[1]))for s in [re.split(',|-',l)for l in open('input.txt').read().splitlines()]]))

#q2
