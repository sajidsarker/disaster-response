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
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.multioutput import MultiOutputClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix


def load_data(database_filepath):
    '''
    Args:
        database_filepath (str): The file path for the database
    Return:
        X (DataFrame): Dataset containing messages (features)
        Y (DataFrame): Dataset containing target categories
        category_names (list of str): List of target category names
    '''
    engine = create_engine('sqlite:///{}'.format(database_filepath))
    df = pd.read_sql_table('Messages', engine)
    X = df['message'].copy()
    Y = df.iloc[:, 4:].copy()
    category_names = Y.columns

    return X, Y, category_names


def tokenize(text):
    '''
    Args:
        text (str): The message to be tokenised
    Return:
        clean_tokens (list of str): The message after cleaning and tokenisation 
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
        None
    Return:
        cross_validated_model (list of str): Cross validated classification model
    '''
    # Create model pipeline
    pipeline = Pipeline([

        ('nlp_pipeline', Pipeline([
            ('vectorise', CountVectorizer(tokenizer=tokenize)),
            ('tfidf', TfidfTransformer())
        ])),

        # Classifier if using Ada Boost
        ('classifier', MultiOutputClassifier(AdaBoostClassifier()))
        
        # Classifier if using Random Forest
        #('classifier', MultiOutputClassifier(RandomForestClassifier()))

    ])

    # Define grid search parameters
    parameters = {
        # Parameters if using Ada Boost
        'classifier__estimator__n_estimators': [50, 60, 70],
        'classifier__estimator__learning_rate': [1, 0.1, 0.05]
        # Parameters if using Random Forest
        #'classifier__estimator__n_estimators': [50, 75, 100],
        #'classifier__estimator__criterion': ['gini', 'entropy'],
        #'classifier__estimator__max_depth': [4, 6, 8, None]
    }

    # Assign pipeline and parameters to grid search model for cross validation
    cross_validated_model = GridSearchCV(pipeline, param_grid=parameters)

    return cross_validated_model


def evaluate_model(model, X_test, Y_test, category_names):
    '''
    Args:
        model: The classification model
        X_test (DataFrame): Testing dataset containing messages (features)
        Y_test (DataFrame): Testing dataset containing target categories
        category_names (list of str): List of target category names
    Return:
        None
    '''
    # Generate category predictions
    Y_pred = model.predict(X_test)

    # Display classification report by feature
    for i in enumerate(category_names):
        print('Target Variable {}: {}'.format(i[0], i[1]))
        print('Class Labels:', np.unique(Y_pred[:, i[0]]))
        print(classification_report(Y_test.iloc[:, i[0]], Y_pred[:, i[0]]))

    # Calculate model accuracy
    accuracy = (Y_pred == Y_test.values).mean()
    print('Model Accuracy: {:.3f}%'.format(accuracy * 100))

    return None


def save_model(model, model_filepath):
    '''
    Args:
        model: The classification model
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
