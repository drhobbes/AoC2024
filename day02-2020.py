def validate(policy, pwd):
    parts = policy.split(' ')
    letter = parts[1]
    min_count = int(parts[0].split('-')[0])
    max_count = int(parts[0].split('-')[1])
    actual_count = pwd.count(letter)
    return min_count <= actual_count <= max_count

count = 0
with open('day02-2020_input.txt','r') as f:
    for line in f:
        parts = line.split(':')
        if validate(parts[0], parts[1].strip()):
            count += 1

print('part 1:',count)

def other_validate(policy, pwd):
    parts = policy.split(' ')
    letter = parts[1]
    index_1 = int(parts[0].split('-')[0])-1
    index_2 = int(parts[0].split('-')[1])-1
    return (pwd[index_1] == letter) ^ (pwd[index_2] == letter)

count = 0
with open('day02-2020_input.txt','r') as f:
    for line in f:
        parts = line.split(':')
        if other_validate(parts[0], parts[1].strip()):
            count += 1

print('part 2:',count)
