import itertools

def substring_divisibility():
    '''
    first define rules and then use them to limit eachother; ultimately means only two possiblities for last five characters
    d5d6d7d8d9d10 must be either 357289 or 952867, leaving only permutations of, respectively, 0146,0134 for the d1d2d3d4
    problem 43
    '''

    nums = []
    d = {'0146':'357289','0134':'952867'}
    for first_four,last_five in d.items():
        for i in itertools.permutations(first_four):
            s = ''.join(i)+last_five
            if int(s[1:4]) % 2 == 0 and int(s[2:5]) % 3 == 0:
                nums.append(int(s))
    return nums
