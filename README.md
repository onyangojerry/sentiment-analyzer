---

# Sentiment Analysis Tool

This Python script is designed to perform sentiment analysis on given text input. By analyzing positive and negative sentences, it can classify the sentiment of a sentence as either positive or negative. This tool leverages basic natural language processing techniques to calculate word frequencies and determine the overall sentiment of sentences based on trained models from provided text files.

## Features

- Word frequency calculation
- Probability distribution conversion
- Sentiment classification
- Accuracy assessment for model performance

## Setup

To run this script, you need a Python environment (Python 3.x recommended). No additional libraries are required beyond the Python standard library.

1. Clone or download this repository to your local machine.
2. Ensure you have Python installed by running `python --version` in your terminal.
3. Prepare your dataset: positive and negative sentences in separate text files for both training and testing the model.

## Usage

The script is executed from the command line. Navigate to the directory containing the script and run it using Python. Here's a basic example:

```sh
python sentiment_analysis.py
```

Upon running, the script will prompt you to enter a sentence. After inputting your sentence, it will classify the sentiment as positive or negative based on the trained model.

### Training the Model

To train the model, you need to provide it with text files containing positive and negative sentences:

```python
train_model('positive_sentences.txt')
train_model('negative_sentences.txt')
```

### Classifying Sentiment

To classify the sentiment of a sentence:

```python
positives = train_model('positive_sentences.txt')
negatives = train_model('negative_sentences.txt')
print(classify("Your sentence here.", positives, negatives))
```

### Assessing Accuracy

To assess the accuracy of the model, provide it with test files for positive and negative sentences:

```python
get_accuracy('positive_test.txt', 'negative_test.txt', 'positive_train.txt', 'negative_train.txt')
```

## Contributing

Your contributions are welcome! If you'd like to improve the accuracy of the sentiment analysis or add new features, please feel free to fork this repository, make your changes, and submit a pull request.

## License

This project is open-source and available under the MIT License.

---
