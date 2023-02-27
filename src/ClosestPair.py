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

    # kasus 1 dimensi

    if (len(points[0]) == 1):
        leftValue = (minDistance, [])
        rightValue = (minDistance, [])

        if (mid > 0):
            leftValue = (abs(points[mid][0] - points[mid-1][0]), points[mid-1])
        
        if (mid < len(points) - 1):
            rightValue = (abs(points[mid+1][0] - points[mid-1][0]), points[mid+1])

        if (leftValue[0] < minDistance):
            return leftValue
        
        return rightValue


    midPoint = points[mid]
    midPoints = []

    result = (minDistance, [])

    for point in points:
        if (abs(point[0] - midPoint[0]) < minDistance):
            midPoints.append(point)


    p.sort(midPoints, 1)

    size = len(midPoints)
    for i in range(size - 1):
        for j in range(i + 1, size):

            if (abs(midPoints[i][1] - midPoints[j][1]) >= result[0]):
                break

            if (not(p.isInRange(midPoints[i], midPoints[j], result[0]))): 
                continue
            
            tempDistance = p.getDistance(midPoints[i], midPoints[j])

            if (tempDistance < result[0]):
                result = (tempDistance, [midPoints[i], midPoints[j]])
    
    return result

def findNearestPairDNC(points):
    # mengembalikan tuple berupa (minDistance, Pair) untuk pasangan titik terdekat dengan pendekatan divide and conquer
    if (len(points) <= 3):

        return findNearestPairBF(points)
    
    mid = len(points) // 2

    result1 = findNearestPairDNC(points[0:mid])

    result2 = findNearestPairDNC(points[mid:])

    finalResult = (float("inf"), [])

    if (result1[0] <= result2[0]):
        finalResult = result1

    else:
        finalResult = result2

    result3 = findNearestMid(points, mid, finalResult[0])

    if (result3[0] < finalResult[0]):
        finalResult = result3

    return finalResult

def findNearestPair(points, method = 0):
    # return nearest pair with Divide and Conquer if method == 0 and Brute Force if method == 1
    p.counter.reset()

    if (method == 0):
        return findNearestPairDNC(points)
    
    return findNearestPairBF(points)

