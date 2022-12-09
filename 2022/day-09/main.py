def get_input():
    f = open("2022/day-09/input.txt", "r")
    puzzle_input = []
    line = True
    while line:
        line = f.readline()
        puzzle_input.append(line.strip().split(" "))
    puzzle_input.pop()
    return puzzle_input

def moveTail(x, y, headX, headY):
    if headY == y and headX == x + 2:
        x += 1
    elif headY == y and headX == x - 2:
        x -= 1
    elif headX == x and headY == y + 2:
        y += 1
    elif headX == x and headY == y - 2:
        y -= 1
    elif headY > y and headX > x + 1:
        y += 1
        x += 1
    elif headY > y and headX < x - 1:
        y += 1
        x -= 1
    elif headY < y and headX > x + 1:
        y -= 1
        x += 1
    elif headY < y and headX < x - 1:
        y -= 1
        x -= 1
    elif headX > x and headY > y + 1:
        y += 1
        x += 1
    elif headX > x and headY < y - 1:
        y -= 1
        x += 1
    elif headX < x and headY > y + 1:
        y += 1
        x -= 1
    elif headX < x and headY < y - 1:
        y -= 1
        x -= 1
    return [x, y]

def tailRecur(positions, locations, length):
    for i in range(length):
        tailLocation = moveTail(int(positions[i + 1][0]), int(positions[i + 1][1]), int(positions[i][0]), int(positions[i][1]))
        if tailLocation == positions[i + 1]:
            break
        else:
            positions[i + 1] = tailLocation
        if i == length - 1:
            if tailLocation not in locations:
                locations.append(tailLocation)

def move(line, positions, locations, length):
    headX = int(positions[0][0])
    headY = int(positions[0][1])
    if line[0] == 'R':
        for _ in range(int(line[1])):
            headX += 1
            positions[0][0] = headX
            tailRecur(positions, locations, length)

    if line[0] == 'L':
        for _ in range(int(line[1])):
            headX -= 1
            positions[0][0] = headX
            tailRecur(positions, locations, length)

    if line[0] == 'U':
        for _ in range(int(line[1])):
            headY += 1
            positions[0][1] = headY
            tailRecur(positions, locations, length)

    if line[0] == 'D':
        for _ in range(int(line[1])):
            headY -= 1
            positions[0][1] = headY
            tailRecur(positions, locations, length)

    return [positions, locations]
            

def part1(puzzle_input):
    positions = []
    locations = [[0, 0]]
    for i in range(2):
        positions.append([0, 0])
    for i in puzzle_input:
        output = move(i, positions, locations, 1)
        positions = output[0]
        locations = output[1]
    return len(locations)


def part2(puzzle_input):
    positions = []
    locations = [[0, 0]]
    for _ in range(10):
        positions.append([0, 0])
    for i in puzzle_input:
        output = move(i, positions, locations, 9)
        positions = output[0]
        locations = output[1]
    return len(locations)

puzzle_input = get_input()

print("Part 1: {}".format(part1(puzzle_input)))
print("Part 2: {}".format(part2(puzzle_input)))