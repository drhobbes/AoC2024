import re

cmd_str = re.compile("mul\([0-9]{1,3},[0-9]{1,3}\)|do\(\)|don't\(\)")

mult = []
with open('day03_input.txt','r') as f:
    for line in f:
        mult.extend(cmd_str.findall(line))

def process_cmd(cmd):
    x = int(cmd[4:cmd.find(',')])
    y = int(cmd[cmd.find(',')+1:len(cmd)-1])
    return x*y

total = 0
for cmd in mult:
    if cmd[:4] == 'mul(':
        total += process_cmd(cmd)
print('part 1:',total)

total = 0
active = True
for cmd in mult:
    if cmd == "don't()":
        active = False
    elif not active and cmd == "do()":
        active = True
    elif active and cmd != "do()":
        total += process_cmd(cmd)
print('part 2:',total)
