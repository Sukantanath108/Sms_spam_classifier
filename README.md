# Sms_spam_classifier

Welcome to the SMS Spam Classifier project! This repository contains code, examples, and documentation to help you build and experiment with a machine learning model for SMS spam detection. The project utilizes the popular UCI SMS Spam Collection dataset.

## Overview
This project demonstrates how to preprocess, train, and evaluate a spam classifier using the UCI SMS Spam Collection dataset. It includes:

1.Data preprocessing scripts
2.Feature extraction and engineering techniques
3.Model training and evaluation pipelines
4.Utilities for testing and visualizing the classifier's performance

## Requirements
You need jupyter notebook to run the ipynb file. You can also use google colab for easy setup.
Used streamlit to deploy on site. Check the pythonproject1 file for python files used to run this on website.

## How to Clone and Use This Repository

1. **Clone the repository**:
   ```bash
   git clone <repository_url>

2. **Download Datasets**:
   ```bash
   cd Dataset
3. **To check what files are inside the dataset folder:**
   ```bash
   ls
4. **Install dependencies:**
   ```bash
   npm install nltk
5 . **Download necessary packages for this project**
   ```bash
   nltk.download('stopwords')
   nltk.download('punkt')
   ```

## Issue with the model : 
The algorithms trained on unbalanced datasets tends to be biased towards the majority class. I tried to implement the Spam/Ham classifier using Naive Bayes, random forest and ExtraTree Classsifier. The precision ranges from 0.98 to 1.0. But I observe that it is biased towards Ham class (as it is in majority) it works for some statements, but when little bit changes are applied it doesn't work the way it has to.
Mosly it is biased towards certain words such as claim, prize , alert etc.

