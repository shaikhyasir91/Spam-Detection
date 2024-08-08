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

## Code Explanation

### Data Loading and Preprocessing:
The dataset is loaded using pandas and unnecessary columns are dropped.
The messages and their corresponding labels are extracted.

### Data Visualization:
A count plot visualizes the distribution of spam and ham messages.

### Feature Extraction:
CountVectorizer is used to convert the text data into a matrix of token counts.

### Model Training:
The data is split into training and testing sets using train_test_split.
A MultinomialNB classifier is trained on the training set.

### Prediction and Evaluation:
The model predicts the labels for the test set.
The accuracy of the model is evaluated using accuracy_score.

### Real-time Prediction:
The user can input a message, and the model will predict whether it's spam or ham.



## Contribution

Feel free to fork this repository and contribute by submitting a pull request. For major changes, please open an issue first to discuss what you would like to change.
