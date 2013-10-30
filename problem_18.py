
def maximum_path(triangle):
    '''
    find the maximum path through an integer triangle such as in
    problem 18, problem 67

    input triangle is a 2-D list where internal list represents a
    rung and each list item integer within an upfacing triangle

    proceeds from bottom row, adding value of larger of two adjacent
    items on bottom to item on top; once it reaches the apex,
    the sum there is the sum of the greatest possible path.
    '''

    delta = reversed(triangle)

    for i,row in enumerate(delta):
        if i == 0:
            continue
        for j,val in enumerate(row):
            oldI = i - 1
            delta[i][j] = val + max(delta[oldI][j:j+2])

    return delta[i][j]
