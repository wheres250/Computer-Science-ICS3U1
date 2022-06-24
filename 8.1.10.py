"""
Author: Kvin2K
Date: 05/11/2022
codehs
"""
import math
"""
Coordinate pairs
Args:
    x1
    x2
    y1
    y2

Returns:
    "Dead!!! LOL!!!!"
"""

def distance(point1, point2):
    x1 = point1 [0]
    x2 = point2 [0]
    y1 = point1 [1]
    y2 = point2 [1]
    square1 = pow (y2 - y1, 2)
    square2 = pow (x2 - x1, 2)
    return math.sqrt(square1+square2)
