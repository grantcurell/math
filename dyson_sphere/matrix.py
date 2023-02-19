from scipy.optimize import linprog
import numpy as np

# Order = iron, iron factories, copper, copper factories

c = [0, 0, 0, 0, 0, 0, -1, 0, -1, 0]
A_ub = [[0, 0, 0, 0, 1, -60, 0, 0, 0, 0],
     [1, -60, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 1, -40, 0, 0, 0, 0, 0, 0],
     [-1, 0, 0, 0, -2, 0, 1, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 1, -45, 0, 0],
     [-1, 0, -2, 0, 0, 0, 0, 0, 1, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 1, -45]]
b_ub = [0, 0, 180, 150, 0, 0, 0, 0, 0]
A_eq = [[1, 0, -2, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, -2, 0, 0, 0, 0, 0]]
b_eq = [0, 0]

res = linprog(c, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq, method='highs')

np.set_printoptions(suppress=True)

print(res)
