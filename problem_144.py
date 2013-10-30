from utils import solve_quadratic

def points_of_reflection(a_x = 0,a_y = 10.1,b_x=1.4,b_y=-9.6):
    '''
    problem 144
    '''
    points = []
    while b_x < -0.01 or b_x > 0.01 or b_y < 0:
        ab_slope = (b_y - a_y)/(b_x - a_x) #slope of incoming line AB
        points.append((b_x,b_y)) #current reflection at bx,by
        tang_slope = -4*b_x/b_y #slope of tang at bx,by

        #find bc slope (angle of reflection)
        trig_ident = (ab_slope - tang_slope)/(1+ab_slope*tang_slope)
        bc_slope = (tang_slope - trig_ident) / (1+trig_ident*tang_slope) #trig identities (slope = tan) gives us outgoing bc_slope

        #use bc_slope to find new points cx,cy
        bc_intercept = b_y-(bc_slope*b_x) #use known points on BC (bx,by) and slope BC to solve b = y-mx
        new_xs = solve_quadratic(4+bc_slope*bc_slope,2*bc_intercept*bc_slope,bc_intercept*bc_intercept-100) #find intersection by plugging values into equation for ellipse
        c_x = new_xs[0] if abs(b_x-new_xs[0]) > abs(b_x-new_xs[1]) else new_xs[1] #pick value which is not current one

        #move everything along (b_y = mx+b or b_slope*c_x+intercept)
        a_x,a_y,b_x,b_y = b_x,b_y,c_x,bc_slope*c_x + bc_intercept
    return points
