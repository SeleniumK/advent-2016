class Screen(object):
    """Screen would display input -- if it weren't smashed.

    Screen is 50px by 6px.
    """

    def __init__(self, width=50, height=6):
        """Initialize a screen. Contains rid 50x6, all pixels turned off."""
        self.grid = [[0 for _ in range(width)] for _ in range(height)]

    def rect(self, a, b):
        """
        Turn on all of the pixels.

        Turns on in a rectangle at the top-left
        of the screen which is A wide and B tall.
        """
        for row in self.grid[:b]:
            for i in range(a):
                row[i] = 1

    def rotate_row(self, a, b):
        """Rotate a row.

        Shifts all of the pixels in row A (0 index) right by B pixels.
        Pixels that would fall off the right end appear at the
        left end of the row.
        """
        self.grid[a] = self.grid[a][-b:] + self.grid[a][:-b]

    def rotate_column(self, a, b):
        """Rotate a column.

        Shifts all of the pixels in column A (0 index) down by B pixels.
        Pixels that would fall off the end appear at the start of the column.
        """
        rotated = [list(x) for x in zip(*self.grid)]
        rotated[a] = rotated[a][-b:] + rotated[a][:-b]
        self.grid = [list(x) for x in zip(*rotated)]

    def count_lit_pixels(self):
        """Collect number of lit pixels."""
        return sum(sum(row) for row in self.grid)

    def letters(self):
        """Print letters represented by the grid, one at a time."""
        l = [["x" if row[i] else " " for i in range(len(row))] for row in self.grid]
        reversed_letters = [list(x) for x in zip(*l)]
        for i in range(0, 50, 5):
            letter = [list(x) for x in zip(*reversed_letters[i:i + 5])]
            for line in letter:
                print("".join(line))
            print("")


def perform_command(c, screen):
    """"""
    options = {
        "row": screen.rotate_row,
        "column": screen.rotate_column
    }
    if c[0] == "rect":
        a, b = map(int, c[1].split("x"))
        screen.rect(a, b)
    else:
        a = int(c[2].split("=")[-1])
        b = int(c[4])
        options[c[1]](a, b)

    return True


if __name__ == "__main__":
    filename = "input/day-8-input.txt"
    with open(filename, "r") as f:
        commands = [x.split() for x in f.read().splitlines()]

    screen = Screen()
    for c in commands:
        perform_command(c, screen)
    print(screen.count_lit_pixels())
    screen.letters()
