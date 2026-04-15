import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from src.tabular_data_prep import tabular_data_generator

# 1. Prepare your data (X = integer features, y = target)
features, labels = tabular_data_generator('tabulated_chords.csv')
X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2)

# Define early stopping in the constructor
model = xgb.XGBRegressor(
    n_estimators=250,
    learning_rate=0.03,
    early_stopping_rounds=15,  
    max_depth=4,
    sub_sample=0.8,
    colsample_bytree=0.8,
    gamma=2.5,
    random_state=10
    )

# When fitting, you still need to provide the evaluation set
model.fit(
    X_train, y_train,
    eval_set=[(X_test, y_test)],
    verbose=False
)

# 4. Predict
predictions = model.predict(X_test)
# 5. Evaluate
mse = mean_squared_error(y_test, predictions)
print(f"Mean Squared Error: {mse:.4f}")

# Feature importance
importance_scores = model.feature_importances_
for i, score in enumerate(importance_scores):
    print(f"Feature {i}: Importance Score = {score:.4f}")   