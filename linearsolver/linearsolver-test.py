
from linearsolver import *

def test1():
   A = [
   [1,-2,0,0,3,2],
   [0,0,1,0,-5,-3],
   [0,0,0,1,1,7],
   [0,0,0,0,0,0],
   ]

   print(someSolution(A))



A = [
[1, 0, 0, 0, 0, 2, 2],
[0, 1, 0, 0, 0, 0, 1],
[0, 0, 1, 0, 0, 4, 4],
[0, 0, 0, 1, 0, 3, 2],
[0, 0, 0, 0, 1, 3, 0],
]


print(someSolution(A))
