import pandas as pd
from sklearn.linear_model import LinearRegression

def forecast_kpi(csv_path: str):
    """Simple linear regression forecast for next period."""
    df = pd.read_csv(csv_path)
    X = df.index.values.reshape(-1, 1)
    y = df.iloc[:, -1].values
    model = LinearRegression().fit(X, y)
    next_period = [[len(X)]]  # next index
    prediction = model.predict(next_period)[0]
    return prediction
