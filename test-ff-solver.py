
from finitefield.finitefield import FiniteField
from linearsolver.linearsolver import someSolution

FF = FiniteField(13)
A = [
[FF(4), FF(2), FF(9), FF(1)],
[FF(4), FF(3), FF(6), FF(1)],
[FF(2), FF(11), FF(5), FF(1)],
]

B = someSolution(A)
