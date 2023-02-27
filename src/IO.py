import matplotlib.pyplot as plt

def art():
    print("\n")
    print(" _   _                                _    ______         _         _        ")  
    print("| \ | |                              | |   | ___ \       (_)       | |")
    print("|  \| |  ___   __ _  _ __   ___  ___ | |_  | |_/ /  ___   _  _ __  | |_  ___ ")
    print("| . ` | / _ \ / _` || '__| / _ \/ __|| __| |  __/  / _ \ | || '_ \ | __|/ __|")
    print("| |\  ||  __/| (_| || |   |  __/\__ \| |_  | |    | (_) || || | | || |_ \__ \\")
    print("\_| \_/ \___| \__,_||_|    \___||___/ \__| \_|     \___/ |_||_| |_| \__||___/")
    print("\n")

def welcome():
    print("\n")
    print("Welcome to nearest points calculator!\n")
    print("\n")

def showChoices(choices, label = ''):

    print("Select", label, ": ")

    for i in range(len(choices)):
        print('[' + str(i+1) + ']', choices[i])          

    print("\n")

def getChoices():
    return int(input('Your input : ', end = ''))

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
        if(point == Point1 or point == Point2):
            symbol = '^'
        else:
            symbol = 'o'
        ax.scatter(point[0], point[1], point[2], marker=symbol)

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    plt.show()
# end function