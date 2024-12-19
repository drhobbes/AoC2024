from sys import maxsize

layout = []
for i in range(71):
  layout.append([])
  for j in range(71):
    layout[i].append(['.',[i,j],maxsize])
locations = []
with open('day18_input.txt','r') as f:
  for line in f:
    parts = line.strip().split(',')
    locations.append([int(x) for x in parts])

layout[0][0][2] = 0 # no steps to start

for i in range(1024):
  layout[locations[i][1]][locations[i][0]][0] = '#'

def reset(layout):
  for line in layout:
    for loc in line:
      loc[2] = maxsize
  layout[0][0][2] = 0

def print_layout(layout):
  for line in layout:
    display = [element[0] if element[0] == '#' or element[2] == maxsize else str(element[2]) for element in line]
    print(' '.join(display))

def remove_lowest(queue):
  min_cost = queue[0][2]
  min_ind = 0
  for i in range(len(queue)):
    if queue[i][2] < min_cost:
      min_cost = queue[i][2]
      min_ind = i
  return queue.pop(min_ind)

def run_maze(layout):
  queue = []
  visited = []
  queue.append(layout[0][0])
  while len(queue) > 0:
    current = remove_lowest(queue)
    if current in visited: continue
    visited.append(current)

    [i,j] = current[1]
    neighbors = []
    if i>0 and layout[i-1][j][0] != '#': neighbors.append(layout[i-1][j])
    if i<len(layout)-1 and layout[i+1][j][0] != '#': neighbors.append(layout[i+1][j])
    if j>0 and layout[i][j-1][0] != '#': neighbors.append(layout[i][j-1])
    if j<len(layout[i])-1 and layout[i][j+1][0] != '#': neighbors.append(layout[i][j+1])
    tentative_cost = current[2]+1
    for neighbor in neighbors:
      if tentative_cost < neighbor[2]:
        neighbor[2] = tentative_cost
        queue.append(neighbor)
        
run_maze(layout)
print('part 1:', layout[70][70][2])

# brute force baybeeeee (this takes 8 million years fyi)
for i in range(1024,len(locations)):
  reset(layout)
  layout[locations[i][1]][locations[i][0]][0] = '#'
  run_maze(layout)
  if layout[70][70][2] == maxsize:
    print('part 2:',locations[i])
    break
