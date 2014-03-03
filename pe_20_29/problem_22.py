import sys


def word_value(name):
    return sum(ord(c) - 64 for c in name)


def score_words(words):
    for i, word in enumerate(sorted(words), 1):
        yield i * word_value(word)


if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        words = f.read().replace('"', '').split(',')

    print sum(score_words(words))
