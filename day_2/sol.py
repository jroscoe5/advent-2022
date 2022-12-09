#q1
def score(u, o):
  if u=='A':
    if o=='X':return 4  #1 + 3
    if o=='Y':return 8  #2 + 6
    if o=='Z':return 3  #3 + 0
  if u=='B':
    if o=='X':return 1  #1 + 0
    if o=='Y':return 5  #2 + 3
    if o=='Z':return 9  #3 + 6
  if u=='C':
    if o=='X':return 7  #1 + 6
    if o=='Y':return 2  #2 + 0  
    if o=='Z':return 6  #3 + 3

print(sum(score(line.split(' ')[0], line.split(' ')[1]) for line in open('input.txt').read().splitlines()))

#q2
# x = lose, y = draw, z = win
def score2(u, o):
  if u=='A':
    if o=='X':return 3  #3 + 0
    if o=='Y':return 4  #1 + 3
    if o=='Z':return 8  #2 + 6
  if u=='B':
    if o=='X':return 1  #1 + 0
    if o=='Y':return 5  #2 + 3
    if o=='Z':return 9  #3 + 6
  if u=='C':
    if o=='X':return 2  #2 + 0
    if o=='Y':return 6  #3 + 3  
    if o=='Z':return 7  #1 + 6

print(sum(score2(line.split(' ')[0], line.split(' ')[1]) for line in open('input.txt').read().splitlines()))