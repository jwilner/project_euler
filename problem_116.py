

def cache(f):
    cacher = {}

    def inner_func(*args):
        try:
            return cacher[args]
        except KeyError:
            cacher[args] = f(*args)
            return cacher[args]
    return inner_func


def fit_one_block(arr, block):
    return len(range(0, len(arr), block))


@cache
def fit_blocks(row, block):
    '''Find every position for given block length and make recursive call on
    rest of array'''
    if row < block:
        return 0
    if row == block:
        return 1
    summation = sum(fit_blocks(row - x, block) + 1
                    for x in range(block, row + 1))
    return summation

if __name__ == '__main__':
    print sum(fit_blocks(50, i) for i in range(2, 5))
