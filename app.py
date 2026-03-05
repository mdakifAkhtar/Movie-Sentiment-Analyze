from flask import Flask, render_template, request
import pickle

model = pickle.load(open("sentiment_model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    review = request.form["review"]

    vector = vectorizer.transform([review])

    prediction = model.predict(vector)[0]

    probability = model.predict_proba(vector).max()

    confidence = round(probability * 100, 2)

    if prediction == "positive":
        emoji = "😊"
        color = "positive"
    else:
        emoji = "😡"
        color = "negative"

    return render_template(
        "index.html",
        prediction=prediction,
        emoji=emoji,
        confidence=confidence,
        review=review,
        color=color
    )


if __name__ == "__main__":
    app.run(debug=True)