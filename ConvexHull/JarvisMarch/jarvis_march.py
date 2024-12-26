import math


def euclidean_distance(p1, p2):
    x1, y1, x2, y2 = *p1, *p2
    return math.sqrt((y2 - y1) ** 2 + (x2 - x1) ** 2)

def orientation(p1, p2, p3):
    """
    Determines the orientation of the point in relation to the previous
    three points using 3x3 matrix determinant:

	[p1(x) p1(y) 1]
	[p2(x) p2(y) 1]
	[p3(x) p3(y) 1]

    Output:
    -------
    if > 0 then counter-clockwise
    if < 0 then clockwise
    if = 0 then collinear
    """
    return (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0])

def jarvis_march(points):
    """
    Jarvis March algorithm to find Convex Hull.
    
    Complexity: O(n*h), where:
      n - number of points
      h - number of points on the Convex Hull.
    """
    # Find the left most point
    on_hull = min(points)
    hull = []

    while True:
        # Repeat until we reach the starting point
        hull.append(on_hull)
        next_point = points[0]
        for point in points:
            orient = orientation(on_hull, next_point, point)
            if (next_point == on_hull or orient > 0 or 
                (orient == 0 and euclidean_distance(on_hull, point) > euclidean_distance(on_hull, next_point))):
                next_point = point
        on_hull = next_point

        if on_hull == hull[0]:
            break

    return hull
