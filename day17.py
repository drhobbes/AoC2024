program = []
with open('day17_input.txt','r') as f:
    a = int(f.readline().split(':')[1].strip())
    b = int(f.readline().split(':')[1].strip())
    c = int(f.readline().split(':')[1].strip())
    f.readline()
    program = [int(x) for x in f.readline().split(':')[1].strip().split(',')]

def print_registers(a,b,c):
    print('A:',a,'B:',b,'C:',c)

def run_program(a):
    b = 0
    c = 0
    inst_ptr = 0
    output = []
    while inst_ptr < len(program):
        operand = program[inst_ptr+1]
        if program[inst_ptr] in [0,2,5,6,7]: # opcodes 1 and 3 use literal, 4 does not use operand
            if operand == 4: operand = a
            elif operand == 5: operand = b
            elif operand == 6: operand = c
        match program[inst_ptr]:
            case 0:
                #print('a=a//8')
                a = a//(2**operand)
            case 1:
                #print('b=b^'+str(operand))
                b = b^operand
            case 2:
                #print('b=a%8')
                b = operand%8
            case 3:
                #if a != 0: print('GOTO 0')
                inst_ptr = operand-2 if a != 0 else inst_ptr
            case 4:
                #print('b=b^c')
                b = b^c
            case 5:
                #print('out(b)')
                output.append(str(operand%8))
            case 6:
                b = a//(2**operand)
            case 7:
                #print('c=a//2**b')
                c = a//(2**operand)
        inst_ptr += 2
        #print_registers(a,b,c)
    return output
print('part 1:',','.join(run_program(a)))
