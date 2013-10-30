
def spec_cross_product(a,b):
    return (-a[0])*(b[1]-a[1])-(-a[1])*(b[0]-a[0]) > 0

def origin_within_triangle(v0,v1,v2):
    return spec_cross_product(v0,v1) == spec_cross_product(v1,v2) == spec_cross_product(v2,v0)
