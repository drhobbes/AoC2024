coords = []
field = []

with open('day04_babyinput1.txt','r') as f:
    y = 0
    for line in f:
        field.append(line)
        x = line.find('#')
        start = 0
        while x != -1:
            coords.append([x,y])
            start = x+1
            x = line.find('#',start)
        y += 1

''' for every pair of coordinates, what is the line connecting them and
    is there any other coordinate on that line '''
