# Import required libraries
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.tree import DecisionTreeClassifier

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.25,
    random_state=42
)

# Create Decision Tree model
# criterion can be "gini" or "entropy"
# max_depth can be 5, 10, etc.
model = DecisionTreeClassifier(
    criterion="gini",
    max_depth=10
)

# Train the model
model.fit(X_train, y_train)

# Predict test data
y_pred = model.predict(X_test)

# Generate classification report
report = classification_report(y_test, y_pred)

# Print report
print(report)
... 





... 
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import cross_val_score

# Parameters to test
criterion = ["gini", "entropy"]
max_depth = [5, 10, 15]

# Dictionary to store average scores
avg_scores = {}

# Trial and error tuning
for c in criterion:
    for d in max_depth:

        # Create model
        clf = DecisionTreeClassifier(
            criterion=c,
            max_depth=d
        )

        # Perform 5-fold cross validation
        scores_list = cross_val_score(clf, X, y, cv=5)

        # Store average score
        avg_scores[c + "_" + str(d)] = np.average(scores_list)

# Print all average scores
print(avg_scores)


{
 'gini_5': 0.78,
 'gini_10': 0.82,
 'gini_15': 0.80,
 'entropy_5': 0.79,
 'entropy_10': 0.84,
 'entropy_15': 0.81
}


from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import GridSearchCV

# Create GridSearchCV object
clf = GridSearchCV(
    DecisionTreeClassifier(),
    {
        'criterion': ["gini", "entropy"],
        'max_depth': [5, 10, 15]
    },
    cv=5,
    return_train_score=False
)

# Train model
clf.fit(X, y)

# Show all results
print(clf.cv_results_)


... 




... 
from sklearn import svm
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import GridSearchCV

# Dictionary containing models and parameters
model_params = {

    'decision_tree': {
        'model': DecisionTreeClassifier(),
        'params': {
            'criterion': ['gini', 'entropy'],
            'max_depth': [5, 10, 15]
        }
    },

    'svm': {
        'model': svm.SVC(gamma='auto'),
        'params': {
            'C': [1, 10, 20],
            'kernel': ['rbf', 'linear']
        }
    }
}

# Empty list to store results
scores = []

# Loop through models
for key, val in model_params.items():

    # Apply GridSearchCV
    clf = GridSearchCV(
        val['model'],
        val['params'],
        cv=5,
        return_train_score=False
    )

    # Train model
    clf.fit(X, y)

    # Store best results
    scores.append({
        'model': key,
        'best_score': clf.best_score_,
        'best_params': clf.best_params_
    })

# Print results
print(scores)

