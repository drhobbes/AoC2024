opp = []
you = []

with open('2022day02_input.txt','r') as f:
  for line in f:
    parts = line.strip().split(' ')
    opp.append(parts[0])
    you.append(parts[1])

def compare(opp_choice, you_choice):
  score = 0
  match you_choice:
    case 'X': score = 1
    case 'Y': score = 2
    case 'Z': score = 3
  test = ord(you_choice)-(ord(opp_choice)+23)
  if test == 0: return score + 3
  if test == 1 or test == -2: return score + 6
  if test == -1 or test == 2: return score

total = 0
for i in range(len(opp)):
  total += compare(opp[i],you[i])
print('part 1:',total)

# this feels like the most pythonic way to do it
draw = {'A':1, 'B':2, 'C':3}
win = {'A':2, 'B':3, 'C':1}
lose = {'A':3, 'B':1, 'C':2}

def throw(opp_choice, outcome):
  score = 0
  if outcome == 'Y':
    return 3+draw[opp_choice]
  elif outcome == 'X':
    return lose[opp_choice]
  else:
    return 6+win[opp_choice]

total = 0
for i in range(len(opp)):
  total += throw(opp[i],you[i])
print('part 2:',total)
