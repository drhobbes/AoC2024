answers = []
values = []
with open('day07_input.txt','r') as f:
	for line in f:
		key = int(line.split(':')[0])
		nums = [int(x) for x in line[line.find(':')+1:].strip().split(' ')]
		answers.append(key)
		values.append(nums)

def try_all(index, vals, try_cat):
	ans_array = [vals[0]]
	for num in vals[1:]:
		add_ans_array = [num + val for val in ans_array]
		mul_ans_array = [num * val for val in ans_array]
		if try_cat:
			cat_ans_array = [int(str(val)+str(num)) for val in ans_array]
		ans_array = add_ans_array
		ans_array.extend(mul_ans_array)
		if try_cat:
			ans_array.extend(cat_ans_array)
	return answers[index] in ans_array

part1_total = 0
part2_total = 0
for i in range(len(answers)):
	part1 = try_all(i, values[i], False)
	part1_total += answers[i] if part1 else 0
	part2_total += answers[i] if part1 else 0
	if not part1:
		part2_total += answers[i] if try_all(i, values[i], True) else 0
print('part 1:', part1_total)
print('part 2:', part2_total)