import matplotlib.pyplot as plt

def art():

    print(" _   _                                _    ______         _         _        ")  
    print("| \ | |                              | |   | ___ \       (_)       | |")
    print("|  \| |  ___   __ _  _ __   ___  ___ | |_  | |_/ /  ___   _  _ __  | |_  ___ ")
    print("| . ` | / _ \ / _` || '__| / _ \/ __|| __| |  __/  / _ \ | || '_ \ | __|/ __|")
    print("| |\  ||  __/| (_| || |   |  __/\__ \| |_  | |    | (_) || || | | || |_ \__ \\")
    print("\_| \_/ \___| \__,_||_|    \___||___/ \__| \_|     \___/ |_||_| |_| \__||___/")


def welcome():
    print("\n")
    print("Welcome to nearest points calculator!")

def inputFormatInfo(mode):
    print("\n-----------------------------------------------------------------------------------------------")
    print("Input format:")
    
    if (mode == 3):
        print("N  D                          {N is the number of points, and D is the dimension of the points}")
    
    else:
        print("N                             {N is the number of points}")
        print("D                             {D is the dimension of the points}")
    
    if (mode != 2):
        print("\nPoints input must follow the format:")
        print("X1_1 X1_2 X1_3 ... X1_D")
        print("X2_1 X2_2 X2_3 ... X2_D")
        print("...")
        print("XN_1 XN_2 XN_3 ... XN_D       {where Xi_j represents the value of i-th point in j-th dimension}")
    
    print("-----------------------------------------------------------------------------------------------\n")
# end function

def getChoices(choices, label = 'option', cancelOpt = False):
    print("\nSelect", label, ": ")

    optRange = len(choices)
    for i in range(optRange):
        print('[' + str(i+1) + ']', choices[i])

    # include additional option to return to previous menu
    if(cancelOpt):
        optRange += 1
        print(f'[{optRange}] Return')

    print()

    while(True):
        print('Your input : ', end='')
        userOpt = intInput(singleVal=True)

        if(userOpt != None):
            if(1 <= userOpt and userOpt <= optRange):
                break
            else:
                print(f'Input must be in range of [1-{optRange}]!\n')
                # optRange = 1 not handled, why even use when only 1 option is available?

    return userOpt
# end function


def initPointsInput():
    while(True):
        print("Input number of points: ", end='')
        n = intInput(minRange=2, singleVal=True)
        if(n != None):
            break

    while(True):
        print("Input dimensions: ", end='')
        dimension = intInput(minRange=1, singleVal=True)
        if(dimension != None):
            break
    
    return n, dimension
# end function

def fileToPoints():
    filename = fixFileFormat(input("Input file path (relative to test folder): "))

    try:
        f = open("./test/" + filename, "r")
    except FileNotFoundError:
        print("File not found.")
        return None

    tempIn = f.readline()
    pointsInfo = intInput(parseIn=tempIn, n=2)

    if(pointsInfo == None):
        print("File format does not follow input format.")
        return None
    else:
        # Validate number of points
        n = pointsInfo[0]
        if(n < 2):
            print("Number of points must be >= 2.")
            return None
        
        # Validate dimension value
        dim = pointsInfo[1]
        if(dim < 1):
            print("Points dimension cannot be lower than 1.")
            return None

    points = [None for _ in range(n)]

    for i in range(n):
        tempIn = f.readline()
        tempVal = realInput(parseIn=tempIn,n=dim)
        if(tempVal == None):
            print(f"invalid point value input at line {i+2}.")
            return None
        else:
            points[i] = tempVal

    f.close()
    return n, dim, points
# end function

def intInput(parseIn = None, n = 1, minRange = None, maxRange = None, singleVal = False):
    # check parse parameter
    if (isinstance(parseIn, str)):
        parseList = list(parseIn.split())

    elif (isinstance(parseIn, list)):
        parseList = parseIn

    elif (parseIn == None):
        parseList = input().split()

    else:
        return None

    # validate input amount
    if(len(parseList) != n):
        print(f"Input must consist(s) of {n} integers!")
        return None
    else:
        # validate input(s) type
        for i in range(0, n):
            try:
                parseList[i] = int(parseList[i])
            except ValueError:
                print(f"Input type must only be integers! (Caught invalid input at position {i+1})")
                return None
        
        # Validate value(s) range if specified
        if(minRange != None): # validate min value
            for num in parseList:
                if(num < minRange):
                    print(f"Input value(s) must be >= {minRange}!")
                    return None
        
        if(maxRange != None): # validate max value
            for num in parseList:
                if(num > maxRange):
                    print(f"Input value(s) must be <= {minRange}!")
                    return None
                
        # if all input(s) valid, return list of numbers
        if(singleVal):
            return parseList[0]
        else:
            return parseList
# end function


def realInput(parseIn = None, n = 1, minRange = None, maxRange = None, singleVal = False):
    # check parse parameter
    if (isinstance(parseIn, str)):
        parseList = list(parseIn.split())

    elif (isinstance(parseIn, list)):
        parseList = parseIn

    elif (parseIn == None):
        parseList = input().split()

    else:
        return None

    # validate input amount
    if(len(parseList) != n):
        print(f"Input must consist(s) of {n} real numbers!")
        return None
    else:
        # validate input(s) type
        for i in range(0, n):
            try:
                parseList[i] = float(parseList[i])
            except ValueError:
                print(f"Input type must only be real numbers! (Caught invalid input at position {i+1})")
                return None
        
        # Validate value(s) range if specified
        if(minRange != None): # validate min value
            for num in parseList:
                if(num < minRange):
                    print(f"Input value(s) must be >= {minRange}!")
                    return None
        
        if(maxRange != None): # validate max value
            for num in parseList:
                if(num > maxRange):
                    print(f"Input value(s) must be <= {minRange}!")
                    return None
                
        # if all input(s) valid, return list of numbers
        if(singleVal):
            return parseList[0]
        else:
            return parseList
# end function


def plot3DPoints(Points, Point1, Point2):
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
    print("\n[Waiting the plot to be closed]")
    plt.show()
# end function


def plot2DPoints(Points, Point1, Point2):
    # fig = plt.figure()
    # ax = fig.add_subplot(projection = '2d')

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
        plt.scatter(point[0], point[1], marker=symbol, color=color)

    plt.xlabel('X')
    plt.ylabel('Y')
    print("\n[Waiting the plot to be closed]\n")
    plt.show()
# end function

def fixFileFormat(fileName):
    
    return fileName.split('.', 1)[0] + ".txt"
