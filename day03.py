''' because i don't want to figure out regular expressions this morning '''
def verify_command(cmd):
	# basic check
	if cmd[:4] != 'mul(':
		return False

	# verify first number
	comma = cmd.find(',')
	if comma > 7 or comma == -1:
		return False
	if not cmd[4:comma].isnumeric():
		return False

	# verify second number
	close = cmd.find(')',comma)
	if close-comma > 4:
		return False
	if not cmd[comma+1:close].isnumeric():
		return False
	return True

instructions = []
with open("day03_input.txt",'r') as f:
	for line in f:
		while line.find('mul(') != -1:
			start = line.find('mul(')
			end = line.find(')',start)
			if verify_command(line[start:end+1]):
				instructions.append(line[start:end+1])
				line = line[end+1:]
			else:
				line = line[start+4:]

def process_cmd(cmd):
	x = int(cmd[4:cmd.find(',')])
	y = int(cmd[cmd.find(',')+1:cmd.find(')')])
	return x*y

total = 0
for cmd in instructions:
	total += process_cmd(cmd)
print('part 1:',total)

instructions = []
with open('day03_input.txt','r') as f:
	active = True
	for line in f:
		while line.find('mul(') != -1:
			if not active:
				# figure out where we can start processing commands again
				find_do = line.find('do()')
				if find_do != -1:
					active = True
					line = line[find_do+4:]
				else:
					line = ""
			elif active:
				find_dont = line.find("don't()")
				find_cmd = line.find('mul(')
				if find_dont != -1 and (find_cmd == -1 or find_dont < find_cmd):
					active = False
					line = line[find_dont+7:]
				else:
					end = line.find(')',find_cmd)
					if (verify_command(line[find_cmd:end+1])):
						instructions.append(line[find_cmd:end+1])
						line = line[end+1:]
					else:
						line = line[find_cmd+4:]
			
total = 0
for cmd in instructions:
	total += process_cmd(cmd)
print('part 2:',total)
