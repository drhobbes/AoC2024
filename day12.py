crops = []
with open('day12_input.txt','r') as f:
    for line in f:
        crops.append([x for x in line.strip()])

def find_region(i,j,letter,region):
    if i < 0 or i >= len(crops):
        return
    if j < 0 or j >= len(crops[i]):
        return
    if crops[i][j] != letter or (i,j) in region:
        return

    region.append((i,j))
    find_region(i-1,j,letter,region)
    find_region(i+1,j,letter,region)
    find_region(i,j-1,letter,region)
    find_region(i,j+1,letter,region)

visited = []
regions = []
for i in range(len(crops)):
    for j in range(len(crops[i])):
        if (i,j) not in visited:
            region = []
            find_region(i,j,crops[i][j],region)
            for loc in region:
                visited.append(loc)
            regions.append(region)

def calc_perim(region):
    perim = 0
    for loc in region:
        perim += 1 if (loc[0]-1,loc[1]) not in region else 0
        perim += 1 if (loc[0]+1,loc[1]) not in region else 0
        perim += 1 if (loc[0],loc[1]-1) not in region else 0
        perim += 1 if (loc[0],loc[1]+1) not in region else 0
    return perim

def count_sides(region):
    num_sides = 0
    for loc in region:
        if (loc[0]-1,loc[1]) not in region:
            # top edge, only add if this is the rightmost element
            if (loc[0],loc[1]+1) not in region: # nothing to the right of this in the region
                num_sides += 1
            elif (loc[0]-1,loc[1]+1) in region: # the top edge ends here
                num_sides += 1
        if (loc[0]+1,loc[1]) not in region:
            # bottom edge, only add if this is the rightmost element
            if (loc[0],loc[1]+1) not in region: # nothing to the right of this in the region
                num_sides += 1
            elif (loc[0]+1,loc[1]+1) in region: # the bottom edge ends here
                num_sides += 1
        if (loc[0],loc[1]-1) not in region:
            # left edge, only add if this is the bottom element
            if (loc[0]+1,loc[1]) not in region: # nothing below this in the region
                num_sides += 1
            elif (loc[0]+1,loc[1]-1) in region: # the left edge ends here
                num_sides += 1
        if (loc[0],loc[1]+1) not in region:
            # right edge, only add if this is the bottom element
            if (loc[0]+1,loc[1]) not in region: # nothing below this in the region
                num_sides += 1
            elif (loc[0]+1,loc[1]+1) in region: # the right edge ends here
                num_sides += 1
    return num_sides

p1_total = 0
p2_total = 0
for region in regions:
    p1_total += calc_perim(region)*len(region)
    p2_total += count_sides(region)*len(region)
print('part 1:',p1_total)
print('part 2:',p2_total)
