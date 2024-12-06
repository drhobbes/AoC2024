layout = []
guard_start = []
visited = []

with open('day06_input.txt','r') as f:
  line_index = 0
  for line in f:
    if '^' in line:
      guard_start = [line_index, line.find('^')]
    layout.append(line.strip())
    visited.append([' ']*len(line.strip()))
    line_index += 1
    
visited[guard_start[0]][guard_start[1]] = 'X'

def move_up(guard):
  i = guard[0]-1
  while i >= 0 and layout[i][guard[1]] != '#':
    visited[i][guard[1]] = 'X'
    i -= 1
  guard[0] = -1 if i == -1 else i+1

def move_down(guard):
  i = guard[0]+1
  while i < len(layout) and layout[i][guard[1]] != '#':
    visited[i][guard[1]] = 'X'
    i += 1
  guard[0] = -1 if i == len(layout) else i-1

def move_right(guard):
  j = guard[1]+1
  while j < len(layout[guard[0]]) and layout[guard[0]][j] != '#':
    visited[guard[0]][j] = 'X'
    j += 1
  guard[1] = -1 if j == len(layout) else j-1

def move_left(guard):
  j = guard[1]-1
  while j >= 0 and layout[guard[0]][j] != '#':
    visited[guard[0]][j] = 'X'
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
  total += row.count('X')
print('part 1:',total)
