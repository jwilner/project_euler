
'''
biggest possible n under maximum m
n + n - 1 + n - 1 = m
3n - 2 = m
n = (m + 2) // 3

possible perimeters = n + 2n + 2, n + 2n - 2
area = (a**2 / 2) * sqrt((b ** 2 / a ** 2) - 1 / 4)

(n - 1) ** 2

if n + 1:
area = n / 4 * sqrt((n + 2) * (3n + 2))
if n - 1:
area = n / 4 * sqrt((n - 2) * (3n - 2))
'''


def equilateral_triangles(max_perimeter=10**9):
    max_side = (max_perimeter + 2) // 3

    area_funcs = [lambda n: ((n/4) * ((n+2) * (3*n+2)) ** .5),
                  lambda n: ((n/4) * ((n-2) * (3*n-2)) ** .5)]

    for n in xrange(2, max_side):
        print n, [f(n) for f in area_funcs]


if __name__ == '__main__':
    from sys import argv
    print equilateral_triangles(int(argv[1]))
