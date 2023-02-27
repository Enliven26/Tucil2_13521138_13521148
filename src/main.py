import Points as p
import IO
import ClosestPair as cp

for i in range(100):
       p1 = p.generateRandomPoints(100, 1, -1e6, 1e6)

       p.sort(p1)

       res1 = cp.findNearestPair(p1, 1)
       print(p.counter.count)

       res2 = cp.findNearestPair(p1)
       print(p.counter.count)
       
       if (res1[0] != res2[0]): 
              print("BF result: ", res1)
              print("DNC result: ", res2)
              
              print("ERROR")
              print(p1)
              exit()


print("CONGRATS!")
