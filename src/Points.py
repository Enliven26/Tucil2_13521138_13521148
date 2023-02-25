import math

def getDistance(point1, point2):
    # mengembalikan jarak euclidean dua titik N dimensi
    result = 0

    for i in range(len(point1)):
        result += pow ((point1[i] - point2[i]), 2)

    return math.sqrt(result)

def isSmaller(point1, point2, startingIndex = 0):
    # membandingkan point1 dan point2, mengembalikan true jika ada indeks terkecil sehingga elemen pertama point1 lebih kecil dari elemen point2
    # dengan indeks terkecil >= startingIndex

    # asumsi startingIndex < len(point1)
    for i in range(startingIndex, len(point1)):

        if (point1[i] < point2[i]):
            return True
        
        if (point1[i] > point2[i]):
            return False
        
    return False

def isInRange(point1, point2, minDistance):
    # mengembalikan true jika selisih tiap elemen kedua titik kecil dari minDistance

    for i in range(len(point1)):
        if (abs(point1[i] - point2[i]) >= minDistance):
            return False
    
    return True

def merge(points, left, mid, right, startingElementIndex):
    # menggabungkan dua list titik N dimensi yang sudah terurut
    # startingElementIndex menjadi acuan perbandingan dua buah titik
    leftLimit = mid - left + 1
    rightLimit = right - mid

    leftPoints = [points[i] for i in range(leftLimit)]

    rightPoints = [points[i] for i in range(mid, right)]
    
    i = 0
    j = 0
    k = 0

    while (i < leftLimit and j < rightLimit):
        if (isSmaller(leftPoints[i], rightPoints[j], startingElementIndex)):
            points[k] = leftPoints[i]
            i += 1

        else:
            points[k] = rightPoints[j]
            j += 1
            
        k += 1

    while (i < leftLimit):
        points[k] = leftPoints[i]
        i += 1
        k += 1

    while (j < rightLimit):
        points[k] = rightPoints[j]
        j += 1
        k += 1
 
def mergeSort(points, left, right, startingElementIndex = 0):

    # mengurutkan list titik dengan algoritma merge sort

    if left < right:

        mid = (left + right) // 2
 
        mergeSort(points, left, mid)
        mergeSort(points, mid, right)
        merge(points, left, mid, right, startingElementIndex)