def get_input():
    f = open("2022/day-04/input.txt", "r")
    puzzle_input = f.read().strip().split("\n")
    return puzzle_input

def part1(puzzle_input):
    count = 0
    for i in puzzle_input:
        (e1, e2) = i.split(',')
        (e11, e12) = e1.split('-')
        (e21, e22) = e2.split('-')
        if (int(e11) <= int(e21)) and (int(e22) <= int(e12)) or (int(e21) <= int(e11)) and (int(e12) <= int(e22)):
            count += 1
    return count

def part2(puzzle_input):
    count = 0
    for i in puzzle_input:
        (e1, e2) = i.split(',')
        (e11, e12) = e1.split('-')
        (e21, e22) = e2.split('-')
        if int(e11) <= int(e21) and int(e12) >= int(e21):
            count += 1
        elif int(e21) <= int(e11) and int(e22) >= int(e11):
            count += 1
    return count

puzzle_input = get_input()

print("Part 1: {}".format(part1(puzzle_input)))
print("Part 2: {}".format(part2(puzzle_input)))