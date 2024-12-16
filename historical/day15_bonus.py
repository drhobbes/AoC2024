fish = {}
with open('day15_bonusinput.txt','r') as f:
  fish_states = [int(x) for x in f.readline().strip().split(',')]
  for state in fish_states:
    if state not in fish:
      fish[state] = 0
    fish[state] += 1

def update():
  new_fish = {}
  for key in fish:
    if key == 0:
      if 6 not in new_fish:
        new_fish[6] = 0
      new_fish[6] += fish[key]
      if 8 not in new_fish:
        new_fish[8] = 0
      new_fish[8] += fish[key]
    else:
      if key-1 not in new_fish:
        new_fish[key-1] = 0
      new_fish[key-1] += fish[key]
  return new_fish

for i in range(80):
  fish = update()
total = 0
for key in fish:
  total += fish[key]
print('part 1:',total)

for i in range(80,256):
  fish = update()
total = 0
for key in fish:
  total += fish[key]
print('part 2:',total)
