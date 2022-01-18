import pandas as pd
from sklearn.feature_extraction import _stop_words
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import classification_report

class Clasificador:
    Clasificador=LogisticRegression(multi_class='multinomial', max_iter=10)

    def __init__(self):
        stop_words=_stop_words.ENGLISH_STOP_WORDS
        rows_data = pd.read_csv("dataset_final.csv", encoding="latin-1")
        rows_stop_words= pd.read_csv("stopwords", sep='\n', header=None)
        tweets = rows_data['fullText'].values
        polaridad = rows_data['polaridad'].values
        stop_words=stop_words.union(list(rows_stop_words[0]))
        Tweet_train, Tweet_test, polaridad_train, polaridad_test = train_test_split(tweets, polaridad, test_size=0.1, random_state=4)
        self.vectorizer = CountVectorizer(analyzer='word', encoding="latin-1", lowercase=True, token_pattern=r'\b\w+\b', max_df=0.9, min_df=0.01, ngram_range=(1,2), stop_words=stop_words)
        
        self.vectorizer.fit(Tweet_train)
        self.v_train = self.vectorizer.transform(Tweet_train)
        self.v_test = self.vectorizer.transform(Tweet_test)

        self.Clasificador.fit(self.v_train, polaridad_train)
        self.eficiencia = self.Clasificador.score(self.v_test, polaridad_test)
        resultado = self.Clasificador.predict(self.v_test)
        print(classification_report(polaridad_test,resultado ))











