from collections import defaultdict

keylog = ['319', '680', '180', '690', '129', '620', '762', '689', '762', '318', '368', '710', '720', '710', '629', '168', '160', '689', '716', '731', '736', '729', '316', '729', '729', '710', '769', '290', '719', '680', '318', '389', '162', '289', '162', '718', '729', '319', '790', '680', '890', '362', '319', '760', '316', '729', '380', '319', '728', '716']

def keylog_analysis(keylog):
    '''
    find the shortest possible passcode
    problem 79
    '''
    rules = set()
    for code in keylog:
        rules.update([tuple(code[:2]),tuple(code[1:])])

    rules = list(rules)
    beginning = ''
    end = ''
    while rules:
        first = set()
        last = set()
        record = defaultdict(list)
        for rule in rules:
            first.add(rule[0])
            last.add(rule[1])
            record[rule[0]].append(rule)
            record[rule[1]].append(rule)
        first_term = first.difference(last)
        last_term = last.difference(first)
        if len(first_term) == 1:
            ft = first_term.pop()
            beginning += ft
            for f in record[ft]:
                if f in rules: rules.remove(f)
        if len(last_term) == 1:
            lt = last_term.pop()
            end = lt+end
            for l in record[lt]:
                if l in rules: rules.remove(l)
    return beginning+end
