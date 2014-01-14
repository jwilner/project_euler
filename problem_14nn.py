

def collatz(target):
    lengths = {1: 1}

    def get_next_collatz(n):
        return n // 2 if n % 2 == 0 else (n * 3) + 1

    def get_collatz_seq_length(n):
        try:
            return lengths[n]
        except KeyError:
            lengths[n] = get_collatz_seq_length(get_next_collatz(n)) + 1
            return lengths[n]

    for x in range(2, target):
        get_collatz_seq_length(x)

    return max(lengths.items(), key=lambda x: x[1])

if __name__ == '__main__':
    print collatz(10**6)
