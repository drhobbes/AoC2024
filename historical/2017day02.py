nums = []
with open('2017day02_input.txt','r') as f:
    for line in f:
        nums.append([int(x) for x in line.strip().split('\t')])

diff = []
for row in nums:
    diff.append(max(row)-min(row))
print('part 1:',sum(diff))

total = 0
for row in nums:
    for i in range(len(row)-1):
        val1 = row[i]
        for j in range(i, len(row)):
            val2 = row[j]
            if val1 != val2 and max(val1,val2)%min(val1,val2) == 0:
                total += max(val1,val2)//min(val1,val2)
print('part 2:',total)
