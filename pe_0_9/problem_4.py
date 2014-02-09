

def is_palindrome(n):
    strung = str(n)
    return strung == strung[::-1]


def find_largest_palindrome(digits=2):
    largest_eleven = (10 ** digits // 11) * 11
    largest_palindrome = 1
    for m in xrange(largest_eleven, 0, -11):
        for n in xrange((10 ** digits) - 1, 0, -1):
            num = m * n
            if is_palindrome(num) and num > largest_palindrome:
                largest_palindrome = num
                break
            if num < largest_palindrome:
                break
    return largest_palindrome




if __name__ == '__main__':
    print find_largest_palindrome(3)
