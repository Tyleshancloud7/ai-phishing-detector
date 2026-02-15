import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import pickle
from flask import Flask, request, jsonify

# Load dataset and train model
data = pd.read_csv("emails.csv")
X = data["text"]
y = data["label"]

vectorizer = TfidfVectorizer(stop_words="english")
X_vectorized = vectorizer.fit_transform(X)

model = LogisticRegression()
model.fit(X_vectorized, y)

# Save model and vectorizer
pickle.dump(model, open("model.pkl", "wb"))
pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))

# Create Flask app
app = Flask(__name__)

@app.route("/predict", methods=["POST"])
def predict():
    # Get email text from request
    email = request.json["email"]
    email_vectorized = vectorizer.transform([email])
    
    # Predict phishing
    prediction = model.predict(email_vectorized)[0]
    probability = model.predict_proba(email_vectorized)[0][1]  # risk score
    
    return jsonify({
        "is_phishing": int(prediction),
        "risk_score": float(probability)
    })

if __name__ == "__main__":
    app.run(debug=True)

