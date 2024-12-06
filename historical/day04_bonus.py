import math

coords = {}
field = []

with open('day04_bonusinput.txt','r') as f:
    y = 0
    for line in f:
        field.append(line)
        x = line.find('#')
        start = 0
        while x != -1:
            coords[x,y] = []
            start = x+1
            x = line.find('#',start)
        y += 1

def is_blocked(a1, a2):
    dx = a1[0]-a2[0]
    dy = a1[1]-a2[1]
    if dy == 0:
        return '#' in field[a1[1]][min(a1[0],a2[0])+1:max(a1[0],a2[0])]
    elif dx == 0:
        btw = ''
        for i in range(min(a1[1],a2[1])+1,max(a1[1],a2[1])):
            btw += field[i][a1[0]]
        return '#' in btw
    elif dx == -1 or dx == 1 or dy == -1 or dy == 1:
        return False
    else:
        for i in range(2,len(field[0])//2):
            if dx%i == 0 and dy%i == 0:
                x = a1[0]-(dx//i)
                y = a1[1]-(dy//i)
                while a2[0] != x and a2[1] != y:
                    if field[y][x] == '#':
                        return True
                    x -= (dx//i)
                    y -= (dy//i)
        return False

for i in range(len(coords.keys())):
    c1 = list(coords.keys())[i]
    for j in range(i+1,len(coords.keys())):
        c2 = list(coords.keys())[j]
        if not is_blocked(c1,c2):
            coords[c1].append(c2)
            coords[c2].append(c1)

max_key = list(coords.keys())[0]
max_view = len(coords[max_key])
for key in coords:
    if len(coords[key]) > max_view:
        max_view = len(coords[key])
        max_key = key
print('part 1:',max_view,max_key)

# given max key and starting with dx = 0 rotate clockwise and find 200th
north = [coord for coord in coords[max_key] if coord[0] == max_key[0] and coord[1] < max_key[1]]
east = [coord for coord in coords[max_key] if coord[0] > max_key[0] and coord[1] == max_key[1]]
south = [coord for coord in coords[max_key] if coord[0] == max_key[0] and coord[1] > max_key[1]]
west = [coord for coord in coords[max_key] if coord[0] < max_key[0] and coord[1] == max_key[1]]

ne = [coord for coord in coords[max_key] if coord[0] > max_key[0] and coord[1] < max_key[1]]
se = [coord for coord in coords[max_key] if coord[0] > max_key[0] and coord[1] > max_key[1]]
sw = [coord for coord in coords[max_key] if coord[0] < max_key[0] and coord[1] > max_key[1]]
nw = [coord for coord in coords[max_key] if coord[0] < max_key[0] and coord[1] < max_key[1]]

in_order = north, ne, east, se, south, sw, west, nw
total = 0
for group in in_order:
    total += len(group)
    print('added group',total)

# sample input 130 when we hit nw (x=11), actual input 185 when we hit nw (x=23)
# find angle between max_key and coordinate, order increasing

def find_angle(coord):
    opp = abs(coord[1]-max_key[1])
    adj = abs(coord[0]-max_key[0])
    return math.atan(opp/adj)

angles = []
for coord in nw:
    angles.append([find_angle(coord),coord])

sorted_angles = sorted(angles, key=lambda x: x[0])
count = 185
for coord in sorted_angles:
    count += 1
    if count >= 199 and count < 202:
        print(count,coord[1])
