dependencies = {}
updates = []
with open('day05_input.txt','r') as f:
	for line in f:
		if '|' in line:
			first_page = int(line.split('|')[0])
			if first_page in dependencies:
				dependencies[first_page].append(int(line.strip().split('|')[1]))
			else:
				dependencies[first_page] = [int(line.strip().split('|')[1])]
		elif len(line.strip()) != 0:
			updates.append([int(x) for x in line.strip().split(',')])

def correct_order(update):
	for i in range(1,len(update)):
		page = update[i]
		if page in dependencies:
			for other_page in dependencies[page]:
				if other_page in update[:i]: return False
	return True

def fix_order(update):
	i = 1
	while i < len(update):
		page = update[i]
		if page in dependencies:
			for other_page in dependencies[page]:
				if other_page in update[:i]:
					j = update.index(other_page)
					update[j] = page
					update[i] = other_page
					i = 0
		i += 1

total = 0
p2_total = 0
for update in updates:
	if correct_order(update):
		total += update[len(update)//2]
	else:
		fix_order(update)
		p2_total += update[len(update)//2]
print('part 1:',total)
print('part 2:',p2_total)