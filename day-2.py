# test_inst = ["ULL", "RRDDD", "LURDL", "UUUUD"]

with open('day-2-input.txt', 'r') as f:
    instructions = f.read().splitlines()


def bathroom_code(instructions):
    keypad = [
        [None, None, 1, None, None],
        [None, 2, 3, 4, None],
        [5, 6, 7, 8, 9],
        [None, "A", "B", "C", None],
        [None, None, "D", None, None]
    ]
    dirs = {"U": [0, -1], "D": [0, 1], "L": [-1, 0], "R": [1, 0]}

    code = []
    y, x = 2, 0
    for number in instructions:
        for step in number:
            if (
                y + dirs[step][1] in range(len(keypad)) and
                x + dirs[step][0] in range(len(keypad)) and
                keypad[y + dirs[step][1]][x + dirs[step][0]]
            ):
                    y, x = y + dirs[step][1], x + dirs[step][0]
        code.append(keypad[y][x])
    return "Bathroom Code: {}".format("".join(map(str, code)))


if __name__ == "__main__":
    print(bathroom_code(instructions))
