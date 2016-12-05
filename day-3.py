input_file = "input/day-3-input.txt"
test_1 = [5, 3, 3]


def valid_triangle(a, b, c):
    return (a < b + c) and (b < a + c) and (c < a + b)


def sum_of_valid_triangles(lst):
    return sum(valid_triangle(*x) for x in lst)


if __name__ == "__main__":
    # read by row
    with open(input_file, "r") as f:
        triangles = [map(int, x.split()) for x in f.read().splitlines()]
    print(sum_of_valid_triangles(triangles))

    # read by column
    row = []
    for x in zip(*triangles):
        row.extend(list(x))
    row = [row[i:i + 3] for i in range(0, len(row), 3)]
    print(sum_of_valid_triangles(row))
