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