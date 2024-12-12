stones = {}
with open('day11_input.txt','r') as f:
	line = f.readline().strip().split(' ')
	for num in line:
		stone = int(num)
		if stone not in stones:
			stones[stone] = 1
		else:
			stones[stone] += 1

def change(stone):
	if stone == 0: return 1
	elif len(str(stone)) % 2 == 0:
		split_at = len(str(stone))//2
		return [int(str(stone)[:split_at]), int(str(stone)[split_at:])]
	else: return stone*2024

def blink():
	new_stones = {}
	for stone in stones:
		new_stone = change(stone)
		if isinstance(new_stone, int):
			if new_stone not in new_stones:
				new_stones[new_stone] = stones[stone]
			else:
				new_stones[new_stone] += stones[stone]
		else:
			if new_stone[0] not in new_stones:
				new_stones[new_stone[0]] = stones[stone]
			else:
				new_stones[new_stone[0]] += stones[stone]
			if new_stone[1] not in new_stones:
				new_stones[new_stone[1]] = stones[stone]
			else:
				new_stones[new_stone[1]] += stones[stone]
	return new_stones

for i in range(25): stones = blink()
total = 0
for stone in stones:
	total += stones[stone]
print('part 1:',total)

for i in range(50): stones = blink()
total = 0
for stone in stones:
	total += stones[stone]
print('part 2:',total)