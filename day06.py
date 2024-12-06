layout = []
guard_start = []
visited = []

with open('day06_babyinput.txt','r') as f:
  line_index = 0
  for line in f:
    if '^' in line:
      guard_start = [line_index, line.find('^')]
    layout.append(line.strip())
    visited.append([' ']*len(line.strip()))
    line_index += 1
    
visited[guard_start[0]][guard_start[1]] = 'U'

def move_up(guard):
  i = guard[0]-1
  while i >= 0 and layout[i][guard[1]] != '#':
    visited[i][guard[1]] = 'U'
    i -= 1
  guard[0] = -1 if i == -1 else i+1

def move_down(guard):
  i = guard[0]+1
  while i < len(layout) and layout[i][guard[1]] != '#':
    visited[i][guard[1]] = 'D'
    i += 1
  guard[0] = -1 if i == len(layout) else i-1

def move_right(guard):
  j = guard[1]+1
  while j < len(layout[guard[0]]) and layout[guard[0]][j] != '#':
    visited[guard[0]][j] = 'R'
    j += 1
  guard[1] = -1 if j == len(layout) else j-1

def move_left(guard):
  j = guard[1]-1
  while j >= 0 and layout[guard[0]][j] != '#':
    visited[guard[0]][j] = 'L'
    j -= 1
  guard[1] = -1 if j == -1 else j+1

moves = 0
while guard_start[0] != -1 and guard_start[1] != -1:
  if moves % 4 == 0:
    move_up(guard_start)
  elif moves % 4 == 1:
    move_right(guard_start)
  elif moves % 4 == 2:
    move_down(guard_start)
  else:
    move_left(guard_start)
  moves += 1

total = 0
for row in visited:
  total += len(row)-row.count(' ')
print('part 1:',total)

################################################

def blockable_sw(loc_row, loc_col):
  if loc_col == 0: return False
  if loc_row+1 < len(layout) and layout[loc_row+1][loc_col+1:].find('#') != -1:
    k = layout[loc_row+1][loc_col+1:].find('#')+loc_col+1
  else: return False
  m = loc_row+2
  while m < len(layout) and layout[m][k-1] != '#':
    m += 1
  if m == len(layout): return False
  # coord 2 is [loc_row+1][k], coord 3 is [m][k-1]; blockable at [m-1][loc_col-1]
  return True

def blockable_se(loc_row, loc_col):
  if loc_row+1 < len(layout) and layout[loc_row+1][loc_col+1:].find('#') != -1:
    k = layout[loc_row+1][loc_col+1:].find('#')+loc_row+1
  else: return False
  m = loc_row+2
  while m < len(layout) and layout[m][loc_col-1] != '#':
    m += 1
  if m == len(layout): return False
  # coord 2 is [loc_row+1][k], coord 3 is [m][loc_col-1]
  return True
  
def blockable_ne(loc_row, loc_col):
  m = loc_row+2
  while m < len(layout) and layout[m][loc_col-1] != '#':
    m += 1
  if m == len(layout): return False
  if m+1 < len(layout) and layout[m+1][loc_col+1:].find('#') != -1:
    return True
  else: return False
  # coord 2 is [m][loc_col-1], coord 3 is [m+1][k]

def blockable_nw(loc_row, loc_col):
  if loc_row == 0: return False
  if layout[loc_row-1][:loc_col].find('#') == -1: return False
  m = loc_row-2
  while m >= 0 and layout[m][loc_col+1] != '#':
    m -= 1
  if m == -1: return False
  return True
  # coord 2 is [loc_row-1][m], coord 3 is [k][loc_col+1]

count = 0
for i in range(len(layout)):
  start = 0
  obst_j = layout[i].find('#')
  while obst_j != -1:
    if blockable_sw(i, obst_j): count += 1
    if blockable_se(i, obst_j): count += 1
    if blockable_ne(i, obst_j): count += 1
    if blockable_nw(i, obst_j): count += 1
    start = obst_j + 1
    obst_j = layout[i].find('#',start)
print('part 2:',count)
