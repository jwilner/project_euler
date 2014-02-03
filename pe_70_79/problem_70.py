from problem_10 import get_all_primes_under

def permuted_totients(limit=10**7):
    '''
    problem 70 -- find the permuted number-totient pair for which n/phi(n) is a minimum
    '''
    rooted = int((limit)**.5)
    primes = get_all_primes_under(rooted*3)
    mid_index = primes.index(min(primes,key=lambda x:abs(x-rooted)))
    step = mid_index//10
    best_n_phi, found, i, cache = limit, (0,0,0), 0, set()
    while found == (0,0,0) and i < mid_index:
        i += step
        for p in primes[mid_index:mid_index+i]:
            for q in primes[mid_index:mid_index-i:-1]:
                n = p*q
                if n > limit or n in cache: continue
                cache.add(n)
                phi = (p-1)*(q-1)
                n_over_phi = n/phi
                if n_over_phi > best_n_phi: break
                sn,sphi = str(n),str(phi)
                if sorted(sn) == sorted(sphi):
                    best_n_phi,found = n_over_phi,(n,p,q)
                    break #if we find one here, we won't find any better totient ratios below, so stop looking
    return found
