from pulp import LpMaximize, LpProblem, LpVariable, value, PULP_CBC_CMD

problem = LpProblem("Production_Optimization", LpMaximize) # Create problem

lemonade = LpVariable("Lemonade", lowBound=0, cat='Integer') # Decision variable
fruit_juice = LpVariable("Fruit_Juice", lowBound=0, cat='Integer')

problem += lemonade + fruit_juice # Objective function

# Constraints
problem += 2 * lemonade + 1 * fruit_juice <= 100  # Water
problem += 1 * lemonade <= 50  # Sugar
problem += 1 * lemonade <= 30  # Lemon Juice
problem += 2 * fruit_juice <= 40  # Fruit Puree

problem.solve() # Solve the problem

print(f"Lemonade: {int(value(lemonade))} units")
print(f"Fruit Juice: {int(value(fruit_juice))} units")
print(f"Total Production: {int(value(problem.objective))} units")