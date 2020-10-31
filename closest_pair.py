# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 09:15:27 2020

@author: Vrajesh
"""
import random
import math
import time

pair=[(random.randrange(1,100),random.randrange(1,100)) for i in range(100)] # generating random pair of 100 values 


def distance(p1, p2):   # calculate the euclidean distance
    return math.sqrt(pow(p1[0] - p2[0], 2)
                     + pow(p1[1] - p2[1], 2))

def bruteForce(points_x):
    p1_x = p1_y = p2_x = p2_y = 0
    minDist = math.inf # constant returns a floating-point positive infinity

    # Take the min distance of possible pairs
    for i in range(len(points_x) - 1):
        if distance(points_x[i], points_x[i + 1]) < minDist:
            minDist = distance(points_x[i], points_x[i + 1])  # Update the min distance
            p1_x, p1_y, p2_x, p2_y = points_x[i][0], points_x[i][1], points_x[i + 1][0], points_x[i + 1][1]
    return int(minDist), ([p1_x, p1_y], [p2_x, p2_y])



def closest_pair_strip(P, Q, d):
    midPoint = P[len(P) // 2][0]
    p1_x = p1_y = p2_x = p2_y = 0

    # Get the points in range (-d, d) according tho the mid point
    rangeDist = [Q[i] for i in range(len(Q)) if midPoint - d <= Q[i][0] <= midPoint + d]
    minDist = math.inf

    for i in range(len(rangeDist)):
        # Check at most 15 next values
        for j in range(i + 1, min(i + 15, len(rangeDist))):
            dNew = distance(rangeDist[i], rangeDist[j])

            if dNew < minDist:
                p1_x, p1_y, p2_x, p2_y = rangeDist[i][0], rangeDist[i][1], rangeDist[j][0], rangeDist[j][1]
                minDist = dNew  # Update the min distance
    return minDist, ([p1_x, p1_y], [p2_x, p2_y])




def closest_pair(P):
    # Brut if tree points are left:
    lenP = len(P)
    if lenP <= 3:
        return bruteForce(P)

    Pn = sorted(P, key=lambda x: x[0]) # Sorting on basis of x coordinate
    Qn = sorted(P, key=lambda x: x[1]) # Sorting on basis of y coordinate

    midPoint = lenP // 2
    Qx = Pn[:midPoint]  # Get left part of array with x sorted
    Rx = Pn[midPoint:]  # Get right part of array with x sorted

    # Recursively call
    dLeft, ([p1Left_x, p1Left_y], [p2Left_x, p2Left_y]) = closest_pair(Qx)  # Left side min
    dRight, ([p1Right_x, p1Right_y], [p2Right_x, p2Right_y]) = closest_pair(Rx)  # Right side min

    # Take the min value and assign the points
    if dLeft > dRight:
        minDistAll = dRight
        p1Min_x, p1Min_y, p2Min_x, p2Min_y = \
            p1Right_x, p1Right_y, p2Right_x, p2Right_y
    else:
        minDistAll = dLeft
        p1Min_x, p1Min_y, p2Min_x, p2Min_y = \
            p1Left_x, p1Left_y, p2Left_x, p2Left_y

    # Check the middle for closest pair of points
    d, ([p1_x, p1_y], [p2_x, p2_y]) = closest_pair_strip(Pn, Qn, minDistAll)
    minDistPlane = min(d, minDistAll)

    # Return the min distance on a plane
    if minDistPlane == d:
        return minDistPlane, ([p1_x, p1_y], [p2_x, p2_y])
    else:
        return minDistPlane, ([p1Min_x, p1Min_y], [p2Min_x, p2Min_y])

start = time.time()
print(closest_pair(pair))
print(time.time() - start)