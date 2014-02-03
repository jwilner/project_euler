

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
def fit_blocks(row, blocks):
    '''Find every position for given block length and make recursive call on
    rest of array'''
    summation = 0
    for block in blocks:
        if row < block:
            break
        if row == block:
            summation += 1
            break
        summation += sum(fit_blocks(row - x, blocks) + 1
                         for x in range(block, row + 1))
    return summation

if __name__ == '__main__':
    print fit_blocks(50, (2, 3, 4)) + 1
