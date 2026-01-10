# Scenario 6: Custom Evaluation Metric
# Task: Implement a custom metric weighted_accuracy where
# class 0 has a weight of 1 and class 1 has a weight of 2.

import numpy as np  #importing the Pandas library as pd
from sklearn.metrics import make_scorer # This Creates custom scoring metrixx

def weighted_accuracy(y_true, y_pred, weights=None):

    if weights is None:     # If no weights are given, use default weights
        weights = {0: 1, 1: 2}      # Class 0 → weight 1, Class 1 → weight 2

    total_weight = 0.0      # Total weight of all samples
    correct_weight = 0.0    # Weight of correctly predicted samples

    # Go through each actual and predicted value
    for yt, yp in zip(y_true, y_pred):
        w = weights.get(yt, 1)   # Get weight of the actual class
        total_weight += w       # Add to total

        if yt == yp:
            correct_weight += w   # Add weight only if prediction is correct

    return correct_weight / total_weight if total_weight > 0 else 0.0     # Return weighted accuracy

# Convert this function into a scorer for GridSearchCV
weighted_acc_scorer = make_scorer(weighted_accuracy, greater_is_better=True)

# Sample true and predicted labels
y_true = np.array([0, 1, 1, 0, 1])
y_pred = np.array([0, 1, 0, 0, 1])

print("Weighted accuracy:", weighted_accuracy(y_true, y_pred))  # Print weighted accuracy value
