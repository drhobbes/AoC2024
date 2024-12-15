layout = []
moves = ''
robot = []
p2_robot = []
p2_layout = []
with open('day15_input.txt','r') as f:
  map_read = True
  for line in f:
    if len(line.strip()) == 0:
      map_read = False
    elif map_read:
      layout.append([c for c in line.strip()])
      p2_layout.append([])
      for c in layout[-1]:
        match c:
          case '#':
            p2_layout[-1].extend(['#','#'])
          case '.':
            p2_layout[-1].extend(['.','.'])
          case 'O':
            p2_layout[-1].extend(['[',']'])
          case '@':
            p2_layout[-1].extend(['@','.'])
      if '@' in line:
        robot = [len(layout)-1,line.find('@')]
        p2_robot = [len(p2_layout)-1,p2_layout[-1].index('@')]
    else:
      moves += line.strip()

def move_left():
  line = layout[robot[0]][:robot[1]]
  if '.' not in line: return
  if line[::-1].index('#') < line[::-1].index('.'): return

  for i in range(len(line)-1-line[::-1].index('.'),robot[1]-1):
    layout[robot[0]][i] = 'O'
  layout[robot[0]][robot[1]-1]='@'
  layout[robot[0]][robot[1]] = '.'
  robot[1] -= 1

def move_right():
  line = layout[robot[0]][robot[1]+1:]
  if '.' not in line: return
  if line.index('#') < line.index('.'): return

  i = robot[1]+line.index('.')+1
  while i > robot[1]:
    layout[robot[0]][i] = 'O'
    i -= 1
  layout[robot[0]][robot[1]+1] = '@'
  layout[robot[0]][robot[1]] = '.'
  robot[1] += 1

def move_up():
  free = robot[0]-1
  while free >= 0 and layout[free][robot[1]] != '.': free -= 1
  if free == -1: return
  wall = robot[0]-1
  while wall >= 0 and layout[wall][robot[1]] != '#': wall -= 1
  if wall > free: return

  for i in range(free, robot[0]-1):
    layout[i][robot[1]] = 'O'
  layout[robot[0]-1][robot[1]] = '@'
  layout[robot[0]][robot[1]] = '.'
  robot[0] -= 1

def move_down():
  free = robot[0]+1
  while free < len(layout) and layout[free][robot[1]] != '.': free += 1
  if free == len(layout): return
  wall = robot[0]+1
  while wall < len(layout) and layout[wall][robot[1]] != '#': wall += 1
  if wall < free: return

  while free > robot[0]:
    layout[free][robot[1]] = 'O'
    free -= 1
  layout[robot[0]+1][robot[1]] = '@'
  layout[robot[0]][robot[1]] = '.'
  robot[0] += 1

def calc_gps(i,j,layout):
  return 100*i+j if layout[i][j] in ['O','['] else 0

def print_layout(layout):
  for line in layout:
    print(' '.join(line))

for c in moves:
  match c:
    case '<':
      move_left()
    case '>':
      move_right()
    case '^':
      move_up()
    case 'v':
      move_down()

total = 0
for i in range(len(layout)):
  for j in range(len(layout[i])):
    total += calc_gps(i,j,layout)
print('part 1:',total)

################################################################### part 2

def move_left2():
  line = p2_layout[p2_robot[0]][:p2_robot[1]]
  if '.' not in line: return
  if line[::-1].index('#') < line[::-1].index('.'): return

  i = len(line)-1-line[::-1].index('.')
  while i < p2_robot[1]:
    p2_layout[p2_robot[0]][i] = '['
    p2_layout[p2_robot[0]][i+1] = ']'
    i += 2
  p2_layout[p2_robot[0]][p2_robot[1]-1] = '@'
  p2_layout[p2_robot[0]][p2_robot[1]] = '.'
  p2_robot[1] -= 1

def move_right2():
  line = p2_layout[p2_robot[0]][p2_robot[1]+1:]
  if '.' not in line: return
  if line.index('#') < line.index('.'): return

  i = p2_robot[1]+line.index('.')+1
  while i > p2_robot[1]:
    p2_layout[p2_robot[0]][i] = ']'
    p2_layout[p2_robot[0]][i-1] = '['
    i -= 2
  p2_layout[p2_robot[0]][p2_robot[1]+1] = '@'
  p2_layout[p2_robot[0]][p2_robot[1]] = '.'
  p2_robot[1] += 1

def is_blocked(i,j,dir):
  # (i,j) is the location of the [, and dir is -1 to look up and 1 to look down
  if p2_layout[i+dir][j] == '.' and p2_layout[i+dir][j+1] == '.': return False
  if p2_layout[i+dir][j] == '#' or p2_layout[i+dir][j+1] == '#': return True

  # there must be other boxes in that direction, ask them:
  if p2_layout[i+dir][j] == '[':
    # one box directly above/below me
    return is_blocked(i+dir,j,dir)
  if p2_layout[i+dir][j] == ']':
    # box offset to the left
    if is_blocked(i+dir,j-1,dir): return True
  if p2_layout[i+dir][j+1] == '[':
    if is_blocked(i+dir,j+1,dir): return True
  return False

def update_boxes(i,j,dir):
  # (i,j) is the location of the [, and dir is -1 to move up and 1 to move down
  if p2_layout[i+dir][j] != '.' or p2_layout[i+dir][j+1] != '.':
    if p2_layout[i+dir][j] == '[':
      update_boxes(i+dir,j,dir)
    if p2_layout[i+dir][j] == ']':
      update_boxes(i+dir,j-1,dir)
    if p2_layout[i+dir][j+1] == '[':
      update_boxes(i+dir,j+1,dir)
  p2_layout[i+dir][j] = '['
  p2_layout[i+dir][j+1] = ']'
  p2_layout[i][j] = '.'
  p2_layout[i][j+1] = '.'

def move(dir):
  # -1 to move up, 1 to move down
  if p2_layout[p2_robot[0]+dir][p2_robot[1]] == '#': return
  if p2_layout[p2_robot[0]+dir][p2_robot[1]] == '[':
    if is_blocked(p2_robot[0]+dir,p2_robot[1],dir): return
    update_boxes(p2_robot[0]+dir,p2_robot[1],dir)
  if p2_layout[p2_robot[0]+dir][p2_robot[1]] == ']':
    if is_blocked(p2_robot[0]+dir,p2_robot[1]-1,dir): return
    update_boxes(p2_robot[0]+dir, p2_robot[1]-1,dir)
  p2_layout[p2_robot[0]+dir][p2_robot[1]] = '@'
  p2_layout[p2_robot[0]][p2_robot[1]] = '.'
  p2_robot[0] += dir

for c in moves:
  match c:
    case '<':
      move_left2()
    case '>':
      move_right2()
    case '^':
      move(-1)
    case 'v':
      move(1)

total = 0
for i in range(len(p2_layout)):
  for j in range(len(p2_layout[i])):
    total += calc_gps(i,j,p2_layout)
print('part 2:',total)