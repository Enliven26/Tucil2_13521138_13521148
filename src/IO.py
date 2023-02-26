import matplotlib.pyplot as plt

def realInput(n = 1):
    uIn = list(input().split())
    # validate input amount
    if(len(uIn) != n):
        print(f"Mohon input berupa {n} buah angka bulat!\n")
        return None
    else:
        # validate input(s) type
        for i in range(0, n):
            try:
                uIn[i] = int(uIn[i])
            except ValueError:
                print(f"Mohon input bertipe bilangan bulat! (masukan invalid pertama pada posisi {i+1})\n")
                return None
        # if all input(s) valid, return list of numbers
        return uIn
# end function


def realInput(n = 1):
    uIn = list(input().split())
    # validate input amount
    if(len(uIn) != n):
        print(f"Mohon input berupa {n} buah angka!\n")
        return None
    else:
        # validate input(s) type
        for i in range(0, n):
            try:
                uIn[i] = float(uIn[i])
            except ValueError:
                print(f"Mohon input bertipe bilangan! (masukan invalid pertama pada posisi {i+1})\n")
                return None
        # if all input(s) valid, return list of numbers
        return uIn
# end function
    
def plotPoints(Points, Point1, Point2):
    fig = plt.figure()
    ax = fig.add_subplot(projection = '3d')

    for point in Points:
        if(point == Point1):
            symbol = '^'
            color = '#ff0000'
        elif(point == Point2):
            symbol = '^'
            color = '#ffa500'
        else:
            symbol = 'o'
            color = '#7fdcfa'
        ax.scatter(point[0], point[1], point[2], marker=symbol, color=color)

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    plt.show()
# end function