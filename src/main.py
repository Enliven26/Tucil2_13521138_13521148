import Points as p
import IO
import ClosestPair as cp
import time

def main():

       stop = False

       IO.art()
       IO.welcome()
       while(not(stop)):
              
              choice = IO.getChoices(['Start', 'Exit'], "Action")

              if (choice == 1):

                     n = int(input("Points amount: "), end='')
                     dimension = int(input("Input dimension: "), end='')

                     choice = IO.getChoices(['Console', 'File', 'Random'])

                     # if (choice == 1):

                     # elif (choice == 2):

                     if (choice == 3):      
                            p1 = p.generateRandomPoints(n, dimension, -1e6, 1e6)

                     p.sort(p1)

                     start = time.time()
                     BFresult = cp.findNearestPair(p1, 1)
                     end = time.time()
                     print('Brute Force getDistance() calls count :', p.counter.count)
                     print('Brute Force execution time:', (end - start) * (10 ** 3), 'ms')

                     print('\n')

                     start = time.time()
                     DNCresult = cp.findNearestPair(p1)
                     end = time.time()

                     print('Divide and Conquer getDistance() calls count :', p.counter.count)
                     print('Divide and Conquer execution time:', (end - start) * (10 ** 3), 'ms')
                     print('\n')

       
       exit()
