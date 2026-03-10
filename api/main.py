from fastapi import FastAPI
import joblib
import time
import sqlite3

app = FastAPI()

# load model
model = joblib.load("model/spam_model.pkl")
vectorizer = joblib.load("model/vectorizer.pkl")

@app.get("/")
def home():
    return {"message": "AI Model Monitoring API Running"}

@app.post("/predict")
def predict(text: str):

    start = time.time()

    text_vec = vectorizer.transform([text])

    prediction = model.predict(text_vec)[0]
    confidence = model.predict_proba(text_vec).max()

    latency = time.time() - start

    label = "spam" if prediction == 1 else "ham"

    # store metrics
    conn = sqlite3.connect("monitoring.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO predictions (message, prediction, confidence, latency) VALUES (?, ?, ?, ?)",
        (text, label, float(confidence), latency)
    )

    conn.commit()
    conn.close()

    return {
        "prediction": label,
        "confidence": float(confidence),
        "latency": latency
    }