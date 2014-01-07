

def find_all_states(min_size=5):
    '''Takes a maximum paper size, runs the paper cutting process, and
    returns a list of all the possible states after following the cutting
    process through to its conclusion (i.e. the min_size)'''

    def cut_paper(n):
        ''' paper -> list of resulting papers '''
        return [p for p in range(n + 1, min_size + 1)]

    def get_all_resultant_envelopes(envelope):
        ''' envelope list -> list of envelope lists '''
        result_envelopes = []
        for index, paper in enumerate(envelope):
            result_envelopes.append(
                [p for i, p in enumerate(envelope) if i != index]
                + cut_paper(paper))

        return result_envelopes

    cache = {}

    def cached_envelopes(env):
        tup = tuple(env)
        try:
            return cache[tup]
        except KeyError:
            cache[tup] = get_all_resultant_envelopes(env)
        return cache[tup]

    class Node(object):

        def __init__(self, data):
            self.data = data
            self.branches = [Node(e)
                             for e in cached_envelopes(data)]

        def is_one_long(self):
            return len(self.data) == 1

        def is_not_one(self):
            return self.data == [1]

        def is_not_five(self):
            return self.data == [5]

    tree = Node([1])
    #print tree.data
    #for b in tree.branches:
        #print b.data

    print get_all_resultant_envelopes([2, 3])
    print cached_envelopes([1])

    def count_cases_and_children(node):
        if not node.data:
            return 0, 0

        child_info = [count_cases_and_children(n) for n in node.branches]
        numerator = sum(c[0] for c in child_info)
        denominator = sum(c[1] for c in child_info)

        if node.is_not_one() and node.is_not_five():
            if node.is_one_long():
                numerator += 1
            denominator += 1

        return numerator, denominator

    return count_cases_and_children(tree)


if __name__ == '__main__':
    import sys
    print find_all_states(min_size=int(sys.argv[1]))
