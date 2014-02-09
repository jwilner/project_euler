

def find_pythagorean_triplet(abc=100):
    for c in xrange(abc - 2, 2, - 1):
        for b in xrange(abc - c - 1, 1, - 1):
            a = abc - c - b
            if a ** 2 + b ** 2 == c ** 2:
                return a * b * c


if __name__ == '__main__':
    print find_pythagorean_triplet(1000)
