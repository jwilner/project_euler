
def cyclicate_figural_numbers():
    '''
    problem 61
    '''
    funcs = {lambda n:int(n*(n+1)/2),
                            lambda n:n*n,
                            lambda n:int(n*(3*n-1)/2),
                            lambda n:n*(2*n-1),
                            lambda n:int(n*(5*n-3)/2),
                            lambda n:n*(3*n-2)}
    terms = []

    for tag,f in enumerate(funcs):
        gen = (f(i) for i in range(1,1000))
        x = next(gen)
        while x < 1000: x = next(gen)
        else:
            while x < 10000:
                terms.append((str(x),tag))
                x = next(gen)

    sequences = [[x,[tag]] for x,tag in terms]

    for term,tag in terms:
        start,end = term[:2],term[2:]
        newly_found = []
        for string,tags in sequences:
            if tag not in tags:
                if string[-2:] == start:
                    if end == string[:2] and len(tags+[tag]) == 6:
                        final = string+term
                        return [int(final[i:i+4]) for i in range(0,len(final),4)]
                    newly_found.append((string+term,tags+[tag]))
                elif string[:2] == end:
                    newly_found.append((term+string,tags+[tag]))
        sequences.extend(newly_found)
