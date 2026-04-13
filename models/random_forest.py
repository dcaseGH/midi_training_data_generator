from src.tabular_data_prep import tabular_data_generator
from sklearn.ensemble import RandomForestClassifier
from sklearn.inspection import permutation_importance


features, labels = tabular_data_generator('tabulated_chords.csv')

rf = RandomForestClassifier(
    n_estimators=200,
    max_depth=5,
    min_samples_split=15,
    max_features="sqrt",
    oob_score=True, # Enables self-testing
    random_state=10
)

rf.fit(features, labels)
print(f"OOB Accuracy: {rf.oob_score_}")

# Calculate feature importance using permutation importance
result = permutation_importance(rf, features, labels, n_repeats=10, random_state=42)
importance_scores = result.importances_mean
# Print feature importance scores
for i, score in enumerate(importance_scores):
    print(f"Feature {i}: Importance Score = {score:.4f}")   

#Total of importance scores is 1
# suggests root note may be less important, and final chord is more important?