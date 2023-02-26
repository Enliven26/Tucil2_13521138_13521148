import Points as p
import IO
import ClosestPair as cp

for i in range(1000):
       p1 = p.generateRandomPoints(500, 3, -1, 1)

       p.sort(p1)

       res1 = cp.findNearestPair(p1, 1)

       res2 = cp.findNearestPair(p1)
       
       if (res1[0] != res2[0]): 
              print(res1)
              print(res2)
              
              print("ERROR")
              print(p1)
              exit()
       else:
              print(i)
              
print("CONGRATS!")
