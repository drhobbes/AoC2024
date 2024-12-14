robots = []
with open('day14_input.txt','r') as f:
    for line in f:
      parts = line.strip().split(' ')
      pos = [int(x) for x in parts[0].split('=')[1].split(',')]
      vel = [int(x) for x in parts[1].split('=')[1].split(',')]
      robots.append({'pos':pos, 'vel':vel})

width = 101
height = 103

def move(robot, seconds):
  robot['pos'][0] += seconds * robot['vel'][0]
  robot['pos'][0] %= width
  robot['pos'][1] += seconds * robot['vel'][1]
  robot['pos'][1] %= height

def show_robots():
  grid = [['.']*width for i in range(height)]
  for robot in robots:
    if grid[robot['pos'][1]][robot['pos'][0]] == '.':
      grid[robot['pos'][1]][robot['pos'][0]] = 1
    else:
      grid[robot['pos'][1]][robot['pos'][0]] += 1
  return grid

def safety_factor():
  grid = show_robots()
  nw = 0
  for i in range(height//2):
    for j in range(width//2):
      nw += grid[i][j] if isinstance(grid[i][j], int) else 0
  ne = 0
  for i in range(height//2):
    for j in range(width//2+1,width):
      ne += grid[i][j] if isinstance(grid[i][j], int) else 0
  sw = 0
  for i in range(height//2+1, height):
   for j in range(width//2):
      sw += grid[i][j] if isinstance(grid[i][j], int) else 0
  se = 0
  for i in range(height//2+1, height):
    for j in range(width//2+1, width):
      se += grid[i][j] if isinstance(grid[i][j], int) else 0
  return nw*ne*sw*se

for robot in robots:
  move(robot,100)
print('part 1:',safety_factor())

num_seconds = 100
orig_safety = safety_factor()
while abs(safety_factor()-orig_safety) < 0.75*orig_safety:
  for robot in robots:
    move(robot,1)
  num_seconds += 1
# for debugging
for line in show_robots():
  print(' '.join([str(x) for x in line]))
print('part 2:',num_seconds)

'''
 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
 1 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1 
 1 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1
 1 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1
 1 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1 
 1 . . . . . . . . . . . . . . 1 . . . . . . . . . . . . . . 1 
 1 . . . . . . . . . . . . . 1 1 1 . . . . . . . . . . . . . 1 
 1 . . . . . . . . . . . . 1 1 1 1 1 . . . . . . . . . . . . 1 
 1 . . . . . . . . . . . 1 1 1 1 1 1 1 . . . . . . . . . . . 1 
 1 . . . . . . . . . . 1 1 1 1 1 1 1 1 1 . . . . . . . . . . 1 
 1 . . . . . . . . . . . . 1 1 1 1 1 . . . . . . . . . . . . 1 
 1 . . . . . . . . . . . 1 1 1 1 1 1 1 . . . . . . . . . . . 1 
 1 . . . . . . . . . . 1 1 1 1 1 1 1 1 1 . . . . . . . . . . 1 
 1 . . . . . . . . . 1 1 1 1 1 1 1 1 1 1 1 . . . . . . . . . 1 
 1 . . . . . . . . 1 1 1 1 1 1 1 1 1 1 1 1 1 . . . . . . . . 1 
 1 . . . . . . . . . . 1 1 1 1 1 1 1 1 1 . . . . . . . . . . 1 
 1 . . . . . . . . . 1 1 1 1 1 1 1 1 1 1 1 . . . . . . . . . 1 
 1 . . . . . . . . 1 1 1 1 1 1 1 1 1 1 1 1 1 . . . . . . . . 1 
 1 . . . . . . . 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 . . . . . . . 1 
 1 . . . . . . 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 . . . . . . 1 
 1 . . . . . . . . 1 1 1 1 1 1 1 1 1 1 1 1 1 . . . . . . . . 1 
 1 . . . . . . . 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 . . . . . . . 1 
 1 . . . . . . 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 . . . . . . 1 
 1 . . . . . 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 . . . . . 1 
 1 . . . . 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 . . . . 1 
 1 . . . . . . . . . . . . . 1 1 1 . . . . . . . . . . . . . 1 
 1 . . . . . . . . . . . . . 1 1 1 . . . . . . . . . . . . . 1 
 1 . . . . . . . . . . . . . 1 1 1 . . . . . . . . . . . . . 1 
 1 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1 
 1 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1 
 1 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1 
 1 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1 
 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
 '''
