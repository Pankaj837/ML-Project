from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

reviews = [
    "I absolutely loved this movie, it was fantastic!",
    "Best movie I have seen in a long time.",
    "An excellent film with great performances.",
    "Truly enjoyed, wonderful story and acting.",
    "It's a masterpiece, highly recommended.",
    "I hated this movie, it was a waste of time.",
    "Worst movie ever, plot was horrible.",
    "Terrible film, do not recommend.",
    "Poor acting and predictable story.",
    "One of the worst films I have watched."
]
labels = [1, 1, 1, 1, 1, 0, 0, 0, 0, 0]  # 1=positive, 0=negative

X_train, X_test, y_train, y_test = train_test_split(
    reviews, labels, test_size=0.2, random_state=4)
vectorizer = CountVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)
classifier = MultinomialNB()
classifier.fit(X_train_vec, y_train)
predictions = classifier.predict(X_test_vec)
print("Test reviews and predictions:")
for review, actual, pred in zip(X_test, y_test, predictions):
    print(f"Review: '{review}'")
    print(f"Actual label: {actual}, Predicted label: {pred}\n")
print("Accuracy:", accuracy_score(y_test, predictions))
