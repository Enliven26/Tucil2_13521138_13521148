import math
import numpy
import Points as p

    
def findNearestPairBF(points):
    # mengembalikan tuple berupa (minDistance, Pair) untuk pasangan titik terdekat dengan pendekatan brute force

    pair = []
    minDistance = float("inf")

    for i in range(len(points) - 1):
        for j in range(i + 1, len(points)):

            temp = p.getDistance(points[i], points[j])

            if (temp < minDistance):
                minDistance = temp
                pair = [points[i], points[j]]

    return (minDistance, pair)

def findNearestMid(points, mid, minDistance):
    # mengembalikan tuple berupa (minDistance, Pair) untuk pasangan titik terdekat yang berada di range tengah

    midPoint = points[mid]
    midPoints = []

    result = (float("inf"), [])

    for point in points:
        if (abs(point[0] - midPoint[0]) < minDistance):
            midPoints.append(point)

    p.mergeSort(midPoints, 1)

    size = len(midPoints)
    for i in range(size - 1):
        for j in range(i + 1, size):
            if (abs(midPoints[i][0] - midPoints[j][0]) >= minDistance):
                continue

            if (not(p.isInRange(midPoints[i], midPoints[j]))):
                break
            
            tempDistance = p.getDistance(midPoints[i], midPoints[j])

            if (tempDistance < minDistance):
                result[0] = tempDistance
                result[1] = [midPoints[i], midPoints[j]]
    
    return result

def findNearestPair(points):
    # mengembalikan tuple berupa (minDistance, Pair) untuk pasangan titik terdekat dengan pendekatan divide and conquer

    if (len(points) <= 3):
        return findNearestPairBF(points)
    
    mid = len(points) // 2

    result1 = findNearestPair(points[0:mid])
    result2 = findNearestPair(points[mid:])

    finalResult = (0, [])

    if (result1[0] <= result2[0]):
        finalResult = result1

    else:
        finalResult = result2

    result3 = findNearestMid(points, mid, finalResult[0])

    if (result3[0] < finalResult[0]):
        finalResult = result3

    return finalResult
    

