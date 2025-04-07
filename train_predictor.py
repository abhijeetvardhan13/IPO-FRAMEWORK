
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from models.predictor import DemandPredictor

# Load features and demand
X = pd.read_csv('data/raw/features.csv')
Y = pd.read_csv('data/raw/demand.csv')

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

# Train model
model = DemandPredictor()
model.train(X_train, y_train)

# Predict and evaluate
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print(f'Mean Squared Error on test set: {mse:.4f}')
