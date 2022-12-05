def get_boxes():
    f = open("2022/day-05/input.txt", "r")
    puzzle_input = []
    columns = 9
    for _ in range(columns):
        puzzle_input.append([])
    line = True
    while line:
        line = f.readline().strip("\n") + " "
        if "[" not in line:
            break
        else:
            col = 0
            for j in range(0, len(line), 4):
                try:
                    if line[j: j + 4] != "    ":
                        puzzle_input[col].append(line[j: j + 4])
                    col += 1
                except IndexError:
                    continue
    return puzzle_input

def get_moves():
    f = open("2022/day-05/input.txt", "r")
    puzzle_input = []
    start = False
    line = f.readline()
    while line:
        line = f.readline()
        if start:
            puzzle_input.append(line.strip())
        if line.strip() == "":
            start = True
    puzzle_input.pop()
    return puzzle_input


def part1(boxes, moves):
    for i in moves:
        move_components = i.split(" ")
        for _ in range(int(move_components[1])):
            moved = boxes[int(move_components[3]) - 1].pop(0)
            boxes[int(move_components[5]) - 1].insert(0, moved)
    result = ""
    for col in boxes:
        result += col[0][1]
    return result


def part2(boxes, moves):
    for i in moves:
        stack = []
        move_components = i.split(" ")
        for _ in range(int(move_components[1])):
            moved = boxes[int(move_components[3]) - 1].pop(0)
            stack.append(moved)
        for j in range(len(stack)):
            boxes[int(move_components[5]) - 1].insert(0, stack[len(stack) - 1 - j])
    result = ""
    for col in boxes:
        result += col[0][1]
    return result

boxesInput1 = get_boxes()
boxesInput2 = get_boxes()
movesInput = get_moves()

print("Part 1: {}".format(part1(boxesInput1, movesInput)))
print("Part 2: {}".format(part2(boxesInput2, movesInput)))