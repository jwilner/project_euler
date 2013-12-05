
def euclid_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def triangles_at_p_or_q(x, y):
    gcd = euclid_gcd(x, y)
    new_x, new_y = x / gcd, y / gcd
    return min(int(y / new_x),
               int((50 - x) / new_y))

if __name__ == '__main__':
    num_at_origin = 2500
    trivial_cases_for_one_side = 2500
    triangles_with_angle_at_p = (sum(triangles_at_p_or_q(x, y)
                                     for x in range(1, 51)
                                     for y in range(1, 51))
                                 + trivial_cases_for_one_side)
    print num_at_origin + (2 * triangles_with_angle_at_p)  # by reflection
