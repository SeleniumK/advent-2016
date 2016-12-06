from collections import Counter


def set_up_input(filename):
    """Read in text file and return a list, split by lines."""
    with open(filename, "r") as f:
        input_list = f.read().splitlines()
    return input_list


def find_most_frequent_char_for_position(inputs):
    """Return a string representing the most common character in each element of the input."""
    return "".join([Counter(x).most_common(1)[0][0] for x in inputs])


def find_least_frequent_char_for_position(inputs):
    """Return a string representing the least common character in each element of the input."""
    return "".join([Counter(x).most_common()[-1][0] for x in inputs])


if __name__ == "__main__":
    filename = "input/day-6-input.txt"
    x = ["".join(x) for x in zip(*set_up_input(filename))]

    # Part 1
    print(find_most_frequent_char_for_position(x))

    # Part 2
    print(find_least_frequent_char_for_position(x))
