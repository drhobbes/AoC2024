antennae = {}
dimensions = []
with open('day08_input.txt','r') as f:
	i = 0
	for line in f:
		for j in range(len(line.strip())):
			char = line[j]
			if char.isalnum():
				if char not in antennae:
					antennae[char] = []
				antennae[char].append([i,j])
		i += 1
	dimensions = [i,len(line.strip())]

antinodes = []
def calc_antinodes(a1, a2):
	d_row = a2[0]-a1[0]
	d_col = a2[1]-a1[1]
	antinode_1 = [a1[0]-d_row, a1[1]-d_col]
	antinode_2 = [a2[0]+d_row, a2[1]+d_col]
	if 0 <= antinode_1[0] < dimensions[0] and 0 <= antinode_1[1] < dimensions[1] and antinode_1 not in antinodes:
		antinodes.append(antinode_1)
	if 0 <= antinode_2[0] < dimensions[0] and 0 <= antinode_2[1] < dimensions[1] and antinode_2 not in antinodes:
		antinodes.append(antinode_2)

antinodes_p2 = []
def calc_p2(a1, a2):
	d_row = a2[0]-a1[0]
	d_col = a2[1]-a1[1]
	step = 0
	while 0 <= a1[0]-step*d_row < dimensions[0] and 0 <= a1[1]-step*d_col < dimensions[1]:
		i = a1[0]-step*d_row
		j = a1[1]-step*d_col
		if [i,j] not in antinodes_p2: antinodes_p2.append([i,j])
		step += 1
	step = 0
	while 0 <= a2[0]+step*d_row < dimensions[0] and 0 <= a2[1]+step*d_col < dimensions[1]:
		i = a2[0]+step*d_row
		j = a2[1]+step*d_col
		if [i,j] not in antinodes_p2: antinodes_p2.append([i,j])
		step += 1

for freq in antennae:
	for i in range(len(antennae[freq])-1):
		for j in range(i+1,len(antennae[freq])):
			calc_antinodes(antennae[freq][i], antennae[freq][j])
			calc_p2(antennae[freq][i], antennae[freq][j])
print('part 1:',len(antinodes))
print('part 2:',len(antinodes_p2))