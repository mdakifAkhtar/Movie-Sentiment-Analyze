🎬 AI Movie Sentiment Analyzer

A Machine Learning web application that analyzes movie reviews and predicts whether the sentiment is Positive 😊 or Negative 😡 using Natural Language Processing (NLP) and Logistic Regression.

The application allows users to input a movie review and instantly receive a sentiment prediction with confidence score through a web interface.

🌐 Live Demo
Try the deployed application:
https://movie-sentiment-analyze-akif7.onrender.com

🚀 Features
	•	Predicts positive or negative sentiment from movie reviews
	•	Displays confidence score (%)
	•	Uses TF-IDF vectorization for text representation
	•	Machine Learning model built with Logistic Regression
	•	Interactive Flask web application
	•	Modern glassmorphism user interface
	•	Real-time prediction from user input

🧠 Machine Learning Pipeline

Text Cleaning
→ Tokenization
→ TF-IDF Vectorization
→ Logistic Regression Model
→ Sentiment Prediction
→ Confidence Score Output

📊 Model Performance

Evaluation on the test dataset:

Metric	Negative	Positive
Precision	0.90	0.88
Recall	0.88	0.90
F1-Score	0.89	0.89

Overall Accuracy:

Accuracy: 0.8904 (≈ 89%)
Additional metrics:

Metric	Score
Macro Average F1	0.89
Weighted Average F1	0.89
Test Samples	10,000

📂 Dataset

IMDB Movie Reviews Dataset

Kaggle Source:
https://www.kaggle.com/datasets/manoharpothumahanthi/imdb-dataset-for-sentiment-analysis

The dataset contains 50,000 labeled movie reviews used for training and evaluation.

⚙️ Tech Stack
	•	Python
	•	Scikit-learn
	•	Flask
	•	Natural Language Processing (NLP)
	•	TF-IDF Vectorization
	•	Logistic Regression
	•	HTML / CSS
	•	Gunicorn (Deployment)

📁 Project Structure

movie-sentiment-analyze
│
├── app.py
├── sentiment_model.pkl
├── vectorizer.pkl
├── requirements.txt
├── README.md
│
└── templates
     └── index.html

🖥️ Example Prediction
Input:
This movie was absolutely amazing and beautifully directed

Output:
😊 Positive
Confidence: 94%

🔮 Future Improvements
	•	Deploy deep learning models (LSTM / BERT) for higher accuracy
	•	Add model comparison (SVM, Naive Bayes, Logistic Regression)
	•	Implement advanced NLP preprocessing
	•	Add sentiment visualization dashboards

👨‍💻 Author
Mohammad Akif
AI / ML Engineer

GitHub:
https://github.com/mdakifAkhtar
