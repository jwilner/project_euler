

def maximum_path(triangle):
    """
    find the maximum path through an integer triangle such as in
    problem 18, problem 67

    input triangle is a 2-D list where internal list represents a
    rung and each list item integer within an upfacing triangle

    proceeds from bottom row, adding value of larger of two adjacent
    items on bottom to item on top; once it reaches the apex,
    the sum there is the sum of the greatest possible path.
    """

    delta = triangle[::-1]

    for i, row in enumerate(delta[1:], 1):
        old_i = i - 1
        for j, val in enumerate(row):
            delta[i][j] = val + max(delta[old_i][j:j+2])

    return delta[-1][-1]
