

def digit_power_sequence():
    def get_digits(n):
        while n > 0:
            n, r = divmod(n, 10)
            yield r

    make_digit_sum = lambda n: sum(get_digits(n))

    cache = {}

    def raise_to_power(n, e):
        try:
            return cache[n][e - 1]
        except KeyError:
            cache[n] = [n]
            return raise_to_power(n, e)
        except IndexError:
            powers = cache[n]
            powers.append(powers[-1] * n)
            try:
                return powers[e - 1]
            except IndexError:
                return raise_to_power(n, e)

    def has_digit_power_sum(n, sum_digits, exp_guess):
        if sum_digits == 1:
            return False, exp_guess

        value = raise_to_power(sum_digits, exp_guess)
        if value == n:
            return True, exp_guess
        new_guess = exp_guess + (1 if value < n else -1)
        return (n == raise_to_power(sum_digits, new_guess)), new_guess

    n = 10
    last_guess = 1
    while True:
        dig_sum = make_digit_sum(n)
        success, last_guess = has_digit_power_sum(n, dig_sum,
                                                  last_guess)
        print "Closest guess for {} was {} ** {} == {}".format(n, dig_sum, last_guess, dig_sum ** last_guess)
        if success:
            yield n
        n += 1

if __name__ == '__main__':
    from sys import argv
    from itertools import islice

    try:
        if argv[1]:
            limit = int(argv[1])
    except IndexError:
        limit = 3

    for i, v in islice(enumerate(digit_power_sequence()), 0, limit):
        print "{}. {}".format(i + 1, v)
