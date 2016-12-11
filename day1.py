steps = [
    "L2", "L3", "L3", "L4", "R1", "R2", "L3", "R3", "R3", "L1",
    "L3", 'R2', "R3", "L3", "R4", "R3", "R3", "L1", "L4", "R4", "L2",
    "R5", "R1", "L5", "R1", "R3", "L5", 'R2', "L2", "R2", "R1", "L1",
    "L3", "L3", "R4", "R5", "R4", "L1", "L189", "L2", "R2", "L5", "R5",
    "R45", 'L3', "R4", "R77", "L1", "R1", "R194", "R2", "L5", "L3",
    "L2", "L1", "R5", "L3", "L3", "L5", "L5", "L5", "R2", "L1", "L2",
    "L3", "R2", "R5", "R4", "L2", "R3", "R5", "L2", "L2", "R3", "L3",
    "L2", "L1", "L3", "R5", "R4", "R3", "R2", "L1", "R2", "L5", 'R4',
    'L5', 'L4', "R4", "L2", "R5", "L3", "L2", "R4", "L1", "L2", "R2",
    "R3", "L2", "L5", "R1", "R1", "R3", "R4", "R1", "R2", "R4", "R5",
    "L3", "L5", "L3", "L3", "R5", "R4", "R1", "L3", "R1", "L3", "R3",
    "R3", "R3", "L1", 'R3', "R4", "L5", "L3", "L1", "L5", "L4", "R4",
    "R1", "L4", "R3", 'R3', "R5", "R4", "R3", "R3", "L1", "L2", "R1",
    "L4", "L4", "L3", "L4", "L3", "L5", "R2", "R4", "L2"
]


def taxi(steps):
    """Return the length of the shortest path to the point calculated by steps provided.

    Must move along city streets -- Taxicab Geometry
    """
    directions = {0: [0, 1], 1: [1, 0], 2: [0, -1], 3: [-1, 0]}
    facing = 0
    position = [0, 0]
    visited = [position[:]]

    for step in steps:
        facing = (facing + 1) % 4 if step[0] == "R" else (facing - 1) % 4
        for _ in range(int(step[1:])):
            position[0] += directions[facing][0]
            position[1] += directions[facing][1]
            if position in visited:
                return "Shortest path to HQ: {}".format(sum(map(abs, position)))
            visited.append(position[:])
    return False

if __name__ == "__main__":
    print(taxi(steps))
