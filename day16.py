from sys import maxsize

layout = []
with open('day16_input.txt','r') as f:
  for line in f:
    layout.append([c for c in line.strip()])
    if 'E' in line:
      end = [len(layout)-1,line.find('E')]
    if 'S' in line:
      start = [len(layout)-1,line.find('S')]

costs = []
for line in layout:
  costs.append([None if c == '#' else [maxsize,'',''] for c in line])
  j = 0
  for val in costs[len(costs)-1]:
    if val != None:
      val.append([len(costs)-1,j])
    j += 1
costs[end[0]][end[1]][1] = 'E'
costs[start[0]][start[1]] = [0,'S','>',start]

def print_layout(layout):
  for line in layout:
    print(' '.join(line))

def print_costs():
  for line in costs:
    printline = ''
    for val in line:
      if val == None:
        printline += '# '
      elif val[1] != '':
        printline += val[1]+' '
      else:
        printline += val[2]+' '
    print(printline)

def print_paths():
  for line in costs:
    printline = ''
    for val in line:
      if val == None:
        printline += '# '
      elif val[1] == '':
        printline += '  '
      else:
        printline += val[1]+' '
    print(printline)

def dijkstra():
  queue = []
  visited = []
  queue.append(costs[start[0]][start[1]])

  while len(queue) > 0:
    current = remove_lowest_cost(queue) # this is O(N) and i should refactor it to use a fucking heap but idgaf
    if current in visited: continue
    visited.append(current)

    [i,j] = current[3]
    if costs[i-1][j] != None:
      tentative_cost = current[0] + (1 if current[2] == '^' else 1001)
      if tentative_cost < costs[i-1][j][0] and current[2] != 'v':
        costs[i-1][j][0] = tentative_cost
        costs[i-1][j][2] = '^'
        queue.append(costs[i-1][j])

    if costs[i+1][j] != None:
      tentative_cost = current[0] + (1 if current[2] == 'v' else 1001)
      if tentative_cost < costs[i+1][j][0] and current[2] != '^':
        costs[i+1][j][0] = tentative_cost
        costs[i+1][j][2] = 'v'
        queue.append(costs[i+1][j])

    if costs[i][j-1] != None:
      tentative_cost = current[0] + (1 if current[2] == '<' else 1001)
      if tentative_cost < costs[i][j-1][0] and current[2] != '>':
        costs[i][j-1][0] = tentative_cost
        costs[i][j-1][2] = '<'
        queue.append(costs[i][j-1])

    if costs[i][j+1] != None:
      tentative_cost = current[0] + (1 if current[2] == '>' else 1001)
      if tentative_cost < costs[i][j+1][0] and current[2] != '<':
        costs[i][j+1][0] = tentative_cost
        costs[i][j+1][2] = '>'
        queue.append(costs[i][j+1])

def remove_lowest_cost(queue):
  min_cost = queue[0][0]
  min_ind = 0
  for i in range(len(queue)):
    if queue[i][0] < min_cost:
      min_cost = queue[i][0]
      min_ind = i
  return queue.pop(min_ind)

dijkstra()
print('part 1:',costs[end[0]][end[1]][0])

def find_paths():
  queue = []
  visited = []
  queue.append(costs[end[0]][end[1]])

  while len(queue) > 0:
    current = remove_lowest_cost(queue)
    if current in visited: continue
    visited.append(current)
    if current[1] == 'S': continue

    [i,j] = current[3]
    neighbors = []
    if costs[i-1][j] != None: neighbors.append(costs[i-1][j])
    if costs[i+1][j] != None: neighbors.append(costs[i+1][j])
    if costs[i][j-1] != None: neighbors.append(costs[i][j-1])
    if costs[i][j+1] != None: neighbors.append(costs[i][j+1])
    scores = [val[0] for val in neighbors]
    min_score = min(scores)
    for neighbor in neighbors:
      if neighbor[0] == min_score or (neighbor[0] == min_score + 1000 and neighbor[2] != current[2] and current[1] != 'E'):
        neighbor[1] = 'O' if neighbor[1] != 'S' else 'S'
        if neighbor[3] == [13,2]: print(current)
        queue.append(neighbor)
  return len(visited)

print('part 2:',find_paths())