import Points as p
import IO
import ClosestPair as cp

p1 = p.generateRandomPoints(10, 3, -1, 1)

p.sort(p1)

print(cp.findNearestPair(p1, 1))
print(p.counter.count)

print(cp.findNearestPair(p1))
print(p.counter.count)