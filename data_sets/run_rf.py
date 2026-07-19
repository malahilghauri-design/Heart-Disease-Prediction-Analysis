import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score

# Load data using your file paths
X = pd.read_csv('data_sets/anti_gravity_experiment/X.csv')
y = pd.read_csv('data_sets/anti_gravity_experiment/y.csv')

# Configuration
seeds = [42, 10, 0, 99, 7]
accuracies = []
f1_scores = []

print(f"Starting robust experiment with {len(seeds)} random seeds...")

# Experiment Loop
for s in seeds:
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=s)
    
    clf = RandomForestClassifier(n_estimators=100, random_state=s)
    clf.fit(X_train, y_train.values.ravel())
    
    preds = clf.predict(X_test)
    
    accuracies.append(accuracy_score(y_test, preds))
    f1_scores.append(f1_score(y_test, preds, average='macro'))

# Reporting Results
print(f"\n--- Final Results (Average over {len(seeds)} seeds) ---")
print(f"Average Accuracy: {np.mean(accuracies)*100:.2f}%")
print(f"Average F1 Score: {np.mean(f1_scores)*100:.2f}%")