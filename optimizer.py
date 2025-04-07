
import pulp

class NetworkOptimizer:
    def __init__(self, costs, capacities, demands):
        self.costs = costs
        self.capacities = capacities
        self.demands = demands
        self.num_warehouses = len(capacities)
        self.num_regions = len(demands)
        self.problem = pulp.LpProblem("NetworkDesign", pulp.LpMinimize)
        self.x = {}  # decision variables

    def build_model(self):
        # Decision variables: x[i][j] = 1 if warehouse i serves region j
        for i in range(self.num_warehouses):
            for j in range(self.num_regions):
                self.x[i, j] = pulp.LpVariable(f"x_{i}_{j}", cat='Binary')

        # Objective: Minimize total cost
        self.problem += pulp.lpSum(self.costs[i][j] * self.x[i, j]
                                   for i in range(self.num_warehouses)
                                   for j in range(self.num_regions)), "TotalCost"

        # Each region must be served by exactly one warehouse
        for j in range(self.num_regions):
            self.problem += pulp.lpSum(self.x[i, j] for i in range(self.num_warehouses)) == 1, f"Demand_{j}"

        # Warehouse capacity constraints
        for i in range(self.num_warehouses):
            self.problem += pulp.lpSum(self.demands[j] * self.x[i, j]
                                       for j in range(self.num_regions)) <= self.capacities[i], f"Capacity_{i}"

    def solve(self):
        self.problem.solve()
        return pulp.LpStatus[self.problem.status]
