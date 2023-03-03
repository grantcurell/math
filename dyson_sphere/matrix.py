import pulp

# Define decision variables
copper_ingots_per_second = pulp.LpVariable('Copper Ingots Per Second', lowBound=0)
iron_ingots_per_second = pulp.LpVariable('Iron Ingots Per Second', lowBound=0)
iron_ore_per_second = pulp.LpVariable('Iron Ore Per Second', lowBound=0)
copper_ore_per_second = pulp.LpVariable('Copper Ore Per Second', lowBound=0)
y = pulp.LpVariable('y', lowBound=0)

# Define the optimization problem as a maximization problem
problem = pulp.LpProblem('Green Circuit Production', pulp.LpMaximize)

# Define objective function
problem += y

# Define constraints
problem += copper_ingots_per_second >= .75 * y
problem += iron_ingots_per_second >= 1.5 * y
problem += copper_ore_per_second >= copper_ingots_per_second
problem += iron_ore_per_second >= iron_ingots_per_second
problem += iron_ore_per_second <= 3.5
problem += copper_ore_per_second <= 3.5
problem += y <= .75

# Solve the problem
status = problem.solve()

# Check if a solution was found
if status == pulp.LpStatusOptimal:
    # Print the values of copper_ingots_per_second, iron_ingots_per_second, iron_ore_per_second, copper_ore_per_second, and y
    print("Copper Ingots Per Second = ", copper_ingots_per_second.value())
    print("Iron Ingots Per Second = ", iron_ingots_per_second.value())
    print("Iron Ore Per Second = ", iron_ore_per_second.value())
    print("Copper Ore Per Second = ", copper_ore_per_second.value())
    print("y = ", y.value())
else:
    print("No solution found.")
