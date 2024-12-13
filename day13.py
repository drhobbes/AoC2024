machines = []
with open('day13_input.txt','r') as f:
  for line in f:
    if len(line.strip())>0:
      parts = line.split(':')[1].strip().split(',')
      if line.startswith('Button'):
        x = int(parts[0].strip().split('+')[1])
        y = int(parts[1].strip().split('+')[1])
        if 'A' in line:
          machine = {}
          machine['A'] = (x,y)
        elif 'B' in line:
          machine['B'] = (x,y)
      elif line.startswith('Prize'):
        x = int(parts[0].strip().split('=')[1])
        y = int(parts[1].strip().split('=')[1])
        machine['Prize'] = (x,y)
        machines.append(machine)

def push_A(machine, claw_loc):
  claw_loc[0] -= machine['A'][0]
  claw_loc[1] -= machine['A'][1]
  return 3

total = 0
for machine in machines:
  machine_cost = 0
  claw_loc = [machine['Prize'][0], machine['Prize'][1]]

  a_count = 0
  while a_count <= 100:
    if claw_loc[0] % machine['B'][0] == 0 and claw_loc[1] % machine['B'][1] == 0 and claw_loc[0]//machine['B'][0] == claw_loc[1]//machine['B'][1]:
      break
    a_count += 1
    machine_cost += push_A(machine, claw_loc)
  
  num_b = claw_loc[0]//machine['B'][0]
  machine_cost += num_b
  claw_loc[0] -= machine['B'][0] * num_b
  claw_loc[1] -= machine['B'][1] * num_b
  if claw_loc == [0,0]:
    total += machine_cost
print('part 1:',total)