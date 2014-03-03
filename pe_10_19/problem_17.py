

one_to_nineteen = '''one two three four five six seven eight nine ten
    eleven twelve thirteen fourteen fifteen sixteen seventeen
    eighteen nineteen'''

twenty_to_ninety = "twenty thirty forty fifty sixty seventy eighty ninety"

word_lengths = {}
word_lengths.update({i: len(word)
                     for i, word in enumerate(one_to_nineteen.split(), 1)})

word_lengths.update({i * 10: len(word)
                     for i, word in enumerate(twenty_to_ninety.split(), 2)})


def get_word_length(n):
    if n in word_lengths:
        return word_lengths[n]

    if n == 1000:
        length = get_word_length(1) + len("thousand")

    elif n > 99:
        hundreds, remains = divmod(n, 100)
        second_part = len("and") + get_word_length(remains) if remains else 0
        length = get_word_length(hundreds) + len("hundred") + second_part

    else:  # 20 < n < 100
        tens_place, unit_place = divmod(n, 10)
        length = get_word_length(10 * tens_place) + get_word_length(unit_place)

    word_lengths[n] = length
    return word_lengths[n]

if __name__ == '__main__':
    print sum(get_word_length(n) for n in xrange(1, 1001))
