
def stupid_difference(start, end):
    num_terms = 1 + end - start
    sum_square = ((start + end) * num_terms / 2) ** 2
    square_sum = sum(i ** 2 for i in xrange(start, end + 1))
    return sum_square - square_sum

if __name__ == '__main__':
    print stupid_difference(1, 100)
