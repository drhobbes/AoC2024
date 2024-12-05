with open('day05_bonusinput.txt','r') as f:
    digits = f.readline().strip()

i = len(digits)-1
total = 0
match = False
while i >= -1:
    if match:
        total += int(digits[i])
    
    if digits[i] == digits[i-1]:
        if not match:
            match = True
    else:
        match = False

    i -= 1

print('part 1:',total)

step = len(digits)//2
total = 0
for i in range(len(digits)//2):
    if digits[i] == digits[i+step]:
        total += int(digits[i])*2
print('part 2:',total)
