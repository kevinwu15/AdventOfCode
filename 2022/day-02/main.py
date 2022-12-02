def get_input():
    f = open("2022/day-02/input.txt", "r")
    puzzle_input = f.read().strip().split("\n")
    return puzzle_input

code = {"A": "rock", "B": "paper", "C": "scissors", "X": "rock", "Y": "paper", "Z": "scissors"}
choices = ["rock", "paper", "scissors"]
scores = [1, 2, 3]

def part1(puzzle_input):
    score = 0
    for i in puzzle_input:
        playerChoice = code.get(i[2])
        pIndex = choices.index(playerChoice)
        score += scores[pIndex]
        oppChoice = code.get(i[0])
        oIndex = choices.index(oppChoice)
        if pIndex == oIndex:
            score += 3
        if pIndex - 1 == oIndex or pIndex + 2 == oIndex:
            score += 6
    return score

def part2(puzzle_input):
    score = 0
    for i in puzzle_input:
        oppChoice = code.get(i[0])
        oIndex = choices.index(oppChoice)
        result = i[2]
        if result == 'X':
            try:
                playerChoice = choices[oIndex - 1]
            except IndexError:
                playerChoice = choices[oIndex + 2]
            pIndex = choices.index(playerChoice)
            score += scores[pIndex]
        elif result == 'Y':
            score += (scores[oIndex] + 3)
        else:
            try:
                playerChoice = choices[oIndex + 1]
            except IndexError:
                playerChoice = choices[oIndex - 2]
            pIndex = choices.index(playerChoice)
            score += (scores[pIndex] + 6)
    return score

puzzle_input = get_input()

print("Part 1: {}".format(part1(puzzle_input)))
print("Part 2: {}".format(part2(puzzle_input)))