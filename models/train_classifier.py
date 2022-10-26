import sys
import re
import pickle

import numpy as np
import pandas as pd

from sqlalchemy import create_engine

import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.stem.wordnet import WordNetLemmatizer

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

from sklearn.pipeline import Pipeline
from sklearn.pipeline import FeatureUnion
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.multioutput import MultiOutputClassifier


def load_data(database_filepath):
    '''
    Args:
        ... (): ...
    Return:
        ... (): ...
    '''
    engine = create_engine('sqlite:///{}'.format(database_filepath))

    df = pd.read_sql_table('Messages', engine)

    X = df['message'].copy()

    Y = df.columns
    Y = Y.drop(['id', 'message', 'original', 'genre'])
    Y = df[Y].copy()

    return X, Y, Y.columns


def tokenize(text):
    '''
    Args:
        text (str): ...
    Return:
        ... (): ...
    '''
    # Normalise text
    text = text.lower()

    # Remove URLs
    url_mask = 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'

    urls = re.findall(url_mask, text)
    for url in urls:
        text = text.replace(url, 'urlplaceholder')

    # Remove punctuation
    text = re.sub(r'[^a-zA-Z0-9]', ' ', text)

    # Tokenise text
    tokens = word_tokenize(text)

    # Remove stopwords
    tokens = [token for token in tokens if token not in stopwords.words('english')]

    # Stemming
    stemmer = PorterStemmer()
    stemmed_tokens = [stemmer.stem(token) for token in tokens]

    # Lemmatisation
    lemmatiser = WordNetLemmatizer()
    lemmed_tokens = [lemmatiser.lemmatize(token) for token in stemmed_tokens]
    lemmed_tokens = [lemmatiser.lemmatize(token, pos='v') for token in lemmed_tokens]

    clean_tokens = lemmed_tokens

    return clean_tokens


def build_model():
    '''
    Args:
        ... (): ...
    Return:
        ... (): ...
    '''
    # Create model pipeline
    pipeline = Pipeline([

        ('nlp_pipeline', Pipeline([
            ('vectorise', CountVectorizer(tokenizer=tokenize)),
            ('tfidf', TfidfTransformer())
        ])),

        ('classifier', MultiOutputClassifier(RandomForestClassifier()))

    ])

    # Define grid search parameters
    parameters = {
        '': ,
        '': (
            {'': },
            {'': },
            {'': }
        )
    }

    cross_validated_model = GridSearchCV(pipeline, param_grid=parameters)

    return cross_validated_model


def evaluate_model(model, X_test, Y_test, category_names):
    '''
    Args:
        ... (): ...
    Return:
        ... (): ...
    '''
    Y_pred = model.predict(X_test)
    accuracy = (Y_pred == Y_test.values).mean()
    print('Model Accuracy: {:.3f}%'.format(accuracy * 100))

    return None


def save_model(model, model_filepath):
    '''
    Args:
        model (): The classification model
        model_filepath (str): The file path for classification model pickle file
    Return:
        None
    '''
    with open(model_filepath, 'wb') as model_file:
        pickle.dump(model, model_file)
        model_file.close()

    return None


def main():
    if len(sys.argv) == 3:
        database_filepath, model_filepath = sys.argv[1:]
        print('Loading data...\n    DATABASE: {}'.format(database_filepath))
        X, Y, category_names = load_data(database_filepath)
        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)
        
        print('Building model...')
        model = build_model()
        
        print('Training model...')
        model.fit(X_train, Y_train)
        
        print('Evaluating model...')
        evaluate_model(model, X_test, Y_test, category_names)

        print('Saving model...\n    MODEL: {}'.format(model_filepath))
        save_model(model, model_filepath)

        print('Trained model saved!')

    else:
        print('Please provide the filepath of the disaster messages database '\
              'as the first argument and the filepath of the pickle file to '\
              'save the model to as the second argument. \n\nExample: python '\
              'train_classifier.py ../data/DisasterResponse.db classifier.pkl')


if __name__ == '__main__':
    main()
