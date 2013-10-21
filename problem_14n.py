import pudb

def memoize(func):
    memo = {}
    def inner_func(*args):
        try:
            return memo[args]
        except:
            memo[args] = func(args)
            return memo[args]
    return inner_func

def get_next_Collatz(n):
    assert type(n) == int
    return n/2 if n % 2 == 0 else (n*3) + 1 

@memoize
def get_Collatz_sequence_length(n):
    if n == 1: 
        return 1 
    else:
        return get_Collatz_sequence_length(get_next_Collatz(n))+1

if __name__ == '__main__':
    pudb.set_trace()
    print get_Collatz_sequence_length(13)
   #results = {x:get_Collatz_sequence_length(x) for x in range(1,10**6)}
   #print max(results.items(),key=lambda x: x[1])
        
