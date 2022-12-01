def get_input():
    f = open("2022/day-01/input.txt", "r")
    puzzle_input = f.read().strip().split("\n")

    return puzzle_input


def part1(puzzle_input):
    prevSum = 0
    sum = 0
    for i in range(len(puzzle_input) - 1):
        if puzzle_input[i] == "" or i == len(puzzle_input) - 1:
            if sum >= prevSum:
                prevSum = sum
            sum = 0
        else:
            sum += int(puzzle_input[i])

    return prevSum

def part2(puzzle_input):
    top = [0, 0, 0]
    sum = 0
    for i in range(len(puzzle_input) - 1):
        if puzzle_input[i] == "" or i == len(puzzle_input) - 1:
            if sum >= top[0]:
                top[2] = top[1]
                top[1] = top[0]
                top[0] = sum
            elif sum >= top[1]:
                top[2] = top[1]
                top[1] = sum
            elif sum >= top[2]:
                top[2] = sum
            sum = 0
        else:
            sum += int(puzzle_input[i])

    return top[0] + top[1] + top[2]

puzzle_input = get_input()

print("Part 1: {}".format(part1(puzzle_input)))
print("Part 2: {}".format(part2(puzzle_input)))