from scipy.optimize import linprog

# Order = copper, copper factories, magnets, magnet factories

c = [-1, 0, -2, 0]
A = [[1, -60, 0, 0], [0, 0, 1, 0], [1, 0, 0, 0], [0, 0, 1, -40]]
b = [0, 180, 150, 0]
copper_bounds = (0, None)
iron_bounds = (0, None)

res = linprog(c, A_ub=A, b_ub=b, method='highs')

print(res)
