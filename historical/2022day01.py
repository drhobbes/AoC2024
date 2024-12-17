elves = []
with open('2022day01_input.txt','r') as f:
  elf = []
  for line in f:
    if len(line.strip()) == 0:
      elves.append(elf)
      elf = []
    else:
      elf.append(int(line.strip()))

cals = []
for elf in elves:
  cals.append(sum(elf))
print('part 1:',max(cals))

total = 0
for i in range(3):
  total += max(cals)
  cals.remove(max(cals))
print('part 2:',total)
