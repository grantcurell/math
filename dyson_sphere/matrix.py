import pulp

# This code will find the minimum values required to build electromagnetic matrices
# at 20/s.

# Define decision variables
copper_ingots_per_second_circuit = pulp.LpVariable('Copper Ingots Per Second Circuit', lowBound=0) #, cat=pulp.LpInteger)
iron_ingots_per_second_circuit = pulp.LpVariable('Iron Ingots Per Second Circuit', lowBound=0) # , cat=pulp.LpInteger)
magnets_per_second_magnetic_coil = pulp.LpVariable('Magnets Per Second Magnetic Coil', lowBound=0) #, cat=pulp.LpInteger)
copper_ingots_per_second_magnetic_coil = pulp.LpVariable('Copper Ingots Per Second Magnet Coil', lowBound=0) #, cat=pulp.LpInteger)
circuits_per_second_matrix = pulp.LpVariable('Circuits Per Second Matrix', lowBound=0)
magnetic_coils_per_second_matrix = pulp.LpVariable('Magnetic Coils Per Second Matrix', lowBound=0)
iron_ore_per_second = pulp.LpVariable('Iron Ore Per Second', lowBound=0)
copper_ore_per_second = pulp.LpVariable('Copper Ore Per Second', lowBound=0)
matrix_per_second = pulp.LpVariable('matrix_per_second', lowBound=0)

# Define the optimization problem as a minimization problem
problem = pulp.LpProblem('Electromagnetic Matrix Production', pulp.LpMinimize)

# Define objective function
problem += copper_ingots_per_second_circuit + iron_ingots_per_second_circuit + iron_ore_per_second + copper_ore_per_second

# Define constraints for raw materials
problem += iron_ore_per_second <= 3.5
problem += copper_ore_per_second <= 3.5

# Define constraints for direct consumers of raw resources
problem += copper_ore_per_second >= copper_ingots_per_second_circuit + copper_ingots_per_second_magnetic_coil
problem += iron_ore_per_second >= iron_ingots_per_second_circuit + magnets_per_second_magnetic_coil

# Define constraints for a circuit board
problem += copper_ingots_per_second_circuit >= .75 * circuits_per_second_matrix
problem += iron_ingots_per_second_circuit >= 1.5 * circuits_per_second_matrix

# Define constraints for a magnetic coil
problem += magnets_per_second_magnetic_coil >= 2 * magnetic_coils_per_second_matrix
problem += copper_ingots_per_second_magnetic_coil >= magnetic_coils_per_second_matrix

# Define constraints for a matrix
problem += circuits_per_second_matrix >= 1/3 * matrix_per_second
problem += magnetic_coils_per_second_matrix >= 1/3 * matrix_per_second

problem += matrix_per_second >= 1/3

# Solve the problem
status = problem.solve()

# Check if a solution was found
if status == pulp.LpStatusOptimal:
    print('Copper Ingots Per Second Circuit:', copper_ingots_per_second_circuit.value())
    print('Iron Ingots Per Second Circuit:', iron_ingots_per_second_circuit.value())
    print('Magnets Per Second Magnetic Coil:', magnets_per_second_magnetic_coil.value())
    print('Copper Ingots Per Second Magnet Coil:', copper_ingots_per_second_magnetic_coil.value())
    print('Circuits Per Second Matrix:', circuits_per_second_matrix.value())
    print('Magnetic Coils Per Second Matrix:', magnetic_coils_per_second_matrix.value())
    print('Iron Ore Per Second:', iron_ore_per_second.value())
    print('Copper Ore Per Second:', copper_ore_per_second.value())
    print('Matrix Per Second:', matrix_per_second.value())

else:
    print("No solution found.")
