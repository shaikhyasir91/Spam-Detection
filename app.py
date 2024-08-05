from flask import Flask, render_template, request
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB

app = Flask(__name__)

# Load the dataset
df = pd.read_csv('spam.csv', encoding='latin-1')

# Prepare data
x = np.array(df['message'])
y = np.array(df['class'])
cv = CountVectorizer()
X = cv.fit_transform(x)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

# Train the classifier
clf = MultinomialNB()
clf.fit(X_train, y_train)

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    if request.method == 'POST':
        sample = request.form['message']
        data = cv.transform([sample]).toarray()
        result = clf.predict(data)[0]
        prediction = 'Not a spam' if result == 'ham' else 'Spam'
    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
