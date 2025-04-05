import pickle
import os

# Load the model and vectorizer correctly
file_path = r"F:\Machine leaarning XDDDD\Spam classifier\model_etc.pkl"
file_path1 = r"F:\Machine leaarning XDDDD\Spam classifier\vectorizer.pkl"

with open(file_path, "rb") as f:
    etc = pickle.load(f)

with open(file_path1, "rb") as f2:
    tfidf = pickle.load(f2)

print(os.path.exists("model_etc_new.pkl"))
