import pandas as pd

def detect_anomalies(csv_path: str, z_threshold: float = 3.0):
    df = pd.read_csv(csv_path)
    z_scores = (df - df.mean()) / df.std(ddof=0)
    anomalies = df[(z_scores.abs() > z_threshold).any(axis=1)]
    return anomalies.to_dict(orient="records")
