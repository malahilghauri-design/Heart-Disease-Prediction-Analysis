import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score
from sklearn.model_selection import train_test_split

# Load data
X = pd.read_csv('data_sets/anti_gravity_experiment/X.csv')
y = pd.read_csv('data_sets/anti_gravity_experiment/y.csv')

# Train/Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Random Forest
clf = RandomForestClassifier(n_estimators=100)
clf.fit(X_train, y_train.values.ravel())

# Predict and Evaluate
preds = clf.predict(X_test)
print(f"Accuracy: {accuracy_score(y_test, preds)*100:.2f}%")
print(f"F1 Score: {f1_score(y_test, preds, average='macro')*100:.2f}%")