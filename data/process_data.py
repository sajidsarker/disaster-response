import sys

import numpy as np
import pandas as pd

from sqlalchemy import create_engine


def load_data(messages_filepath, categories_filepath):
    '''
    Args:
        messages_filepath (str): The file path for csv file containing messages
        categories_filepath (str): The file path for csv file containing categories
    Return:
        df (DataFrame): A merged dataframe of messages and categories
    '''
    messages = pd.read_csv(messaged_filepath)
    categories = pd.read_csv(categories_filepath)
    df = messages.merge(categories, on='id')

    return df


def clean_data(df):
    '''
    Args:
        df (DataFrame): A merged dataframe of messages and categories
    Return:
        df (DataFrame): A merged and cleaned dataframe of messages and categories
    '''
    # Convert categories into categorical variables
    categories = df['categories'].copy().str.split(pat=';', expand=True)
    categories.columns = [x[0:-2] for x in categories.iloc[0, :]]
    for column in categories:
        categories[column] = categories[column].str[-1]
        categories[column] = categories[column].astype(int)
    categories['id'] = df['id'].copy()
    df.drop('categories', inplace=True, axis=1)
    df = df.merge(categories, on='id')

    # Remove duplicates
    duplicates = df.duplicated(subset=['id', 'message'], keep='first')
    df = df[duplicates == False]
    
    return df


def save_data(df, database_filename):
    '''
    Args:
        df (DataFrame): A merged and cleaned dataframe of messages and categories
        database_filename (str): The file name for the database
    Return:
        None
    '''
    engine = create_engine('sqlite:///{}'.format(database_filename))
    df.to_sql('Messages', engine, index=False)
    
    return None


def main():
    if len(sys.argv) == 4:

        messages_filepath, categories_filepath, database_filepath = sys.argv[1:]

        print('Loading data...\n    MESSAGES: {}\n    CATEGORIES: {}'
              .format(messages_filepath, categories_filepath))
        df = load_data(messages_filepath, categories_filepath)

        print('Cleaning data...')
        df = clean_data(df)
        
        print('Saving data...\n    DATABASE: {}'.format(database_filepath))
        save_data(df, database_filepath)
        
        print('Cleaned data saved to database!')
    
    else:
        print('Please provide the filepaths of the messages and categories '\
              'datasets as the first and second argument respectively, as '\
              'well as the filepath of the database to save the cleaned data '\
              'to as the third argument. \n\nExample: python process_data.py '\
              'disaster_messages.csv disaster_categories.csv '\
              'DisasterResponse.db')


if __name__ == '__main__':
    main()
