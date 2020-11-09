'''
closestPointPair (Task 3 of 3)
(1:24:54)
Codewriting

You have an array p of points on a Cartesian plane. Find and return the minimum possible Euclidian distance between two points with different indices in p.

Example

For p = [[0, 11], [-7, 1], [-5, -3]], the output should be
closestPointPair(p) = 4.472135955.

Input/Output

[execution time limit] 4 seconds (php)

[input] array.array.integer p

Every inner array p[i] contains exactly 2 integers: the x and y coordinates of the ith point.

Guaranteed constraints:
2 ≤ p.length ≤ 2 · 104,
p[i].length = 2,
|p[i][j]| ≤ 107.

[output] float

The minimum possible distance between two points with different indices in p.

Your answer will be considered correct if its absolute error doesn't exceed 10-5.
'''
import math


def closest_point_pair(p):
    distances = list()
    len_points = len(p)

    for i1 in range(0, len_points - 1):
        p1 = p[i1]
        for i2 in range(i1 + 1, len_points):
            p2 = p[i2]
            distances.append(math.sqrt(
                ((p1[0] - p2[0]) ** 2) + ((p1[1] - p2[1]) ** 2)
            ))

    return min(distances)
