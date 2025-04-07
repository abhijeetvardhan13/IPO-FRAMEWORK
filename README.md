Research Problem Summary 

The paper proposes a Prediction-and-Optimization framework to solve a distribution network design problem in e-logistics. The goal is to design a distribution network (choosing hub locations and assigning demand nodes to them) by learning from data (historical demand, costs, etc.). 

Core Challenges Addressed: 

Classical network design problems assume known parameters. 

In real-world e-logistics, parameters like demand and cost may be noisy or partially observed. 

There's a need to jointly learn from data and optimize network decisions. 

 

Step 1: Understand the Research Problem 

Goal: 
 Design an efficient e-logistics distribution network using an iterative prediction-and-optimization framework. The approach combines: 

Demand Prediction Model (to forecast product demand across regions) 

Optimization Model (to choose the best warehouse & fulfillment center placements and flows) 

Key Idea: 
 Instead of treating prediction and optimization separately, the paper proposes a loop that iteratively improves predictions and optimization decisions together, which improves the quality of network design. 

 

 

Step 2: Problem Components 

Component 

Description 

Prediction Module 

Uses a machine learning model (e.g., regression or neural network) to forecast demand. 

Optimization Module 

Solves a Mixed Integer Linear Program (MILP) for network design decisions. 

Iterative Framework 

Updates the predictor using optimized labels to improve both models jointly. 

 

Step 3: Environment & Tools 

Python 3.8+ 

Libraries: numpy, pandas, scikit-learn, pulp or pyomo (for optimization), matplotlib, torch (if deep learning is used) 

GitHub account and Git installed 

Step 4: Code Structure & GitHub Setup 

 Suggested Folder Structure 

 

 

 

 

 

 

 

 

 

 

css 

CopyEdit 

distribution-network-design/ 
├── data/ 
│   ├── raw/ 
│   └── processed/ 
├── models/ 
│   ├── predictor.py 
│   └── optimizer.py 
├── notebooks/ 
│   └── EDA.ipynb 
├── main.py 
├── requirements.txt 
├── README.md 
└── .gitignore 
 

 GitHub Instructions 

Create a new GitHub repo named: distribution-network-design. 

On your local machine: 

bash 

CopyEdit 

git clone https://github.com/YOUR_USERNAME/distribution-network-design.git 
cd distribution-network-design 
 

Create files and folders as per the structure above. 

Add & commit: 

bash 

CopyEdit 

git add . 
git commit -m "Initial setup for project" 
git push origin main 

 

Step 5: Implementing the Framework 

1. Demand Predictor (models/predictor.py) 

python 

CopyEdit 

from sklearn.linear_model import LinearRegression 
 
class DemandPredictor: 
    def __init__(self): 
        self.model = LinearRegression() 
 
    def train(self, X_train, y_train): 
        self.model.fit(X_train, y_train) 
 
    def predict(self, X): 
        return self.model.predict(X) 
 

2. Optimization Model (models/optimizer.py) 

Use PuLP or Pyomo for MILP. 

python 

CopyEdit 

import pulp 
 
class NetworkOptimizer: 
    def __init__(self, costs, capacities, demands): 
        self.costs = costs 
        self.capacities = capacities 
        self.demands = demands 
        self.problem = pulp.LpProblem("NetworkDesign", pulp.LpMinimize) 
 
    def build_model(self): 
        # Define decision variables and constraints 
        pass  # Implement MILP logic here 
 
    def solve(self): 
        self.problem.solve() 
        return self.problem.status 
 

3. Iterative Loop (main.py) 

python 

CopyEdit 

from models.predictor import DemandPredictor 
from models.optimizer import NetworkOptimizer 
 
# Load data 
# Train predictor 
# Predict demand 
# Optimize network 
# Update labels and repeat 

 

Step 6: Replicate Results 

Run experiments using the dataset mentioned in the paper. 

Measure: 

Demand prediction error (RMSE) 

Total cost of distribution network 

Compare your metrics with those in the paper to confirm replication. 

 

Step 7: Write the README.md 

markdown 

CopyEdit 

# Distribution Network Design using Iterative Prediction-and-Optimization 
 
This project replicates results from the paper _"Iterative Prediction-and-Optimization for E-Logistics Distribution Network Design"_. 
 
## Structure 
- `models/`: Predictor and Optimizer classes 
- `data/`: Raw and processed datasets 
- `main.py`: Script for running the framework 
 
## How to Run 
```bash 
pip install -r requirements.txt 
python main.py 
