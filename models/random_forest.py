from src.tabular_data_prep import tabular_data_generator
from sklearn.ensemble import RandomForestClassifier



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