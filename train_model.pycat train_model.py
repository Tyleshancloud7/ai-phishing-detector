import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Load emails
data = pd.read_csv("emails.csv")

X = data["text"]
y = data["label"]

# Convert text to numbers
vectorizer = TfidfVectorizer(stop_words="english")
X_vectorized = vectorizer.fit_transform(X)

# Train model
model = LogisticRegression()
model.fit(X_vectorized, y)

# Test a new email
test_email = ["Congratulations! You won a free gift card!"]
test_vectorized = vectorizer.transform(test_email)
prediction = model.predict(test_vectorized)[0]

if prediction == 1:
    print("This email is PHISHING!")
else:
    print("This email is SAFE.")
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Load emails
data = pd.read_csv("emails.csv")

X = data["text"]
y = data["label"]

# Convert text to numbers
vectorizer = TfidfVectorizer(stop_words="english")
X_vectorized = vectorizer.fit_transform(X)

# Train model
model = LogisticRegression()
model.fit(X_vectorized, y)

# Test a new email
test_email = ["Congratulations! You won a free gift card!"]
test_vectorized = vectorizer.transform(test_email)
prediction = model.predict(test_vectorized)[0]

if prediction == 1:
    print("This email is PHISHING!")
else:
    print("This email is SAFE.")
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Load emails
data = pd.read_csv("emails.csv")

X = data["text"]
y = data["label"]

# Convert text to numbers
vectorizer = TfidfVectorizer(stop_words="english")
X_vectorized = vectorizer.fit_transform(X)

# Train model
model = LogisticRegression()
model.fit(X_vectorized, y)

# Test a new email
test_email = ["Congratulations! You won a free gift card!"]
test_vectorized = vectorizer.transform(test_email)
prediction = model.predict(test_vectorized)[0]

if prediction == 1:
    print("This email is PHISHING!")
else:
    print("This email is SAFE.")

