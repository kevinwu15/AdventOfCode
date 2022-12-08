def get_input():
    f = open("2022/day-08/input.txt", "r")
    puzzle_input = []
    line = True
    while line:
        line = [*f.readline().strip()]
        puzzle_input.append(line)
    puzzle_input.pop()
    return puzzle_input

def xVisible(puzzle_input, x, y):
    x2 = x
    tree = puzzle_input[y][x]
    while True:
        try:
            if x == 0:
                return True
            if puzzle_input[y][x - 1] < tree:
                x -= 1
            else:
                while True:
                    if x2 == len(puzzle_input[0]) - 1:
                        return True
                    try:
                        if tree > puzzle_input[y][x2 + 1]:
                            x2 += 1
                        else:
                            return False     
                    except IndexError:
                        return True  
        except IndexError:
            return True

def yVisible(puzzle_input, x, y):
    y2 = y
    tree = puzzle_input[y][x]
    while True:
        try:
            if y == 0:
                return True
            if puzzle_input[y - 1][x] < tree:
                y -= 1
            else:
                while True:
                    if y2 == len(puzzle_input) - 1:
                        return True
                    try:
                        if tree > puzzle_input[y2 + 1][x]:
                            y2 += 1
                        else:
                            return False     
                    except IndexError:
                        return True  
        except IndexError:
            return True

def isVisible(puzzle_input, x, y):
    if xVisible(puzzle_input, x, y) or yVisible(puzzle_input, x, y):
        return True
    return False

def leftScore(puzzle_input, x, y):
    score = 0
    tree = puzzle_input[y][x]
    if x == 0:
        return score
    while True:
        try:
            if x == 0:
                return score
            score += 1
            if tree > puzzle_input[y][x - 1]:
                x -= 1
            else:
                return score
        except IndexError:
            return score

def rightScore(puzzle_input, x, y):
    score = 0
    tree = puzzle_input[y][x]
    if x == len(puzzle_input[0]) - 1:
        return score
    while True:
        try:
            if x == len(puzzle_input[0]) - 1:
                return score
            score += 1
            if tree > puzzle_input[y][x + 1]:
                x += 1
            else:
                return score
        except IndexError:
            return score
    
def upScore(puzzle_input, x, y):
    score = 0
    tree = puzzle_input[y][x]
    if y == 0:
        return score
    while True:
        try:
            if y == 0:
                return score
            score += 1
            if tree > puzzle_input[y - 1][x]:
                y -= 1
            else:
                return score
        except IndexError:
            return score

def downScore(puzzle_input, x, y):
    score = 0
    tree = puzzle_input[y][x]
    if y == len(puzzle_input) - 1:
        return score
    while True:
        try:
            if y == len(puzzle_input) - 1:
                return score
            score += 1
            if tree > puzzle_input[y + 1][x]:
                y += 1
            else:
                return score
        except IndexError:
            return score


def part1(puzzle_input):
    count = 0
    for y in range(len(puzzle_input)):
        for x in range(len(puzzle_input[0])):
            if isVisible(puzzle_input, x, y):
                count += 1
    return count
        

def part2(puzzle_input):
    maxScore = 0
    for y in range(len(puzzle_input)):
        for x in range(len(puzzle_input[0])):
            temp = leftScore(puzzle_input, x, y) * rightScore(puzzle_input, x, y) * upScore(puzzle_input, x, y) * downScore(puzzle_input, x, y)
            if temp > maxScore:
                maxScore = temp
    return maxScore

puzzle_input = get_input()

print("Part 1: {}".format(part1(puzzle_input)))
print("Part 2: {}".format(part2(puzzle_input)))