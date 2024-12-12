def swap(arr,i,j):
	temp = arr[i]
	arr[i] = arr[j]
	arr[j] = temp

with open('day09_babyinput.txt','r') as f:
	diskmap = f.readline().strip()

# populate filesystem according to the rules
filesys = []
files = {}
empties = {}
file_counter = 0
for i in range(len(diskmap)):
	digit = int(diskmap[i])
	if i % 2 == 0:
		# file
		files[file_counter] = {'len':digit,'loc':len(filesys)}
		filesys.extend([file_counter]*digit)
		file_counter += 1
	else:
		# empty
		empties[file_counter] = {'len':digit,'loc':len(filesys)}
		filesys.extend(['.']*digit)
filesys_p2 = filesys[:]

# compact filesystem
last_occupied = len(filesys)-1
first_unoccupied = int(diskmap[0])
while first_unoccupied < last_occupied:
	swap(filesys,first_unoccupied,last_occupied)
	while filesys[first_unoccupied] != '.':
		first_unoccupied += 1
	while not isinstance(filesys[last_occupied], int):
		last_occupied -= 1

checksum = 0
for i in range(first_unoccupied):
	checksum += filesys[i]*i
print('part 1:',checksum)

# once more with less fragmentation:
keys = list(files.keys())
keys.sort()
for file in keys[::-1]:
	available = list(empties.keys())
	i = 0
	while i < len(available) and empties[available[i]]['len'] < files[file]['len']:
		i += 1
	if i < len(available) and empties[available[i]]['loc'] < files[file]['loc']:
		# found a spot, move the file
		for j in range(files[file]['len']):
			swap(filesys_p2,empties[available[i]]['loc']+j,files[file]['loc']+j)
		files[file]['loc'] = empties[available[i]]['loc']
		empties[available[i]]['len'] -= files[file]['len']
		if empties[available[i]]['len'] == 0:
			del empties[available[i]]
		else:
			empties[available[i]]['loc'] += files[file]['len']

checksum = 0
for i in range(len(filesys_p2)):
	checksum += filesys_p2[i]*i if isinstance(filesys_p2[i],int) else 0
print('part 2:',checksum)