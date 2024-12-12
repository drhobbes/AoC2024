''' 2018 day 05 '''
from string import ascii_lowercase

with open('day06_bonusinput.txt','r') as f:
  seq = f.readline().strip()

def find_pair(line):
  for i in range(len(line)-1):
    if abs(ord(line[i])-ord(line[i+1])) == 32:
      return i
  return -1

def collapse(seq):
  pair = find_pair(seq)
  while pair != -1:
    seq = seq[:pair]+seq[pair+2:]
    pair = find_pair(seq)
  return len(seq)

shortest = collapse(seq[:])
print('part 1:',shortest)

def remove(c, seq):
  result = ''
  for char in seq:
    if char.lower() != c.lower():
      result += char
  return result

removed = {}
for ltr in ascii_lowercase:
  removed[ltr] = remove(ltr, seq)

best_char = ''
for polymer in removed:
  new_len = collapse(removed[polymer])
  print('removing',polymer,'resulted in length',new_len)
  if new_len < shortest:
    shortest = new_len
    best_char = polymer
print('part 2:',shortest,best_char)
