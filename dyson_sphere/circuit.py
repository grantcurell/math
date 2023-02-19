from scipy.optimize import linprog

c = [-2, 0, -1, 0]
A = [[1, -60, 0, 0], [0, 0, 1, -60], [0, 0, 1, 0], [1, 0, 0, 0]]
b = [0, 0, 150, 180]
copper_bounds = (0, None)
iron_bounds = (0, None)

res = linprog(c, A_ub=A, b_ub=b, method='highs')

print(res)
