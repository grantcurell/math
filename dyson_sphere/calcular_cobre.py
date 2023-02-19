from scipy.optimize import linprog

c = [-60]
A = [[60]]
b = [150]
copper_plate_bounds = (0, None)

res = linprog(c, A_ub=A, b_ub=b, bounds=[copper_plate_bounds], method='highs')

print(res)
