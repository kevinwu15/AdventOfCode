def get_input():
    f = open("2022/day-07/input.txt", "r")
    line = True
    puzzle_input = []
    while line:
        line = f.readline()
        puzzle_input.append(line.strip("\n").split(" "))
    return puzzle_input

tree = {}

def cd(current, line):
    current = current.split("-")
    if line[2] != "..":
        current.append(line[2])
    else:
        current.pop()
    path = "-".join(current)
    return path

def ls(puzzle_input, current, lineNum):
    subdirectories = []
    while True:
        lineNum += 1
        if puzzle_input[lineNum][0] == "" or puzzle_input[lineNum][0] == "$":
            break
        elif puzzle_input[lineNum][0] != "$":
            if puzzle_input[lineNum][0] == "dir":
                subdirectories.append(current + "-" + puzzle_input[lineNum][1])
            else:
                subdirectories.append(int(puzzle_input[lineNum][0]))

    if all(isinstance(item, int) for item in subdirectories):
        tree[current] = sum(subdirectories)
    else:
        tree[current] = subdirectories
    return lineNum

def recur(tree, currentD):
    total = 0
    if isinstance(tree[currentD], int):
        total += tree[currentD]
    else:
        size = 0
        for i in tree[currentD]:
            if not isinstance(i, int):
                size += recur(tree, i)
            else:
                size += i
        total += size
    return total
    
        
def part1(puzzle_input, tree):
    current = ""
    for i in range(len(puzzle_input)):
        try:
            if puzzle_input[i][1] == "cd":
                current = cd(current, puzzle_input[i])
            if puzzle_input[i][1] == "ls":
                i = ls(puzzle_input, current, i)
        except IndexError:
            continue
    sums = []
    for key in tree:
        sums.append(recur(tree, key))
    answer = 0
    for j in sums:
        if j <= 100000:
            answer += j
    return answer

def part2(puzzle_input, tree):
    current = ""
    for i in range(len(puzzle_input)):
        try:
            if puzzle_input[i][1] == "cd":
                current = cd(current, puzzle_input[i])            
            if puzzle_input[i][1] == "ls":
                i = ls(puzzle_input, current, i)
        except IndexError:
            continue
    sums = []
    for key in tree:
        sums.append(recur(tree, key))
    sums.sort()
    totalSize = recur(tree, "-/")
    freeSpace = 70000000 - totalSize
    target = 30000000 - freeSpace
    for j in sums:
        if j > target:
            return j

puzzle_input = get_input()

print("Part 1: {}".format(part1(puzzle_input, tree)))
print("Part 2: {}".format(part2(puzzle_input, tree)))