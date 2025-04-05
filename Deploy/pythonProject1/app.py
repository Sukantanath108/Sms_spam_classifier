import pickle
import streamlit as st
import string
import re
import nltk
import os
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords

# Download necessary NLTK resources
nltk.download('stopwords')
nltk.download('punkt')

ps = PorterStemmer()

# Load the model and vectorizer correctly
file_path = r"F:\Machine leaarning XDDDD\Spam classifier\model_etc_new.pkl"
file_path1 = r"F:\Machine leaarning XDDDD\Spam classifier\vectorizer.pkl"

with open(file_path, "rb") as f:
    etc = pickle.load(f)

with open(file_path1, "rb") as f2:
    tfidf = pickle.load(f2)


# Preprocess input from users
def wordsas(text):
    text = text.lower()  # Convert text to lowercase
   # text = re.sub(r'https?://\S+|www\.\S+', '', text)  # Remove URLs
   # text = re.sub(r'<.*?>+', '', text)  # Remove HTML tags
    text = re.sub(r'[%s]' % re.escape(string.punctuation), '', text)  # Remove punctuation
    text = re.sub(r'\n', ' ', text)  # Replace newlines with space
   # text = re.sub(r'\w*\d\w*', '', text)  # Remove words containing numbers
    tokens = nltk.word_tokenize(text)  # Tokenize the text
    filtered_tokens = [word for word in tokens if
                       word not in stopwords.words('english') and word not in string.punctuation]
    stemmed_tokens = filtered_tokens

    return " ".join(stemmed_tokens)


st.title("Sms spam Classifier")

input_sms = st.text_input("Enter your message:")

if st.button('Predict'):
    transformed_sms = wordsas(input_sms)
    print("Transformed Text:", transformed_sms)

    vector_input = tfidf.transform([transformed_sms])
    print("Vector Shape:", vector_input.shape)

    etc_score = etc.predict(vector_input)
    etc_proba = etc.predict_proba(vector_input)

    print("Prediction:", etc_score)
    print("Prediction Probabilities:", etc_proba)

    if etc_score == 1:
        st.header("🚨 This is SPAM!")
    else:
        st.header("✅ This is NOT Spam.")
