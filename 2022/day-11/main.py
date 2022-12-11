fileName = "2022/day-11/input.txt"
m = open(fileName, "r")
total = m.read().strip().split("\n")
numMonkeys = int((len(total) + 1) / 7)

def get_input():
    f = open(fileName, "r")
    line = True
    monkeys = []
    number = 0
    lineNum = 0
    for _ in range(numMonkeys):
        monkeys.append([])
    while line:
        line = f.readline()
        if line.strip() == "":
            number += 1
            lineNum = -1

        elif lineNum == 1:
            content = line.strip().split(" ")
            items = []
            for i in range(len(content) - 2):
                items.append(int(content[2 + i].strip(',')))
            monkeys[number].append(items)
        
        elif lineNum == 2:
            content = line.strip().split(" ")
            operations = []
            operations.append(content[len(content) - 2])
            operations.append(content[len(content) - 1])
            monkeys[number].append(operations)

        elif lineNum == 3:
            content = line.strip().split(" ")
            monkeys[number].append(int(content[len(content) - 1]))

        elif lineNum == 4:
            content = line.strip().split(" ")
            monkeys[number].append(int(content[len(content) - 1]))
        
        elif lineNum == 5:
            content = line.strip().split(" ")
            monkeys[number].append(int(content[len(content) - 1]))

        lineNum += 1

    return monkeys

def playRound(monkeyInput, monkeyList, inspectList, monkeyNum):
    for i in monkeyInput[0]:
        worryLevel = i
        inspectList[monkeyNum] += 1
        operation = monkeyInput[1][0]
        if operation == '+':
            if monkeyInput[1][1].isnumeric():
                worryLevel = i + int(monkeyInput[1][1])
            else:
                worryLevel = i + i

        elif operation == '*':
            if monkeyInput[1][1].isnumeric():
                worryLevel = i * int(monkeyInput[1][1])
            else:
                worryLevel = i * i
        worryLevel = worryLevel // 3

        if worryLevel % monkeyInput[2] == 0:
            monkeyList[monkeyInput[3]][0].append(worryLevel)
        else:
            monkeyList[monkeyInput[4]][0].append(worryLevel)
    monkeyInput[0].clear()
    return monkeyList

def playRound2(monkeyInput, monkeyList, inspectList, monkeyNum):
    for i in monkeyInput[0]:
        worryLevel = i
        inspectList[monkeyNum] += 1
        operation = monkeyInput[1][0]
        if operation == '+':
            if monkeyInput[1][1].isnumeric():
                worryLevel = i + int(monkeyInput[1][1])
            else:
                worryLevel = i + i

        elif operation == '*':
            if monkeyInput[1][1].isnumeric():
                worryLevel = i * int(monkeyInput[1][1])
            else:
                worryLevel = i * i

        if worryLevel >= moduloValue:
            worryLevel %= moduloValue

        if worryLevel % monkeyInput[2] == 0:
            monkeyList[monkeyInput[3]][0].append(worryLevel)
        else:
            monkeyList[monkeyInput[4]][0].append(worryLevel)
    monkeyInput[0].clear()
    return monkeyList

inspect = []
for i in range(numMonkeys):
    inspect.append(0)

inspect2 = []
for i in range(numMonkeys):
    inspect2.append(0)


def part1(puzzle_input):
    for _ in range(1, 21):
        for i in range(numMonkeys):
            puzzle_input = playRound(puzzle_input[i], puzzle_input, inspect, i)
    inspect.sort()
    return inspect[numMonkeys - 1] * inspect[numMonkeys - 2]

def part2(puzzle_input):
    for _ in range(1, 10001):
        for i in range(numMonkeys):
            puzzle_input = playRound2(puzzle_input[i], puzzle_input, inspect2, i)
    inspect2.sort()
    return inspect2[numMonkeys - 1] * inspect2[numMonkeys - 2]

puzzle_input = get_input()
puzzle_input2 = get_input()
moduloValue = 1
for i in puzzle_input2:
    moduloValue *= i[2]

print("Part 1: {}".format(part1(puzzle_input)))
print("Part 2: {}".format(part2(puzzle_input2)))