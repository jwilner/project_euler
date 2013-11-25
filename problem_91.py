import math, itertools

def f(a,b):
    if a == 1 and b == 1:
        return 3
    if a == b:
        return 5
    return 3

def distance_formula((x1,y1),(x2,y2)):
    x_diff, y_diff = x2-x1, y2-y1
    return math.sqrt(x_diff**2 + y_diff**2)

def within_point_zero_zero_zero_one(a,b):
    tolerance = 0.0001
    return min(a,b) + tolerance >= max(a,b)

def is_right_triangle(a,b,c):
    ab,bc,ac = [distance_formula(p,q)**2 for p,q in ((a,b),(b,c),(a,c))]
    return any(within_point_zero_zero_zero_one(p+q,r) for p,q,r in ((ab,bc,ac),
                                      (bc,ac,ab),
                                      (ac,ab,bc)))

def is_all_distinct(a_list):
    return len(set(a_list)) == len(a_list)


# all points have to be unique
# set of x has to be len > 1
# ditto for y

def is_triangle(points):
    return (len(set(points)) == 3 and
            len(set(x for x,y in points)) > 1 and
            len(set(y for x,y in points)) > 1)

def all_points_on_perimeter_of_rectangle(rect_x,rect_y):
    return list((x,rect_y) for x in range(rect_x))+list((rect_x,y) for y in range(rect_y))

def make_all_triples_with_origin(list_of_points):
    return set(tuple(sorted([(0,0),a,b])) for a,b in 
                        itertools.product((x for x in list_of_points if x != (0,0)),
                                          (x for x in list_of_points if x != (0,0))))

def find_all_triangles_in_rect((x,y)):
    points = all_points_on_perimeter_of_rectangle(x,y)
    triples = make_all_triples_with_origin(points)
    triangles = (t for t in triples if is_triangle(t)) 
    return triangles #[t for t in triangles if is_right_triangle(*t)]
