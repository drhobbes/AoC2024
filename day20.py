from sys import maxsize

layout = []
with open('day20_babyinput.txt','r') as f:
  for line in f:
    layout.append([[x] for x in line.strip()])
    if 'S' in line:
      start = [len(layout)-1, line.find('S')]
    if 'E' in line:
      end = [len(layout)-1, line.find('E')]
    for j in range(len(line.strip())):
      layout[-1][j].append([len(layout)-1,j])
      layout[-1][j].append(maxsize)

def reset(layout):
  for line in layout:
    for loc in line:
      loc[2] = maxsize
  layout[start[0]][start[1]][2] = 0

def remove_lowest(queue):
  min_cost = queue[0][2]
  min_ind = 0
  for i in range(len(queue)):
    if queue[i][2] < min_cost:
      min_cost = queue[i][2]
      min_ind = i
  return queue.pop(min_ind)

def shortest_honest(layout):
  queue = []
  visited = []
  queue.append(layout[start[0]][start[1]])
  while len(queue) > 0:
    current = remove_lowest(queue)
    if current in visited: continue
    visited.append(current)

    [i,j] = current[1]
    neighbors = []
    if layout[i-1][j][0] != '#': neighbors.append(layout[i-1][j])
    if layout[i+1][j][0] != '#': neighbors.append(layout[i+1][j])
    if layout[i][j-1][0] != '#': neighbors.append(layout[i][j-1])
    if layout[i][j+1][0] != '#': neighbors.append(layout[i][j+1])
    tentative_cost = current[2]+1
    for neighbor in neighbors:
      if tentative_cost < neighbor[2]:
        neighbor[2] = tentative_cost
        queue.append(neighbor)

reset(layout)
shortest_honest(layout)

honest = []
honest.append(layout[end[0]][end[1]])
while honest[-1][2] != 0:
  [i,j] = honest[-1][1]
  min_neighbor = layout[i-1][j]
  if layout[i+1][j][2] < min_neighbor[2]: min_neighbor = layout[i+1][j]
  if layout[i][j-1][2] < min_neighbor[2]: min_neighbor = layout[i][j-1]
  if layout[i][j+1][2] < min_neighbor[2]: min_neighbor = layout[i][j+1]
  honest.append(min_neighbor)

full_run = honest[0][2]

time_saved = {}
for loc in honest:
  [i,j] = loc[1]
  if layout[i-1][j][0]=='#' and layout[i-2][j] in honest and layout[i-2][j][2] < loc[2]:
    saved = loc[2] - layout[i-2][j][2]
    if saved not in time_saved:
      time_saved[saved] = 0
    time_saved[saved] += 1
  if i < len(layout)-2 and layout[i+1][j][0]=='#' and layout[i+2][j] in honest and layout[i+2][j][2] < loc[2]:
    saved = loc[2] - layout[i+2][j][2]
    if saved not in time_saved:
      time_saved[saved] = 0
    time_saved[saved] += 1
  if layout[i][j-1][0]=='#' and layout[i][j-2] in honest and layout[i][j-2][2] < loc[2]:
    saved = loc[2] - layout[i][j-2][2]
    if saved not in time_saved:
      time_saved[saved] = 0
    time_saved[saved] += 1
  if j < len(layout[i])-2 and layout[i][j+1][0]=='#' and layout[i][j+2] in honest and layout[i][j+2][2] < loc[2]:
    saved = loc[2] - layout[i][j+2][2]
    if saved not in time_saved:
      time_saved[saved] = 0
    time_saved[saved] += 1
print(time_saved)
