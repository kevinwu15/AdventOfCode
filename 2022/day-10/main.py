def get_input():
    f = open("2022/day-10/input.txt", "r")
    puzzle_input = f.read().strip().split("\n")
    return puzzle_input

interesting = [20, 60, 100, 140, 180, 220]

def part1(puzzle_input):
    queue = []
    register = 1
    total = 0

    for i in range(len(puzzle_input)):
        queue.append(0)
        if "addx" in puzzle_input[i]:
            change = int(puzzle_input[i].split(" ")[1])
            queue.append(change)
    
    for cycle in range(1, len(queue) + 1):
        if cycle in interesting:
            total += register * cycle
        register += queue.pop(0)
        
    return total


def part2(puzzle_input):
    queue = []
    register = 1
    for i in range(len(puzzle_input)):
        if "addx" in puzzle_input[i]:
            change = int(puzzle_input[i].split(" ")[1])
            queue.append(0)
            queue.append(change)
        if "noop" in puzzle_input[i]:
            queue.append(0)

    sprite = 1
    row = -1
    line = ""
    board = []
    for cycle in range(1, len(queue) + 1):
        if (cycle - 1) % 40 == 0:
            row += 1
            if row != 0:
                board.append(line)
                line = ""
        index = cycle - (40 * row) - 1
        if index >= sprite - 1 and index <= sprite + 1:
            line += "#"
        else:
            line += "."
        register += queue.pop(0)
        sprite = register
    board.append(line)
    return board

puzzle_input = get_input()

print("Part 1: {}".format(part1(puzzle_input)))

board = part2(puzzle_input)
g = open("2022/day-10/result.txt", "a")
for i in board:
    g.write(i + '\n')