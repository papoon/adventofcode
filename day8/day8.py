with open('input.txt') as f:
    data = f.readlines()
    data = [x.strip('\n.') for x in data]

instructions = { i:data[i] for i in range(len(data)) }

def accumalator(instructions):
    instructions_executed = {}
    k = accumulator = 0
    while k < len(instructions):
        if k in instructions_executed:
            break
        v = instructions[k]
        if 'acc' == v[:3]:
            accumulator += int(v[3:])
            instructions_executed[k] = v
        elif 'jmp' == v[:3]:
            instructions_executed[k] = v
            k += int(v[3:])-1
        else:
            instructions_executed[k] = v
        k += 1

    return accumulator, instructions_executed

acc, instructions_executed = accumalator(instructions)
print(acc)

def fix_acumulator(instructions, instructions_executed):
    for k,v in reversed(instructions_executed.items()):
        if 'acc' in v:
            continue
        instructions_copy = instructions.copy()
        instructions[k] =  v.replace('jmp','nop') if 'jmp' in v else v.replace('nop','jmp')
        accumulator, instructions_executed = accumalator(instructions)
        if len(instructions)-1 in instructions_executed:
            return accumulator,instructions
        else:
            instructions = instructions_copy

acc, instructions_executed = fix_acumulator(instructions,instructions_executed)
print(acc)
