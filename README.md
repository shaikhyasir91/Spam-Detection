# Spam Detection

This project is designed to classify messages as either spam or ham (not spam) using machine learning techniques. The implementation uses the scikit-learn library in Python.

## Project Structure

- `Spam Detection.ipynb`: Jupyter Notebook containing the code for data preprocessing, model training, and evaluation.
- `app.py`: Python script for running the model as a web application.
- `spam.csv`: Dataset used for training and testing the model.

## Dataset

The dataset `spam.csv` contains labeled messages. Each message is classified as either spam or ham.

## Dependencies

- Python
- pandas
- numpy
- scikit-learn
- Flask (for `app.py`)

## Installation

Clone the repository:
   ```bash
   git clone https://github.com/shaikhyasir91/Spam-Detection.git
   ```

## Usage

### Jupyter Notebook

Open `Spam Detection.ipynb` in Jupyter Notebook to see the implementation and results of the spam detection model.

### Web Application

Run the Flask app:
```bash
python app.py
```
Open your browser and go to `http://127.0.0.1:5000/` to use the web interface for spam detection.

## Model Description

The model uses a TF-IDF vectorizer for text feature extraction and a Multinomial Naive Bayes classifier for classification. The dataset is split into training and testing sets, and the model's performance is evaluated using metrics such as accuracy, precision, recall, and F1-score.

## Contribution

Feel free to fork this repository and contribute by submitting a pull request. For major changes, please open an issue first to discuss what you would like to change.
