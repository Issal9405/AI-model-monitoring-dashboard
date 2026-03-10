import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib

# load dataset
data = pd.read_csv("../data/spam.csv", encoding="latin-1")[["v1","v2"]]
data.columns = ["label","message"]

# convert labels
data["label"] = data["label"].map({"ham":0,"spam":1})

# split dataset
X_train, X_test, y_train, y_test = train_test_split(
    data["message"], data["label"], test_size=0.2, random_state=42
)

# improved TF-IDF
vectorizer = TfidfVectorizer(
    stop_words="english",
    ngram_range=(1,2),
    max_features=5000
)

X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# improved logistic regression
model = LogisticRegression(max_iter=1000)

model.fit(X_train_vec, y_train)

# evaluate model
preds = model.predict(X_test_vec)
accuracy = accuracy_score(y_test, preds)

print("Model accuracy:", accuracy)

# save model
joblib.dump(model,"spam_model.pkl")
joblib.dump(vectorizer,"vectorizer.pkl")

print("Model trained and saved successfully")