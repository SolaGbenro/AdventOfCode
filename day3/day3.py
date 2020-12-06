def event_one_traversal(path_to_traverse):
    # advance one row down
    path_to_traverse = path_to_traverse[1:]
    step_size = 3
    # index will start at first step_size
    index = step_size
    tree_count = 0
    map_size = len(path_to_traverse[0])
    for row in path_to_traverse:
        # map continuously repeats, use mod to mimic behavior
        if row[index % map_size] == "#":
            tree_count += 1
        index += step_size

    return tree_count


def right_one_down_one(path_to_traverse):
    # advance one row down
    path_to_traverse = path_to_traverse[1:]
    step_size = 1
    # index will start at first step_size
    index = step_size
    tree_count = 0
    map_size = len(path_to_traverse[0])
    for row in path_to_traverse:
        # map continuously repeats, use mod to mimic behavior
        if row[index % map_size] == "#":
            tree_count += 1
        index += step_size

    return tree_count


def right_five_down_one(path_to_traverse):
    # advance one row down
    path_to_traverse = path_to_traverse[1:]
    step_size = 5
    # index will start at first step_size
    index = step_size
    tree_count = 0
    map_size = len(path_to_traverse[0])
    for row in path_to_traverse:
        # map continuously repeats, use mod to mimic behavior
        if row[index % map_size] == "#":
            tree_count += 1
        index += step_size

    return tree_count


def right_seven_down_one(path_to_traverse):
    # advance one row down
    path_to_traverse = path_to_traverse[1:]
    step_size = 7
    # index will start at first step_size
    index = step_size
    tree_count = 0
    map_size = len(path_to_traverse[0])
    for row in path_to_traverse:
        # map continuously repeats, use mod to mimic behavior
        if row[index % map_size] == "#":
            tree_count += 1
        index += step_size

    return tree_count


def right_one_down_two(path_to_traverse):
    # condense map to only contain rows needed
    path_to_traverse = path_to_traverse[2::2]
    step_size = 1
    # index will start at first step_size
    index = step_size
    tree_count = 0
    map_size = len(path_to_traverse[0])
    for row in path_to_traverse:
        # map continuously repeats, use mod to mimic behavior
        if row[index % map_size] == "#":
            tree_count += 1
        index += step_size

    return tree_count


def event_two_traversal(path_to_traverse):
    return((event_one_traversal(path_to_traverse)) * (right_one_down_one(path_to_traverse)) *
            (right_five_down_one(path_to_traverse)) * (right_seven_down_one(path_to_traverse)) *
           (right_one_down_two(path_to_traverse)))


if __name__ == '__main__':
    path = [e for e in open('day3_input.txt', 'r').read().strip().split('\n')]
    print(event_one_traversal(path))
    print(event_two_traversal(path))
