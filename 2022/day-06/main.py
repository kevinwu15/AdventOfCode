def get_input():
    f = open("2022/day-06/input.txt", "r")
    puzzle_input = f.read().strip()
    return puzzle_input


def part1(puzzle_input):
    letters = []
    count = 0
    for i in puzzle_input:
        if i in letters:
            index = letters.index(i)
            del letters[0:index + 1]
        letters.append(i)
        count += 1
        if len(letters) == 4:
            return count


def part2(puzzle_input):
    letters = []
    count = 0
    for i in puzzle_input:
        if i in letters:
            index = letters.index(i)
            del letters[0:index + 1]
        letters.append(i)
        count += 1
        if len(letters) == 14:
            return count


puzzle_input = get_input()

print("Part 1: {}".format(part1(puzzle_input)))
print("Part 2: {}".format(part2(puzzle_input)))