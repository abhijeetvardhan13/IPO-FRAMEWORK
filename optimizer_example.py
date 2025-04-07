
import numpy as np
from models.optimizer import NetworkOptimizer

# Example cost, capacity, and demand data
costs = np.random.randint(5, 15, size=(3, 10))        # 3 warehouses, 10 regions
capacities = [100, 150, 120]                          # warehouse capacities
demands = np.random.randint(10, 30, size=10)          # regional demands

# Instantiate and build the optimizer
optimizer = NetworkOptimizer(costs, capacities, demands)
optimizer.build_model()
status = optimizer.solve()

# Print status and dummy output
print(f"Optimization Status: {status}")
