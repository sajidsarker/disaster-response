# Disaster Response Pipeline Project

**Author:** Sajid Al Sanai

**License:** MIT License

[Launch Web App](https://sajid-disaster-response.herokuapp.com/)

![screenshot](https://github.com/sajidsarker/disaster-response/blob/main/app.png)

## Table of Contents

1. [Motivation](https://github.com/sajidsarker/disaster-response#1-motivation)
2. [Files](https://github.com/sajidsarker/disaster-response#2-files)
3. [Instructions](https://github.com/sajidsarker/disaster-response#3-instructions)
4. [Documentation](https://github.com/sajidsarker/disaster-response#4-documentation)
5. [Model Evaluation](https://github.com/sajidsarker/disaster-response#5-model-evaluation)

## 1. Motivation

The motivation for this particular project is to construct a web-based application and API that is able to classify social media messages into critical disaster response-related categories. There are 36 predefined natural disasters and disaster response-related categories under which social media messages may be filed including earthquakes, floods, shelter, food, medical aid, search & rescue et cetera.

By classifying these messages, we can determine specific users, locations, and aid resources critically required for disaster relief efforts and forwarding the contents of these messages to the appropriate disaster relief agencies or governmental authorities for disaster response. The utilisation of machine learning and natural language processing ensures faster alert and detection through social media for disasters and identifying where, for whom, and what sort of relief response is essential and effective.

The web-based application and API uses an ETL pipeline that processes social media disaster related messages from **Figure Eight** and subsequently uses the cleaned dataset in a NLP pipeline for a multi-class classification model.

## 2. Files

The directory structure for this repository is detailed below:

```bash
/
├── Documentation/
│   ├── process_data.html
│   └── train_classifier.html
├── app/
│   ├── templates/
│   │   ├── go.html
│   │   └── master.html
│   └── run.py
├── data/
│   ├── process_data.py
│   ├── categories.csv
│   ├── messages.py
│   └── DisasterResponse.db
├── model/
│   ├── train_classifier.py
│   └── classifier.pkl
├── .gitignore
├── requirements.txt
├── LICENSE
└── README.md
```

## 3. Instructions
1. Ensure that you have initialised your local Python environment and installed all relevant Python packages required by this project.

    ```bash
    git clone https://github.com/sajidsarker/disaster-response.git
    cd disaster-response
    pip install virtualenv
    virtualenv env
    source env/bin/activate
    pip install -r requirements.txt
    ```

2. Run the following commands in the project's root directory to set up your database and model.

    - To run ETL pipeline that cleans data and stores in database
    
        ```bash
        python data/process_data.py data/messages.csv data/categories.csv data/DisasterResponse.db
        ```
        
    - To run ML pipeline that trains classifier and saves it in a pickle file
    
        ```bash
        python models/train_classifier.py data/DisasterResponse.db models/classifier.pkl
        ```

3. Run the following command in the `./app` directory to run your web app.

    ```bash
    python app/run.py
    ```

4. Navigate to `http://0.0.0.0:3001/` in your web browser.

## 4. Documentation

Navigate to `./Documentation` to find formatted documentation for the relevant Python scripts in this project.

## 5. Model Evaluation

The classification model was a *Multiple Output* classifier wrapper for individual *Ada Boost* classifiers trained on the message data using a NLP pipeline. Training occurred additionally through Grid Search Cross Validation over a set of pre-defined tuning parameters to derive the best final model parameters.

Prior to this trained model, a *Random Forest* classifier was used. This yielded model parameters totalling `1.0 GB` in file size. In contrast, *Ada Boost*, which is also an ensemble learning model, yielded similar results with model parameters totalling `2.0 MB` in file size.

Model diagnostics are listed below.

```
Model Accuracy: 94.846%
```

```
Target Variable 0: related
Class Labels: [0 1]
              precision    recall  f1-score   support

           0       0.68      0.26      0.37      1253
           1       0.80      0.96      0.88      3983

    accuracy                           0.79      5236
   macro avg       0.74      0.61      0.62      5236
weighted avg       0.77      0.79      0.76      5236
```

```
Target Variable 1: request
Class Labels: [0 1]
              precision    recall  f1-score   support

           0       0.91      0.96      0.94      4358
           1       0.73      0.53      0.62       878

    accuracy                           0.89      5236
   macro avg       0.82      0.75      0.78      5236
weighted avg       0.88      0.89      0.88      5236
```

```
Target Variable 2: offer
Class Labels: [0 1]
              precision    recall  f1-score   support

           0       1.00      1.00      1.00      5222
           1       0.00      0.00      0.00        14

    accuracy                           1.00      5236
   macro avg       0.50      0.50      0.50      5236
weighted avg       0.99      1.00      0.99      5236
```

```
Target Variable 3: aid_related
Class Labels: [0 1]
              precision    recall  f1-score   support

           0       0.77      0.86      0.81      3104
           1       0.75      0.62      0.68      2132

    accuracy                           0.76      5236
   macro avg       0.76      0.74      0.75      5236
weighted avg       0.76      0.76      0.76      5236
```

```
Target Variable 4: medical_help
Class Labels: [0 1]
              precision    recall  f1-score   support

           0       0.93      0.98      0.96      4788
           1       0.58      0.26      0.36       448

    accuracy                           0.92      5236
   macro avg       0.76      0.62      0.66      5236
weighted avg       0.90      0.92      0.91      5236
```

```
Target Variable 5: medical_products
Class Labels: [0 1]
              precision    recall  f1-score   support

           0       0.96      0.99      0.98      4956
           1       0.67      0.33      0.44       280

    accuracy                           0.96      5236
   macro avg       0.82      0.66      0.71      5236
weighted avg       0.95      0.96      0.95      5236
```

```
Target Variable 6: search_and_rescue
Class Labels: [0 1]
              precision    recall  f1-score   support

           0       0.98      1.00      0.99      5099
           1       0.54      0.15      0.24       137

    accuracy                           0.97      5236
   macro avg       0.76      0.57      0.61      5236
weighted avg       0.97      0.97      0.97      5236
```

```
Target Variable 7: security
Class Labels: [0 1]
              precision    recall  f1-score   support

           0       0.98      1.00      0.99      5151
           1       0.36      0.06      0.10        85

    accuracy                           0.98      5236
   macro avg       0.67      0.53      0.55      5236
weighted avg       0.97      0.98      0.98      5236
```

```
Target Variable 8: military
Class Labels: [0 1]
              precision    recall  f1-score   support

           0       0.98      0.99      0.99      5071
           1       0.58      0.39      0.47       165

    accuracy                           0.97      5236
   macro avg       0.78      0.69      0.73      5236
weighted avg       0.97      0.97      0.97      5236
```

```
Target Variable 9: child_alone
Class Labels: [0]
              precision    recall  f1-score   support

           0       1.00      1.00      1.00      5236

    accuracy                           1.00      5236
   macro avg       1.00      1.00      1.00      5236
weighted avg       1.00      1.00      1.00      5236
```

```
Target Variable 10: water
Class Labels: [0 1]
              precision    recall  f1-score   support

           0       0.97      0.98      0.98      4896
           1       0.74      0.62      0.68       340

    accuracy                           0.96      5236
   macro avg       0.86      0.80      0.83      5236
weighted avg       0.96      0.96      0.96      5236
```

```
Target Variable 11: food
Class Labels: [0 1]
              precision    recall  f1-score   support

           0       0.96      0.98      0.97      4655
           1       0.81      0.69      0.75       581

    accuracy                           0.95      5236
   macro avg       0.89      0.83      0.86      5236
weighted avg       0.95      0.95      0.95      5236
```

```
Target Variable 12: shelter
Class Labels: [0 1]
              precision    recall  f1-score   support

           0       0.96      0.98      0.97      4771
           1       0.77      0.53      0.63       465

    accuracy                           0.94      5236
   macro avg       0.86      0.76      0.80      5236
weighted avg       0.94      0.94      0.94      5236
```

```
Target Variable 13: clothing
Class Labels: [0 1]
              precision    recall  f1-score   support

           0       0.99      1.00      0.99      5157
           1       0.76      0.47      0.58        79

    accuracy                           0.99      5236
   macro avg       0.87      0.73      0.79      5236
weighted avg       0.99      0.99      0.99      5236
```

```
Target Variable 14: money
Class Labels: [0 1]
              precision    recall  f1-score   support

           0       0.98      1.00      0.99      5118
           1       0.59      0.31      0.40       118

    accuracy                           0.98      5236
   macro avg       0.79      0.65      0.70      5236
weighted avg       0.98      0.98      0.98      5236
```

```
Target Variable 15: missing_people
Class Labels: [0 1]
              precision    recall  f1-score   support

           0       0.99      1.00      0.99      5173
           1       0.18      0.03      0.05        63

    accuracy                           0.99      5236
   macro avg       0.59      0.52      0.52      5236
weighted avg       0.98      0.99      0.98      5236
```

```
Target Variable 16: refugees
Class Labels: [0 1]
              precision    recall  f1-score   support

           0       0.97      0.99      0.98      5046
           1       0.62      0.25      0.35       190

    accuracy                           0.97      5236
   macro avg       0.80      0.62      0.67      5236
weighted avg       0.96      0.97      0.96      5236
```

```
Target Variable 17: death
Class Labels: [0 1]
              precision    recall  f1-score   support

           0       0.97      0.99      0.98      4997
           1       0.71      0.44      0.55       239

    accuracy                           0.97      5236
   macro avg       0.84      0.72      0.76      5236
weighted avg       0.96      0.97      0.96      5236
```

```
Target Variable 18: other_aid
Class Labels: [0 1]
              precision    recall  f1-score   support

           0       0.89      0.98      0.93      4576
           1       0.51      0.15      0.23       660

    accuracy                           0.87      5236
   macro avg       0.70      0.56      0.58      5236
weighted avg       0.84      0.87      0.84      5236
```

```
Target Variable 19: infrastructure_related
Class Labels: [0 1]
              precision    recall  f1-score   support

           0       0.95      0.99      0.97      4927
           1       0.39      0.12      0.19       309

    accuracy                           0.94      5236
   macro avg       0.67      0.56      0.58      5236
weighted avg       0.91      0.94      0.92      5236
```

```
Target Variable 20: transport
Class Labels: [0 1]
              precision    recall  f1-score   support

           0       0.96      1.00      0.98      5001
           1       0.71      0.22      0.33       235

    accuracy                           0.96      5236
   macro avg       0.84      0.61      0.66      5236
weighted avg       0.95      0.96      0.95      5236
```

```
Target Variable 21: buildings
Class Labels: [0 1]
              precision    recall  f1-score   support

           0       0.97      0.99      0.98      4974
           1       0.68      0.39      0.50       262

    accuracy                           0.96      5236
   macro avg       0.82      0.69      0.74      5236
weighted avg       0.95      0.96      0.96      5236
```

```
Target Variable 22: electricity
Class Labels: [0 1]
              precision    recall  f1-score   support

           0       0.99      1.00      0.99      5136
           1       0.54      0.25      0.34       100

    accuracy                           0.98      5236
   macro avg       0.76      0.62      0.67      5236
weighted avg       0.98      0.98      0.98      5236
```

```
Target Variable 23: tools
Class Labels: [0 1]
              precision    recall  f1-score   support

           0       0.99      1.00      1.00      5205
           1       0.33      0.03      0.06        31

    accuracy                           0.99      5236
   macro avg       0.66      0.52      0.53      5236
weighted avg       0.99      0.99      0.99      5236
```

```
Target Variable 24: hospitals
Class Labels: [0 1]
              precision    recall  f1-score   support

           0       0.99      1.00      0.99      5177
           1       0.23      0.10      0.14        59

    accuracy                           0.99      5236
   macro avg       0.61      0.55      0.57      5236
weighted avg       0.98      0.99      0.98      5236
```

```
Target Variable 25: shops
Class Labels: [0 1]
              precision    recall  f1-score   support

           0       1.00      1.00      1.00      5221
           1       0.40      0.13      0.20        15

    accuracy                           1.00      5236
   macro avg       0.70      0.57      0.60      5236
weighted avg       1.00      1.00      1.00      5236
```

```
Target Variable 26: aid_centers
Class Labels: [0 1]
              precision    recall  f1-score   support

           0       0.99      1.00      0.99      5187
           1       0.35      0.16      0.22        49

    accuracy                           0.99      5236
   macro avg       0.67      0.58      0.61      5236
weighted avg       0.99      0.99      0.99      5236
```

```
Target Variable 27: other_infrastructure
Class Labels: [0 1]
              precision    recall  f1-score   support

           0       0.96      0.99      0.98      5019
           1       0.31      0.09      0.14       217

    accuracy                           0.95      5236
   macro avg       0.64      0.54      0.56      5236
weighted avg       0.93      0.95      0.94      5236
```

```
Target Variable 28: weather_related
Class Labels: [0 1]
              precision    recall  f1-score   support

           0       0.89      0.95      0.92      3799
           1       0.85      0.70      0.77      1437

    accuracy                           0.88      5236
   macro avg       0.87      0.83      0.85      5236
weighted avg       0.88      0.88      0.88      5236
```

```
Target Variable 29: floods
Class Labels: [0 1]
              precision    recall  f1-score   support

           0       0.96      0.99      0.98      4814
           1       0.84      0.55      0.66       422

    accuracy                           0.96      5236
   macro avg       0.90      0.77      0.82      5236
weighted avg       0.95      0.96      0.95      5236
```

```
Target Variable 30: storm
Class Labels: [0 1]
              precision    recall  f1-score   support

           0       0.95      0.98      0.97      4750
           1       0.75      0.52      0.61       486

    accuracy                           0.94      5236
   macro avg       0.85      0.75      0.79      5236
weighted avg       0.93      0.94      0.93      5236
```

```
Target Variable 31: fire
Class Labels: [0 1]
              precision    recall  f1-score   support

           0       0.99      1.00      1.00      5183
           1       0.67      0.26      0.38        53

    accuracy                           0.99      5236
   macro avg       0.83      0.63      0.69      5236
weighted avg       0.99      0.99      0.99      5236
```

```
Target Variable 32: earthquake
Class Labels: [0 1]
              precision    recall  f1-score   support

           0       0.98      0.99      0.98      4749
           1       0.89      0.78      0.83       487

    accuracy                           0.97      5236
   macro avg       0.93      0.88      0.91      5236
weighted avg       0.97      0.97      0.97      5236
```

```
Target Variable 33: cold
Class Labels: [0 1]
              precision    recall  f1-score   support

           0       0.99      1.00      0.99      5140
           1       0.53      0.24      0.33        96

    accuracy                           0.98      5236
   macro avg       0.76      0.62      0.66      5236
weighted avg       0.98      0.98      0.98      5236
```

```
Target Variable 34: other_weather
Class Labels: [0 1]
              precision    recall  f1-score   support

           0       0.95      0.99      0.97      4951
           1       0.54      0.18      0.27       285

    accuracy                           0.95      5236
   macro avg       0.75      0.59      0.62      5236
weighted avg       0.93      0.95      0.93      5236
```

```
Target Variable 35: direct_report
Class Labels: [0 1]
              precision    recall  f1-score   support

           0       0.87      0.96      0.91      4246
           1       0.68      0.41      0.51       990

    accuracy                           0.85      5236
   macro avg       0.78      0.68      0.71      5236
weighted avg       0.84      0.85      0.84      5236
```
