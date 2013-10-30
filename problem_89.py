class Roman:
    '''
    A class for dealing with Roman numerals
    Problem 89
    '''
    _numerals = [('M',1000),('CM',900),('D',500),('CD',400),('C',100),('XC',90),('L',50),('XL',40),('X',10),('IX',9),('V',5),('IV',4),('I',1)]
    _cache = {}

    def __init__(self):
        self._by_length = sorted(self._numerals,reverse = True,key=lambda x:len(x[0]))
        self._by_value = sorted(self._numerals,reverse = True,key=lambda x:x[1])

    def roman_to_arab(self,r_num):
        if type(r_num) != str:
            raise TypeError
        if r_num in self._cache:
            return self._cache[r_num]
        tally = 0
        original = r_num
        for (roman,arab) in self._by_length:
            if roman in r_num:
                times, r_num = r_num.count(roman), r_num.replace(roman,'')
                tally += arab*times
        self._cache[original] = tally
        return tally

    def arab_to_roman(self,a_num):
        if type(a_num) != int:
            raise TypeError
        if a_num in self._cache:
            return self._cache[a_num]
        original = a_num
        r_num = ''
        for (roman,arab) in self._by_value:
            if a_num >= arab:
                r_num += roman*(a_num//arab)
                a_num %= arab
        self._cache[original] = r_num
        return r_num
