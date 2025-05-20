import pandas as pd
import os
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer

# データ読み込み
df = pd.read_csv("data/Titanic.csv")
X = df.drop("Survived", axis=1)
y = df["Survived"].astype(int)

# 前処理
numeric_features = ["Age", "Pclass", "SibSp", "Parch", "Fare"]
categorical_features = ["Sex", "Embarked"]

numeric_transformer = Pipeline([
    ("imputer", SimpleImputer(strategy="median")),
    ("scaler", StandardScaler()),
])

categorical_transformer = Pipeline([
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("onehot", OneHotEncoder(handle_unknown="ignore")),
])

preprocessor = ColumnTransformer([
    ("num", numeric_transformer, numeric_features),
    ("cat", categorical_transformer, categorical_features),
])

# モデル構築 & 学習
model = Pipeline([
    ("preprocessor", preprocessor),
    ("classifier", RandomForestClassifier(n_estimators=100, random_state=42)),
])
X_train, _, y_train, _ = train_test_split(X, y, test_size=0.2, random_state=42)
model.fit(X_train, y_train)

# 保存
os.makedirs("models", exist_ok=True)
with open("models/titanic_model_old.pkl", "wb") as f:
    pickle.dump(model, f)

