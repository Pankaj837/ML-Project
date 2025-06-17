from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

texts = [
    "Let's have lunch tomorrow",
    "Are we still meeting at 10am?",
    "Don't forget to submit the report.",
    "Happy birthday, have a great day!",
    "Can you review my code?",
    "See you at the party tonight.",
    "Congratulations, you have won a lottery, click here!",
    "Earn $1000 per day, no work required.",
    "Exclusive deal just for you, limited time offer!",
    "You won a free vacation to Bahamas, reply now.",
    "Get cheap medicines without prescription now.",
    "This is not spam, I promise you will benefit."
]
labels = [0,0,0,0,0,0, 1,1,1,1,1,1]  # 0=ham, 1=spam

X_train, X_test, y_train, y_test = train_test_split(
    texts, labels, test_size=0.2, random_state=4)
vectorizer = CountVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)
model = LogisticRegression(max_iter=1000)
model.fit(X_train_vec, y_train)
predictions = model.predict(X_test_vec)
print("Test texts and predictions:")
for text, actual, pred in zip(X_test, y_test, predictions):
    print(f"Text: '{text}'")
    print(f"Actual label: {actual}, Predicted label: {pred}\n")
print("Accuracy:", accuracy_score(y_test, predictions))
