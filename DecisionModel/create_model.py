from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline

import pandas as pd
data = pd.read_csv("commands_dataset.csv")  # Путь к вашему файлу

model_pipeline = Pipeline([
    ("vectorizer", TfidfVectorizer(ngram_range=(1, 2))),
    ("classifier", RandomForestClassifier(n_estimators=1500, random_state=42))
])

# Обучение модели
X = data["text"]  # Тексты запросов
y = data["intent"]  # Метки классов (intents)
model_pipeline.fit(X, y)

# Сохранение модели
import pickle
with open("Overlord_model_v0.1.pkl", "wb") as model_file:
    pickle.dump(model_pipeline, model_file)
