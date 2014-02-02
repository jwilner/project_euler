

def count_integer_solutions(target=1000000):

    def cuboids_with_side_m(m):
        """Generates all susbets with repetition; number always equivalent to
        (M^2 + M) / 2"""
        return ((x, y, m) for x in xrange(1, m + 1) for y in xrange(x, m + 1))

    def possible_legs((l, h, w)):
        return (l + h, w), (h + w, l), (w + l, h)

    def make_hypotenuse((a, b)):
        return (a ** 2 + b ** 2) ** .5

    def has_minimal_integer_solution(triple):
        return min(make_hypotenuse(legs)
                   for legs in possible_legs(triple)).is_integer()

    def num_solutions_for_m(m):
        return sum(1 for cuboid in cuboids_with_side_m(m)
                   if has_minimal_integer_solution(cuboid))

    num_solutions, M = 0, 0
    while num_solutions < target:
        M += 1
        m_solutions = num_solutions_for_m(M)
        num_solutions += m_solutions

    return M, num_solutions


if __name__ == '__main__':
    print count_integer_solutions()
