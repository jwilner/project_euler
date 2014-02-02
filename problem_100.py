from fractions import Fraction

discs = ['b'] * 15 + ['r'] * 6


def make_fraction(n=0, d=1):
    return n, d


def inc_numerator((n, d)):
    return make_fraction(n + 1, d)


def dec_numerator((n, d)):
    return make_fraction(n - 1, d)


def inc_denominator((n, d)):
    return make_fraction(n, d + 1)


def dec_denominator((n, d)):
    return make_fraction(n, d - 1)


def probability_blue(blue, red):
    return Fraction(blue, blue + red)

if __name__ == '__main__':
    print probability_blue(15, 6)
