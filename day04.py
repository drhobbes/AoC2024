chars = []
with open('day04_input.txt','r') as f:
	for line in f:
		chars.append(line.strip())

def find_R(xi,xj):
	if xj >= len(chars[xi])-3: return 0
	return 1 if chars[xi][xj:xj+4] == "XMAS" else 0

def find_L(xi, xj):
	if xj <= 2: return 0
	return 1 if chars[xi][xj-3:xj+1] == "SAMX" else 0

def find_U(xi, xj):
	if xi <= 2: return 0
	return 1 if chars[xi-1][xj] == 'M' and chars[xi-2][xj] == 'A' and chars[xi-3][xj] == 'S' else 0

def find_D(xi, xj):
	if xi >= len(chars)-3: return 0
	return 1 if chars[xi+1][xj] == 'M' and chars[xi+2][xj] == 'A' and chars[xi+3][xj] == 'S' else 0

def find_NE(xi, xj):
	if xi <= 2 or xj >= len(chars[xi])-3: return 0
	return 1 if chars[xi-1][xj+1] == 'M' and chars[xi-2][xj+2] == 'A' and chars[xi-3][xj+3] == 'S' else 0

def find_SE(xi, xj):
	if xi >= len(chars)-3 or xj >= len(chars[xi])-3: return 0
	return 1 if chars[xi+1][xj+1] == 'M' and chars[xi+2][xj+2] == 'A' and chars[xi+3][xj+3] == 'S' else 0

def find_SW(xi, xj):
	if xi >= len(chars)-3 or xj <= 2: return 0
	return 1 if chars[xi+1][xj-1] == 'M' and chars[xi+2][xj-2] == 'A' and chars[xi+3][xj-3] == 'S' else 0

def find_NW(xi, xj):
	if xi <= 2 or xj <= 2: return 0
	return 1 if chars[xi-1][xj-1] == 'M' and chars[xi-2][xj-2] == 'A' and chars[xi-3][xj-3] == 'S' else 0

def getAllXMAS(i,j):
	return find_R(i,j)+find_L(i,j)+find_U(i,j)+find_D(i,j)+find_NE(i,j)+find_NW(i,j)+find_SE(i,j)+find_SW(i,j)

total = 0
for i in range(len(chars)):
	start = 0
	j = chars[i].find('X')
	while j != -1:
		total += getAllXMAS(i,j)
		start = j+1
		j = chars[i].find('X', start)
print('part 1:',total)

def findXMAS(ai, aj):
	if ai == 0 or ai == len(chars)-1 or aj == 0 or aj == len(chars[ai])-1: return 0
	word = chars[ai-1][aj-1] + chars[ai+1][aj-1] + chars[ai+1][aj+1] + chars[ai-1][aj+1]
	return 1 if word in ['MMSS','SMMS','SSMM','MSSM'] else 0

total = 0
for i in range(len(chars)):
	start = 0
	j = chars[i].find('A')
	while j != -1:
		total += findXMAS(i,j)
		start = j+1
		j = chars[i].find('A',start)
print('part 2:',total)