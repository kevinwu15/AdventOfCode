def get_input():
    f = open("2022/day-03/input.txt", "r")
    puzzle_input = f.read().strip().split("\n")
    return puzzle_input

letters = {}
for i in range(97, 123):
    letters[chr(i)] = i - 96
    letters[chr(i - 32)] = i - 70

def part1(puzzle_input, letters):
    sum = 0
    for i in puzzle_input:
        chars = []
        first = slice(0, len(i) // 2)
        second = slice(len(i) // 2, len(i))
        for j in i[first]:
            chars.append(j)
        for k in i[second]:
            if k in chars:
                sum += letters.get(k)
                break
    return sum
                
def part2(puzzle_input, letters):
    sum = 0
    for i in range(0, len(puzzle_input) - 2, 3):
        layerOne = []
        layerTwo = []
        for j in puzzle_input[i]:
            layerOne.append(j)
        for k in puzzle_input[i + 1]:
            if k in layerOne:
                layerTwo.append(k)
        for l in puzzle_input[i + 2]:
            if l in layerTwo:
                sum += letters.get(l)
                break
    return sum

puzzle_input = get_input()

print("Part 1: {}".format(part1(puzzle_input, letters)))
print("Part 2: {}".format(part2(puzzle_input, letters)))