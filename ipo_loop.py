
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

from models.predictor import DemandPredictor
from models.optimizer import NetworkOptimizer

# Load data
X = pd.read_csv('data/raw/features.csv').values
y = pd.read_csv('data/raw/demand.csv').values

# For simplicity, use demand for one region (can be extended to all)
y = y[:, 0]  # region_1

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize predictor
predictor = DemandPredictor()

# Iterative loop
for iteration in range(5):
    print(f"\n--- Iteration {iteration + 1} ---")
    
    # Train model
    predictor.train(X_train, y_train)
    y_pred = predictor.predict(X_train)

    # Create optimization problem with predicted demand
    # Simulate 3 warehouses with random cost and capacity
    num_regions = len(y_pred)
    costs = np.random.randint(5, 15, size=(3, num_regions))
    capacities = [int(sum(y_pred)/3 + 50)] * 3
    optimizer = NetworkOptimizer(costs, capacities, y_pred)
    optimizer.build_model()
    status = optimizer.solve()

    print(f"Optimization Status: {status}")

    # Optional: Update training labels with optimized assignments (not done here)
    # y_train = refined_labels_from_optimization

# Final test prediction
y_test_pred = predictor.predict(X_test)
mse = mean_squared_error(y_test, y_test_pred)
print(f"\nFinal Test MSE: {mse:.4f}")
