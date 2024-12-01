list1 = []
list2 = []
with open('day01_input.txt') as f:
	for line in f:
		vals = line.split(" ")
		list1.append(int(vals[0]))
		list2.append(int(vals[len(vals)-1].strip()))

list1.sort()
list2.sort()

total = 0
for i in range(len(list1)):
	total += abs(list1[i]-list2[i])

print('part1: '+str(total))

def count(list, num):
	total = 0
	for val in list:
		if val == num:
			total += 1
	return total

''' similarity score: list1_n * count(list2, n) '''

sim_score = 0
for val in list1:
	sim_score += val * count(list2, val)

print('part2: '+str(sim_score))