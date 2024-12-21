import math

def euclidean_distance(p1, p2):
    x1, y1, x2, y2 = *p1, *p2

    return math.sqrt((y2 - y1) ** 2 + (x2 - x1) ** 2)

def polar_angle(p1, p2):
    if p1[1] == p2[1]:
        return -math.pi
    
    dy = p1[1] - p2[1]
    dx = p1[0] - p2[0]

    return math.atan2(dy, dx)

def orientation(p1, p2, p3):
    """
    Determines the orientation of the point in relation to the previous
    three points using 3x3 matrix determinant:

	[p1(x) p1(y) 1]
	[p2(x) p2(y) 1]
	[p3(x) p3(y) 1]

    Output:
    -------
    if >0 then counter-clockwise
    if <0 then clockwise
    if =0 then collinear
    """
    return (p2[0] - p1[0]) * (p3[1] - p1[1]) -(p2[1] - p1[1]) * (p3[0] - p1[0])

def graham_scan(points):
    """
    Graham Scan algorithm to find Convex Hull.
    
    Complexity: O(n*log(n)).
    """
    # Find the bottom most point
    p0 = min(points, key=lambda p: (p[1], p[0]))
    # Sort by angle and the distance to the most bottom point
    points.sort(key=lambda p: (polar_angle(p0, p), euclidean_distance(p0, p)))
 
    hull = []
    for idx in range(len(points)):
        while len(hull) >= 2 and orientation(hull[-2], hull[-1], points[idx]) < 1:
            hull.pop()
        hull.append(points[idx])

    return hull
