from problem_10 import get_all_primes_under
import itertools

def prime_permutations():
    '''
    finds all primes (necessarily 4 digit primes) that are in an arithmetic sequence and in which each is a permutation of the other
    problem 49
    '''
    all_primes = get_all_primes_under(10000)
    four_digit_primes = all_primes[all_primes.index(min(all_primes, key=lambda x:abs(x-1000))):]
    groups = []
    possibilities = dict(zip(four_digit_primes,[False] * len(four_digit_primes)))
    for p,v in possibilities.items():
        if v == True:
            continue
        perms = {int(''.join(i)) for i in itertools.permutations(str(p))}
        overlap = []
        for k in perms:
            if k in possibilities.keys():
                possibilities[k] = True
                overlap.append(k)
        if len(overlap) >= 3:
            groups.append(tuple(sorted(overlap)))

    prime_permutations = set()
    for g in groups:
        for j in itertools.permutations(g,3):
            j = sorted(j)
            if is_arithmetic_sequence(j[0],j[1],j[2]):
                prime_permutations.add(tuple(j))
    return prime_permutations

def is_arithmetic_sequence(a,b,c):
    return True if (a + c)/2 == b else False

    # possibilities = [int(''.join(a)) for a,b in collections.Counter([tuple(sorted(str(p))) for p in four_digit_primes]).items() if b > 2]
    # permuted =  [p for p in four_digit_primes if p in possibilities] #this is a list of four digit prime numbers having at least two permutations of themselves also present in the list
