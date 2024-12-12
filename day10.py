topo_map = []
trailheads = {}
with open('day10_input.txt','r') as f:
	i = 0
	for line in f:
		topo_map.append([int(x) for x in line if x.isdigit()])
		if '0' in line:
			start = 0
			j = line.find('0')
			while j != -1:
				trailheads[(i,j)] = 0
				start = j+1
				j = line.find('0',start)
		i += 1

def find_helper(i,j,elev):
	# base case 1: out of bounds
	if i < 0 or i >= len(topo_map):
		return None
	if j < 0 or j >= len(topo_map[i]):
		return None

	# base case 2: no trail
	if topo_map[i][j] != elev:
		return None

	# base case 3: end of trail - SUCCESS
	if elev == 9:
		return [[i,j]]

	# recursive case: check up down left right
	new_coords = [[i+1,j],[i-1,j],[i,j+1],[i,j-1]]
	nines = []
	for coord in new_coords:
		ends = find_helper(coord[0],coord[1],elev+1)
		if ends != None:
			nines.extend([x for x in ends if x not in nines])
	return nines

def other_findhelper(i,j,elev):
	# base case 1: out of bounds
	if i < 0 or i >= len(topo_map):
		return 0
	if j < 0 or j >= len(topo_map[i]):
		return 0

	# base case 2: no trail
	if topo_map[i][j] != elev:
		return 0

	# base case 3: end of trail - SUCCESS
	if elev == 9:
		return 1

	new_coords = [[i+1,j],[i-1,j],[i,j+1],[i,j-1]]
	total = 0
	for coord in new_coords:
		total += other_findhelper(coord[0], coord[1],elev+1)
	return total

def other_findtrail(start):
	return other_findhelper(start[0],start[1],0)

def find_trail(start):
	return find_helper(start[0],start[1],0)

for trailhead in trailheads:
	trailheads[trailhead] = [len(find_trail(trailhead)), other_findtrail(trailhead)]

p1_total = 0
p2_total = 0
for val in trailheads.values():
	p1_total += val[0]
	p2_total += val[1]
print('part 1:',p1_total)
print('part 2:',p2_total)