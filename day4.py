with open("input/day-4-input.txt", "r") as f:
    rooms = f.read().splitlines()

with open("input/day-4-test-input.txt", "r") as f:
    test_input = f.read().splitlines()


def is_valid_room(room, ending):
    """Take a string representing a room, and a string representing expected most frequent letters.

    Return if most frequent letters in room are as expected (Validating a real room).
    """
    c = sorted([(x, room.count(x)) for x in set(room)], key=lambda x: x[0])
    c = sorted(c, key=lambda x: x[1], reverse=True)

    return "".join(x for x, _ in c[:len(ending)]) == ending


def total_code_all_valid_rooms(rooms):
    """Return sum of room codes for all valid rooms."""
    total = 0
    for room in rooms:
        room = room.split("-")
        code, ending = room.pop()[:-2].split("[")
        room = "".join(room)
        total += int(code) if is_valid_room(room, ending) else 0
    return total


def list_valid_rooms(rooms):
    """Create a list of room/room code for all valid rooms."""
    r = []
    for room in rooms:
        room = room.split("-")
        code, ending = room.pop()[:-2].split("[")
        x = "".join(room)
        if is_valid_room(x, ending):
            r.append(("-".join(room), code))
    return r


def caesar_cipher(word, n):
    """For word passed in, shift it n numbers forward in the alphabet."""
    return "".join([chr((ord(char) - 97 + n) % 26 + 97) if char != "-" else " " for char in word])


def decode_rooms(rooms):
    """Given a list of valid rooms, decode each room.

    If room name contains "north", return room name and code
    """
    for room in rooms:
        decoded = caesar_cipher(room[0], int(room[1]))
        if "north" in decoded:
            return (decoded, room[1])


if __name__ == "__main__":
    print(decode_rooms(list_valid_rooms(rooms)))
