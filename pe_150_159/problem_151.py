
papers = 5
all_envelopes = [[1]]
tree = {0:{}}

def build_tree(env_index,node):
    envelope = all_envelopes[env_index]
    for sheet in envelope:
        outcome = sorted(envelope+list(range(sheet+1,papers+1)))
        outcome.remove(sheet)
        try:
            env_type = all_envelopes.index(outcome)
        except ValueError:
            all_envelopes.append(outcome)
            env_type = len(all_envelopes)-1
        if outcome == [papers]:
            node[env_type] = 'LEAF'
        else:
            node[env_type] = {}
            build_tree(env_type,node[env_type])
    return node

if __name__ == '__main__':
    build_tree(0,tree[0])
    for i,val in enumerate(all_envelopes):
        print i, val
