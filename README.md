# Spam Detection using Traditional Machine Learning, Deep Learning and Transformer Models

## Project Overview

This project develops an end-to-end **Spam Message Detection System** using multiple Natural Language Processing (NLP) techniques. The objective is to classify SMS messages as **Spam** or **Ham (Legitimate)** and compare the performance of traditional machine learning, deep learning, and transformer-based models under the same experimental setup.

The project includes data preprocessing, exploratory data analysis, feature engineering, model training, evaluation, comparative analysis, and a Streamlit application for real-time spam prediction.

---

## Objectives

* Build an automated spam detection system.
* Compare multiple NLP approaches on the same dataset.
* Evaluate models using standard classification metrics.
* Deploy the best-performing model using Streamlit.

---

## Dataset

**SMS Spam Collection Dataset**

* Total Messages: 5,572
* Duplicate messages removed before training
* Binary classification:

  * Ham (Legitimate)
  * Spam

The dataset is cleaned, preprocessed, and divided into:

* Training Set (70%)
* Validation Set (15%)
* Test Set (15%)

A fixed random seed and stratified sampling are used to ensure reproducibility.

---

## Project Structure

```
spam_detection_project/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   ├── 01_data_preparation.ipynb
│   ├── 02_traditional_machine_learning.ipynb
│   ├── 03_deep_learning_spam_detection.ipynb
│   ├── 04_transformer_models.ipynb
│   └── 05_model_comparison.ipynb
│
├── report/
│
├── app.py
│
├── requirements.txt
│
└── README.md
```

---

## Notebook Overview

### Notebook 1 — Data Preparation

* Dataset loading
* Duplicate removal
* Exploratory Data Analysis (EDA)
* Text preprocessing
* Label encoding
* Train/Validation/Test split
* Dataset persistence

---

### Notebook 2 — Traditional Machine Learning

Models implemented:

* Multinomial Naive Bayes
* Logistic Regression
* Linear Support Vector Machine (SVM)

Feature Engineering:

* TF-IDF Vectorization
* Unigrams + Bigrams

Evaluation:

* Accuracy
* Precision
* Recall
* F1 Score
* Confusion Matrix

---

### Notebook 3 — Deep Learning

Models implemented:

* LSTM
* Bidirectional LSTM (BiLSTM)

Framework:

* TensorFlow / Keras

---

### Notebook 4 — Transformer Models

Transformer architectures:

* BERT
* DistilBERT

Framework:

* Hugging Face Transformers
* PyTorch

Fine-tuning was performed for binary spam classification.

---

### Notebook 5 — Model Comparison

Compares every model using common evaluation metrics.

Includes:

* Accuracy
* Precision
* Recall
* F1 Score
* Confusion Matrices
* Performance Comparison

---

## Text Preprocessing Pipeline

The preprocessing pipeline includes:

* Lowercasing
* URL Removal
* Number Removal
* Punctuation Removal
* Stopword Removal
* Lemmatization

---

## Models Evaluated

### Traditional Machine Learning

* Multinomial Naive Bayes
* Logistic Regression
* Linear SVM

### Deep Learning

* LSTM
* Bidirectional LSTM

### Transformer Models

* DistilBERT
* BERT

---

## Evaluation Metrics

The models were evaluated using:

* Accuracy
* Precision
* Recall
* F1 Score
* Confusion Matrix

---

## Technologies Used

Programming Language

* Python

Libraries

* Pandas
* NumPy
* Scikit-learn
* TensorFlow
* PyTorch
* Hugging Face Transformers
* NLTK
* Matplotlib
* Seaborn
* Streamlit

---

## Streamlit Application

A Streamlit web application was developed for real-time spam message classification.

Users can enter a custom message and receive an instant prediction indicating whether the message is Spam or Ham.

---

## Future Improvements

* Hyperparameter optimization
* Cross-validation
* Additional transformer architectures (RoBERTa, ALBERT, DeBERTa)
* Explainable AI using SHAP/LIME
* Docker deployment
* REST API deployment

---

## Author

**Harsh Prasad**

M.Sc. Data Science

Vellore Institute of Technology (VIT)

---

## License

This project is intended for academic and educational purposes.
