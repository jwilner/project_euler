

def get_hypotenuse(a, b):
    return (a**2 + b**2)**.5


def generate_sides(maximum=100):
    for a in range(1, maximum+1):
        for b in range(a, maximum+1):
            for c in range(b, maximum+1):
                yield a, b, c


def find_shortest_paths(maximum=100):
    return {tuple(sorted(sides)): get_hypotenuse(sides[0], sum(sides[1:]))
            for sides in generate_sides(maximum)}


def get_side_triples(maximum):
    for b in range(1, maximum + 1):
        for c in range(1, maximum + 1):
            yield maximum, b, c
    for a in range(1, maximum):
        yield a, maximum, maximum


def get_shortest_paths(desired_num=1974):
    num_solutions = 0
    max_side_length = 0
    while num_solutions < desired_num:
        max_side_length += 1
        solutions = {tuple(sorted(sides)): get_hypotenuse(sides[0],
                                                          sum(sides[1:]))
                     for sides in get_side_triples(max_side_length)}
        num_solutions += sum(1 for sol in solutions.values()
                             if int(sol) == sol)
    return max_side_length, num_solutions


if __name__ == '__main__':
    print sum(1 for t in find_shortest_paths().values() if t == int(t))
