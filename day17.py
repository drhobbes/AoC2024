program = []
with open('day17_input.txt','r') as f:
    a = int(f.readline().split(':')[1].strip())
    b = int(f.readline().split(':')[1].strip())
    c = int(f.readline().split(':')[1].strip())
    f.readline()
    program = [int(x) for x in f.readline().split(':')[1].strip().split(',')]

inst_ptr = 0

def print_registers():
    print('A:',a,'B:',b,'C:',c)

output = []
while inst_ptr < len(program):
    operand = program[inst_ptr+1]
    if program[inst_ptr] in [0,2,5,6,7]: # opcodes 1 and 3 use literal, 4 does not use operand
        if operand == 4: operand = a
        elif operand == 5: operand = b
        elif operand == 6: operand = c
    match program[inst_ptr]:
        case 0:
            a = a//(2**operand)
        case 1:
            b = b^operand
        case 2:
            b = operand%8
        case 3:
            inst_ptr = operand-2 if a != 0 else inst_ptr
        case 4:
            b = b^c
        case 5:
            output.append(str(operand%8))
        case 6:
            b = a//(2**operand)
        case 7:
            c = a//(2**operand)
    inst_ptr += 2
    #print_registers()
print(','.join(output))
