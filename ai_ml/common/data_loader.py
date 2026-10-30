import numpy as np
import pandas as pd


# Load CSV file into pandas DataFrame
def load_csv(path):
    return pd.read_csv(path)


# Split DataFrame into X and y
def df_to_numpy(df, target_column):
    X = df.drop(columns=[target_column]).values
    y = df[target_column].values
    return X, y


# Train split data
def train_test_split(X, y, test_size=0.2, shuffle=True):
    n = len(X)
    indices = np.arange(n)

    if shuffle:
        np.random.shuffle(indices)

    split = int(n * (1 - test_size))
    train_idx, test_idx = indices[:split], indices[split:]

    return X[train_idx], X[test_idx], y[train_idx], y[test_idx]
