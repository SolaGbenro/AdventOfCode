def event_one_traversal(path_to_traverse):
    # advance one row down and take first step
    path_to_traverse = path_to_traverse[1:]
    step_size = 3
    tree_count = 0
    map_size = len(path_to_traverse[0])
    for row in path_to_traverse:
        # map continuously repeats, use mod to mimic behavior
        if row[step_size % map_size] == "#":
            tree_count += 1
        step_size += 3

    return tree_count


if __name__ == '__main__':
    path = [e for e in open('day3_input.txt', 'r').read().strip().split('\n')]
    print(event_one_traversal(path))
