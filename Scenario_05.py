# Scenario 5: Hyperparameter Tuning
# Task: Use GridSearchCV to find the best max_depth (values: [3, 5, 7])
# and n_estimators (values: [50, 100]) for a Random Forest classifier.

from sklearn.ensemble import RandomForestClassifier # Random Forest tuning libraries
from sklearn.model_selection import GridSearchCV    # Tool for hyperparameter tuning
from sklearn.datasets import make_classification    # Creates sample classification data

# Create some fake classification data to test the model
X, y = make_classification(n_samples=1000, n_features=20, random_state=42)

# These are the values we want to try for tuning the model
param_grid = {
    "max_depth": [3, 5, 7],
    "n_estimators": [50, 100]
}

# Create the Random Forest model
rf = RandomForestClassifier(random_state=42)

# GridSearch will try every combination of the above parameters
# and check which one gives the best accuracy using 5-fold cross-validation
grid = GridSearchCV(rf, param_grid=param_grid, cv=5, scoring="accuracy", n_jobs=-1)

grid.fit(X, y)  # Train the model for all parameter combinations

print("Best params:", grid.best_params_)    # Print the best parameter values found

print("Best score:", grid.best_score_)  # Print the best accuracy score


