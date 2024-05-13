import joblib
import pandas as pd
import re

from sklearn.utils import resample
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.linear_model import SGDClassifier
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.metrics import f1_score


class My_NLP:
    def __init__(self):
        self.loaded_model = joblib.load('./data/benGvir_NLP_filtered.joblib')
        print("Model loaded")

    def preproc(self, text):
        text = text.lower()
        text = re.sub(
            r"(@[\w]+)|([^0-9A-z \t])|(\w+:\/\/\s+)|^rt|http.+?", '', text)

        text = re.sub(r'#\w+\s?', '', text)

        print(f"asdasd = {text}")
        return text

    def getPredict(self, text):
        text = self.preproc(text)

        return self.loaded_model.predict([text])[0]

    def get_model_length(self):
        return len(self.loaded_model)
