# Cyberbullying and Toxicity Detection

This repository contains a Flask web application for detecting toxic language in text input. The app uses pre-trained machine learning models to classify text across six categories of toxicity.

## Project Overview

- `flask_app/toxic_app.py` - Flask application that loads pre-trained TF-IDF vectorizers and classifiers for toxicity detection.
- `flask_app/templates/index_toxic.html` - Web interface for entering text and displaying results.
- `flask_app/static/css/style.css` - Basic styling for the web app.
- `flask_app/*.pkl` - Saved model and vectorizer files used by the Flask app.
- `ToxicityDetection.ipynb` - Notebook in the repository root for exploring or building toxicity detection models.
- `jigsaw datasets/` - Dataset files from the Jigsaw Toxic Comment Classification challenge.

## Toxicity Categories

The app predicts probabilities for the following categories:

- Toxic
- Severe Toxic
- Obscene
- Insult
- Threat
- Identity Hate

A final status is shown using a threshold-based decision:

- `SAFE` if highest probability is below `0.50`
- `WARNING` if highest probability is between `0.50` and `0.75`
- `CYBER THREAT DETECTED` if highest probability is `0.75` or above

## Requirements

- Python 3.8+
- Flask
- scikit-learn
- numpy

If you are using a virtual environment, activate it first.

Install dependencies with:

```bash
pip install flask scikit-learn numpy
```

## Running the App

From the project root, run:

```bash
python flask_app/toxic_app.py
```

Then open the URL shown in the terminal, typically `http://127.0.0.1:5000/`.

## Notes

- The Flask app expects the `.pkl` files to be present in the `flask_app/` directory.
- The app does not currently support model training through the web interface; it uses the saved models directly.
- Training and experimentation were likely performed in `flask_app/Project 4 - Kaggle Toxic Comment Classification Challenge.ipynb`.

## File Structure

```
flask_app/
  toxic_app.py
  toxic_vect.pkl
  toxic_model.pkl
  severe_toxic_vect.pkl
  severe_toxic_model.pkl
  obscene_vect.pkl
  obscene_model.pkl
  insult_vect.pkl
  insult_model.pkl
  threat_vect.pkl
  threat_model.pkl
  identity_hate_vect.pkl
  identity_hate_model.pkl
  templates/
  static/
ToxicityDetection.ipynb
train.csv
jigsaw datasets/
```
