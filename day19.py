patterns = []
with open('day19_input.txt','r') as f:
    for line in f:
        if ',' in line:
            towels = [x.strip() for x in line.split(',')]
        elif len(line.strip()) == 0:
            continue
        else: patterns.append(line.strip())

known_patterns = {}  # memoization my beloved

def fit_pattern(pattern, towels):
    if len(pattern) == 0:
        return 1

    possible = 0
    if pattern in known_patterns:
        possible += known_patterns[pattern]
    else:        
        for towel in towels:
            if pattern.startswith(towel):
                num_ways = fit_pattern(pattern[len(towel):], towels)
                possible += num_ways
                if pattern not in known_patterns:
                    known_patterns[pattern] = 0
                known_patterns[pattern] += num_ways
    return possible

count = 0
total = 0
for pattern in patterns:
    result = fit_pattern(pattern, towels)
    if result > 0:
        count += 1
        total += result
print('\npart 1:',count)
print('part 2:',total)
