import problem_36 

def find_steps_to_palindrome(maximum,limit = 50):
        '''
        Find the number of iterations it takes to make a number into a palindrome through 
        reverse-and-add process for numbers <= maximum; numbers that don't become a 
        palindrome within 'limit' iterations (lychrel numbers) are designated with -1
        problem 55
        '''
        sieve = {a:0 for a in range(maximum+1)}
        for i,v in sieve.items():
                if v > 0: #then number of steps to palindrome has been found
                        continue
                steps = [i]
                n = i #need to access i later, so preserve
                while len(steps) < limit:
                        n += int(''.join(s for s in reversed(str(n))))
                        if problem_36.is_palindrome(str(n)): #check if palindrome before adding; otherwise palindrome would be included in steps
                                steps.reverse() #reverse list so that indices express no. of 0-based steps from palindrome 
                                sieve.update({val:ind+1 for ind,val in enumerate(steps) if val <= maximum}) 
                                break
                        steps.append(n)
                else: #if length of steps surpasses limit, this fires
                        sieve[i] = -1 ##connotes lychrel
        return sieve

