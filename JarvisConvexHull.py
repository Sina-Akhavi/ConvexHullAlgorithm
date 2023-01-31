import math
def find_convex_hull(points):
    convex_hull = []
    first_point = min(points)

    convex_hull.append(first_point)
    last_point_in_hull = first_point
    while True:
        next_point = points[0]
        for point in points:
            status_of_three_points = check_three_points(last_point_in_hull, next_point, point)
            if time_to_update_next_point(status_of_three_points, last_point_in_hull, next_point, point):
                next_point = point
        last_point_in_hull = next_point

        if last_point_in_hull == first_point:
            break
        convex_hull.append(last_point_in_hull)
        
    return convex_hull
        
def check_three_points(p1, p2, p3):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3

    result = (y3 - y2) * (x2 - x1) - (y2 - y1) * (x3 - x2)

    if result < 0:
        return -1
    elif 0 < result:
        return 1
    return 0

def time_to_update_next_point(status_of_three_points, last_point_in_hull, next_point, point):
    condition = (status_of_three_points == 1) or (next_point == last_point_in_hull) 
    condition = condition or (status_of_three_points == 0 and cal_distance(last_point_in_hull, next_point) < cal_distance(last_point_in_hull, point))
    return condition
               
def cal_distance(p1, p2):
    x1 = p1[0]
    y1 = p1[1]

    x2 = p2[0]
    y2 = p2[1]

    return math.sqrt((y1 - y2) ** 2 + (x1 - x2) ** 2)

point = (1, 4)
x, y = point
points = [(1, 2), (0, 1), (-1, 3), (-2, 0), (-3, 1), (-3, 3), (-5, 1), (-5, 3), (-3, 6), (-3, -3), (9, -2), (-3, 6), (-20, -15)]
print(find_convex_hull(points)) # works properly

# print(x, y)

