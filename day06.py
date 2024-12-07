layout = []
guard_start = []
visited = []

''' loading the file: make note of where the guard starts and create blank template for 
tracking movement '''
with open('day06_input.txt','r') as f:B
  line_index = 0
  for line in f:
    if '^' in line:
      guard_start = [line_index, line.find('^')]
    layout.append(line.strip())
    visited.append([' ']*len(line.strip()))
    line_index += 1

###################################################################################################

''' All four of these helper methods work the same way:
  Move the guard up through the room until:
  a) they encounter an obstacle and stop,
  b) they exit the room (in which case we set the relevant coordinate to -1), or
  c) they start retracing steps, in which case they're in a cycle
'''
def move_up(guard, new_visited, layout):
  i = guard[0]-1
  while i >= 0 and layout[i][guard[1]] != '#':
    if new_visited[i][guard[1]] == 'U':
      raise Exception('cycle detected')
    new_visited[i][guard[1]] = 'U'
    i -= 1
  guard[0] = -1 if i == -1 else i+1

def move_down(guard, new_visited, layout):
  i = guard[0]+1
  while i < len(layout) and layout[i][guard[1]] != '#':
    if new_visited[i][guard[1]] == 'D':
      raise Exception('cycle detected')
    new_visited[i][guard[1]] = 'D'
    i += 1
  guard[0] = -1 if i == len(layout) else i-1

def move_right(guard, new_visited, layout):
  j = guard[1]+1
  while j < len(layout[guard[0]]) and layout[guard[0]][j] != '#':
    if new_visited[guard[0]][j] == 'R':
        raise Exception('cycle detected')
    new_visited[guard[0]][j] = 'R'
    j += 1
  guard[1] = -1 if j == len(layout) else j-1

def move_left(guard, new_visited, layout):
  j = guard[1]-1
  while j >= 0 and layout[guard[0]][j] != '#':
    if new_visited[guard[0]][j] == 'L':
      raise Exception('cycle detected')
    new_visited[guard[0]][j] = 'L'
    j -= 1
  guard[1] = -1 if j == -1 else j+1

################################################ PART 1: run the maze

# part 1: guard begins facing upward:
visited[guard_start[0]][guard_start[1]] = 'U'

def run_maze(i, j, visited, layout):
  moves = 0
  guard = [i,j]

  while guard[0] != -1 and guard[1] != -1:
    # move in the sequence: up/right/down/left
    if moves % 4 == 0:
      move_up(guard, visited, layout)
    elif moves % 4 == 1:
      move_right(guard, visited, layout)
    elif moves % 4 == 2:
      move_down(guard, visited, layout)
    else:
      move_left(guard, visited, layout)
    moves += 1

run_maze(guard_start[0],guard_start[1], visited, layout)

total = 0
for row in visited:
  total += len(row)-row.count(' ')
print('part 1:',total)

################################################ PART 2 APPROACH 2: brute fucking force

''' the approach here is to attempt adding an obstacle in every location that the guard visited
back in part 1 and then just run the maze again to see if a cycle occurs '''

def add_obstacle(obst_i,obst_j):
  ''' adds a single obstacle to the original layout at location (i,j) '''
  new_layout = []
  for i in range(len(layout)):
    if i == obst_i:
      new_layout.append(layout[i][:obst_j]+'#'+layout[i][obst_j+1:])
    else:
      new_layout.append(layout[i])
  return new_layout

num_cycles = 0
for i in range(len(visited)):
  for j in range(len(visited[i])):
    if visited[i][j] != ' ':
      # the guard walks here: try adding an obstacle and re-run the maze with a blank walk tracker
      new_layout = add_obstacle(i,j)
      new_visited = [[' ']*len(new_layout[0]) for row in new_layout]
      try:
        # if a cycle occurs, the helper method will raise an exception and interrupt this method
        run_maze(guard_start[0],guard_start[1],new_visited,new_layout)
      except Exception as error:
        # count the number of times we exited run_maze() with an error condition (cycle)
        num_cycles += 1
print('part 2:',num_cycles)

################################################ PART 2 ABANDONED: doesn't handle complicated loops

''' the approach here WAS to try and mathematically calculate if obstacles were in the correct
configuration to induce a cycle if we added Just One More - and it got all of the square-shaped
cycles great but anything more complicated than a square was a big ol nope 

the observation was that a (square) cycle is caused by this configuration of obstacles (with
varying sizes):
       #
            #
      #
           #
'''

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
  if visited[m-1][loc_col-1] == ' ': return False
  print('blockable sw:',m-1,loc_col-1)
  return True

def blockable_se(loc_row, loc_col):
  if loc_row+1 < len(layout) and layout[loc_row+1][loc_col+1:].find('#') != -1:
    k = layout[loc_row+1][loc_col+1:].find('#')+loc_col+1
  else: return False
  m = loc_row+2
  while m < len(layout) and layout[m][loc_col-1] != '#':
    m += 1
  if m == len(layout): return False
  # coord 2 is [loc_row+1][k], coord 3 is [m][loc_col-1]
  if visited[m+1][k-1] == ' ': return False
  print('blockable se:',m+1,k-1)
  return True
  
def blockable_ne(loc_row, loc_col):
  m = loc_row+2
  while m < len(layout) and layout[m][loc_col-1] != '#':
    m += 1
  if m+1 >= len(layout): return False
  if m+1 < len(layout) and layout[m+1][loc_col+1:].find('#') != -1:
    k = layout[m+1][loc_col+1:].find('#')+loc_col+1
  else: return False
  if k+1 >= len(layout[loc_row]): return False
  if visited[loc_row+1][k+1] == ' ': return False
  print('blockable ne:',loc_row+1,k+1)
  return True
  # coord 2 is [m][loc_col-1], coord 3 is [m+1][k]

def blockable_nw(loc_row, loc_col):
  if loc_row == 0: return False
  if layout[loc_row-1][:loc_col].find('#') == -1: return False
  k = layout[loc_row-1][:loc_col].find('#')
  if k-1 < 0: return False
  m = loc_row-2
  while m >= 0 and layout[m][loc_col+1] != '#':
    m -= 1
  if m == -1: return False
  if visited[k-1][m+1] == ' ': return False
  print('blockable nw:',k-1,m+1)
  return True
  # coord 2 is [loc_row-1][m], coord 3 is [k][loc_col+1]

'''count = 0
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
print('part 2:',count)'''
