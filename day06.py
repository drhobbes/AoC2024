layout = []
guard_start = []
visited = [] # TODO: stop double-counting things

with open('day06_input.txt','r') as f:
	line_index = 0
	for line in f:
		if '^' in line:
			guard_start = [line_index, line.find('^')]
		layout.append(line.strip())
		line_index += 1

def move_up(guard):
	i = guard[0]-1
	count = 0
	while i >= 0 and layout[i][guard[1]] != '#':
		count += 1
		i -= 1
	guard[0] = -1 if i == -1 else i+1
	return count if i != -1 else count-1

def move_down(guard):
	i = guard[0]+1
	count = 0
	while i < len(layout) and layout[i][guard[1]] != '#':
		count += 1
		i += 1
	guard[0] = -1 if i == len(layout) else i-1
	return count if i != len(layout) else count-1

def move_right(guard):
	path = layout[guard[0]][guard[1]:]
	stop = path.find('#')
	guard[1] = -1 if stop == -1 else guard[1]+stop-1
	return stop-1 if stop != -1 else len(path-1)

def move_left(guard):
	path = layout[guard[0]][:guard[1]]
	stop = path[::-1].find('#')
	guard[1] = -1 if stop == -1 else guard[1]-stop
	return stop-1 if stop != -1 else len(path)

total = 0
moves = 0
while guard_start[0] != -1 and guard_start[1] != -1:
	if moves % 4 == 0:
		total += move_up(guard_start)
	elif moves % 4 == 1:
		total += move_right(guard_start)
	elif moves % 4 == 2:
		total += move_down(guard_start)
	else:
		total += move_left(guard_start)
	moves += 1

print('part 1:',total)