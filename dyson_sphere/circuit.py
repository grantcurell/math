from scipy.optimize import linprog

# Order = iron, iron factories, copper, copper factories

c = [-2, 0, -1, 0]
A = [[1, -60, 0, 0], [0, 0, 1, -60], [0, 0, 1, 0], [1, 0, 0, 0]]
b = [0, 0, 150, 180]

res = linprog(c, A_ub=A, b_ub=b, method='highs')

print(res)
