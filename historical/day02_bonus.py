''' 2015 day 19 '''
import sys

replacements = {}
reverse = {}
with open('day19-2015_input.txt','r') as f:
    for line in f:
        if '=>' in line:
            parts = line.split(" ")
            reverse[parts[2].strip()] = parts[0]
            if parts[0] in replacements:
                replacements[parts[0]].append(parts[2].strip())
            else:
                replacements[parts[0]] = [parts[2].strip()]
        elif len(line.strip()) > 0:
            starter = line.strip()

total = 0
unique = []
for key in replacements:
    start_index = 0
    while starter.find(key, start_index) != -1:
        index = starter.find(key, start_index)
        for val in replacements[key]:
            molecule = starter[:index]+val+starter[index+len(key):]
            if molecule not in unique:
                unique.append(molecule)
        start_index = index+len(key)
print('part 1:',len(unique))
print(len(starter))

''' for part 2, we want to work backwards '''
def synthesize(mol, num_steps):
    min_steps = sys.maxsize

    # base case
    if len(mol) > 1 and 'e' in mol:
        return min_steps
    elif mol == 'e':
        print('found one:',num_steps)
        return num_steps

    # incredibly inefficient recursive case
    for key in reverse:
        key_index = mol.find(key)
        present = key_index != -1
        while key_index != -1:
            new_mol = mol[:key_index]+reverse[key]+mol[key_index+len(key):]
            steps = synthesize(new_mol, num_steps+1)
            if steps < min_steps:
                min_steps = steps
            key_index = mol.find(key, key_index+len(key))
    if min_steps == sys.maxsize:
        print('dead end ('+str(num_steps)+'): '+mol)
    return min_steps

print('part 2:',synthesize(starter,0))
