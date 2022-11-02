# Disaster Response Pipeline Project

**Author:** Sajid Al Sanai

**License:** MIT License

![screenshot](https://github.com/sajidsarker/disaster-response/app.png)

## Table of Contents

1. [Motivation](https://github.com/sajidsarker/disaster-response#1-motivation)
2. [Files](https://github.com/sajidsarker/disaster-response#2-files)
3. [Instructions](https://github.com/sajidsarker/disaster-response#3-instructions)
4. [Documentation](https://github.com/sajidsarker/disaster-response#4-documentation)
5. [Model Evaluation](https://github.com/sajidsarker/disaster-response#5-model-evaluation)

## 1. Motivation

[...]

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
│   ├── process_data.py
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
Model Accuracy: 94.943%
```

```
Target Variable 0: related
Class Labels: [0 1 2]
              precision    recall  f1-score   support

           0       0.64      0.10      0.17      1193
           1       0.78      0.98      0.87      4003
           2       0.82      0.23      0.35        40

    accuracy                           0.78      5236
   macro avg       0.75      0.44      0.46      5236
weighted avg       0.75      0.78      0.71      5236
```

```
Target Variable 1: request
Class Labels: [0 1]
              precision    recall  f1-score   support

           0       0.92      0.96      0.94      4403
           1       0.71      0.54      0.62       833

    accuracy                           0.89      5236
   macro avg       0.81      0.75      0.78      5236
weighted avg       0.88      0.89      0.89      5236
```

```
Target Variable 2: offer
Class Labels: [0 1]
              precision    recall  f1-score   support

           0       1.00      1.00      1.00      5212
           1       0.10      0.04      0.06        24

    accuracy                           0.99      5236
   macro avg       0.55      0.52      0.53      5236
weighted avg       0.99      0.99      0.99      5236
```

```
Target Variable 3: aid_related
Class Labels: [0 1]
              precision    recall  f1-score   support

           0       0.77      0.86      0.81      3139
           1       0.75      0.61      0.67      2097

    accuracy                           0.76      5236
   macro avg       0.76      0.74      0.74      5236
weighted avg       0.76      0.76      0.76      5236
```

```
Target Variable 4: medical_help
Class Labels: [0 1]
              precision    recall  f1-score   support

           0       0.95      0.98      0.96      4854
           1       0.58      0.32      0.41       382

    accuracy                           0.93      5236
   macro avg       0.76      0.65      0.69      5236
weighted avg       0.92      0.93      0.92      5236
```

```
Target Variable 5: medical_products
Class Labels: [0 1]
              precision    recall  f1-score   support

           0       0.97      0.99      0.98      4973
           1       0.65      0.38      0.48       263

    accuracy                           0.96      5236
   macro avg       0.81      0.69      0.73      5236
weighted avg       0.95      0.96      0.95      5236
```

```
Target Variable 6: search_and_rescue
Class Labels: [0 1]
              precision    recall  f1-score   support

           0       0.98      1.00      0.99      5118
           1       0.62      0.21      0.32       118

    accuracy                           0.98      5236
   macro avg       0.80      0.60      0.65      5236
weighted avg       0.97      0.98      0.97      5236
```

```
Target Variable 7: security
Class Labels: [0 1]
              precision    recall  f1-score   support

           0       0.98      1.00      0.99      5150
           1       0.40      0.07      0.12        86

    accuracy                           0.98      5236
   macro avg       0.69      0.53      0.56      5236
weighted avg       0.98      0.98      0.98      5236
```

```
Target Variable 8: military
Class Labels: [0 1]
              precision    recall  f1-score   support

           0       0.98      0.99      0.99      5071
           1       0.59      0.40      0.48       165

    accuracy                           0.97      5236
   macro avg       0.78      0.70      0.73      5236
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

           0       0.98      0.98      0.98      4903
           1       0.74      0.72      0.73       333

    accuracy                           0.97      5236
   macro avg       0.86      0.85      0.86      5236
weighted avg       0.97      0.97      0.97      5236
```

```
Target Variable 11: food
Class Labels: [0 1]
              precision    recall  f1-score   support

           0       0.96      0.98      0.97      4666
           1       0.79      0.68      0.74       570

    accuracy                           0.95      5236
   macro avg       0.88      0.83      0.85      5236
weighted avg       0.94      0.95      0.94      5236
```

```
Target Variable 12: shelter
Class Labels: [0 1]
              precision    recall  f1-score   support

           0       0.96      0.98      0.97      4801
           1       0.75      0.58      0.66       435

    accuracy                           0.95      5236
   macro avg       0.86      0.78      0.81      5236
weighted avg       0.95      0.95      0.95      5236
```

```
Target Variable 13: clothing
Class Labels: [0 1]
              precision    recall  f1-score   support

           0       0.99      1.00      0.99      5160
           1       0.57      0.38      0.46        76

    accuracy                           0.99      5236
   macro avg       0.78      0.69      0.73      5236
weighted avg       0.98      0.99      0.99      5236
```

```
Target Variable 14: money
Class Labels: [0 1]
              precision    recall  f1-score   support

           0       0.98      0.99      0.99      5104
           1       0.53      0.30      0.38       132

    accuracy                           0.98      5236
   macro avg       0.76      0.64      0.68      5236
weighted avg       0.97      0.98      0.97      5236
```

```
Target Variable 15: missing_people
Class Labels: [0 1]
              precision    recall  f1-score   support

           0       0.99      1.00      1.00      5189
           1       0.62      0.11      0.18        47

    accuracy                           0.99      5236
   macro avg       0.81      0.55      0.59      5236
weighted avg       0.99      0.99      0.99      5236
```

```
Target Variable 16: refugees
Class Labels: [0 1]
              precision    recall  f1-score   support

           0       0.98      0.99      0.98      5071
           1       0.56      0.27      0.37       165

    accuracy                           0.97      5236
   macro avg       0.77      0.63      0.68      5236
weighted avg       0.96      0.97      0.97      5236
```

```
Target Variable 17: death
Class Labels: [0 1]
              precision    recall  f1-score   support

           0       0.98      0.99      0.99      5000
           1       0.75      0.53      0.63       236

    accuracy                           0.97      5236
   macro avg       0.87      0.76      0.81      5236
weighted avg       0.97      0.97      0.97      5236
```

```
Target Variable 18: other_aid
Class Labels: [0 1]
              precision    recall  f1-score   support

           0       0.90      0.98      0.93      4604
           1       0.50      0.18      0.26       632

    accuracy                           0.88      5236
   macro avg       0.70      0.58      0.60      5236
weighted avg       0.85      0.88      0.85      5236
```

```
Target Variable 19: infrastructure_related
Class Labels: [0 1]
              precision    recall  f1-score   support

           0       0.95      0.99      0.97      4918
           1       0.38      0.11      0.17       318

    accuracy                           0.93      5236
   macro avg       0.66      0.55      0.57      5236
weighted avg       0.91      0.93      0.92      5236
```

```
Target Variable 20: transport
Class Labels: [0 1]
              precision    recall  f1-score   support

           0       0.97      0.99      0.98      5031
           1       0.59      0.23      0.33       205

    accuracy                           0.96      5236
   macro avg       0.78      0.61      0.66      5236
weighted avg       0.95      0.96      0.96      5236
```

```
Target Variable 21: buildings
Class Labels: [0 1]
              precision    recall  f1-score   support

           0       0.97      0.99      0.98      4960
           1       0.65      0.41      0.51       276

    accuracy                           0.96      5236
   macro avg       0.81      0.70      0.74      5236
weighted avg       0.95      0.96      0.95      5236
```

```
Target Variable 22: electricity
Class Labels: [0 1]
              precision    recall  f1-score   support

           0       0.99      1.00      0.99      5128
           1       0.57      0.30      0.39       108

    accuracy                           0.98      5236
   macro avg       0.78      0.65      0.69      5236
weighted avg       0.98      0.98      0.98      5236
```

```
Target Variable 23: tools
Class Labels: [0 1]
              precision    recall  f1-score   support

           0       0.99      1.00      1.00      5205
           1       0.00      0.00      0.00        31

    accuracy                           0.99      5236
   macro avg       0.50      0.50      0.50      5236
weighted avg       0.99      0.99      0.99      5236
```

```
Target Variable 24: hospitals
Class Labels: [0 1]
              precision    recall  f1-score   support

           0       0.99      1.00      0.99      5180
           1       0.40      0.14      0.21        56

    accuracy                           0.99      5236
   macro avg       0.70      0.57      0.60      5236
weighted avg       0.98      0.99      0.99      5236
```

```
Target Variable 25: shops
Class Labels: [0 1]
              precision    recall  f1-score   support

           0       1.00      1.00      1.00      5214
           1       0.00      0.00      0.00        22

    accuracy                           1.00      5236
   macro avg       0.50      0.50      0.50      5236
weighted avg       0.99      1.00      0.99      5236
```

```
Target Variable 26: aid_centers
Class Labels: [0 1]
              precision    recall  f1-score   support

           0       0.99      1.00      0.99      5185
           1       0.14      0.08      0.10        51

    accuracy                           0.99      5236
   macro avg       0.57      0.54      0.55      5236
weighted avg       0.98      0.99      0.98      5236
```

```
Target Variable 27: other_infrastructure
Class Labels: [0 1]
              precision    recall  f1-score   support

           0       0.96      0.99      0.98      5019
           1       0.27      0.10      0.14       217

    accuracy                           0.95      5236
   macro avg       0.62      0.54      0.56      5236
weighted avg       0.93      0.95      0.94      5236
```

```
Target Variable 28: weather_related
Class Labels: [0 1]
              precision    recall  f1-score   support

           0       0.89      0.95      0.92      3823
           1       0.85      0.69      0.76      1413

    accuracy                           0.88      5236
   macro avg       0.87      0.82      0.84      5236
weighted avg       0.88      0.88      0.88      5236
```

```
Target Variable 29: floods
Class Labels: [0 1]
              precision    recall  f1-score   support

           0       0.97      0.99      0.98      4835
           1       0.85      0.59      0.70       401

    accuracy                           0.96      5236
   macro avg       0.91      0.79      0.84      5236
weighted avg       0.96      0.96      0.96      5236
```

```
Target Variable 30: storm
Class Labels: [0 1]
              precision    recall  f1-score   support

           0       0.95      0.98      0.97      4757
           1       0.76      0.52      0.61       479

    accuracy                           0.94      5236
   macro avg       0.86      0.75      0.79      5236
weighted avg       0.94      0.94      0.94      5236
```

```
Target Variable 31: fire
Class Labels: [0 1]
              precision    recall  f1-score   support

           0       0.99      1.00      1.00      5187
           1       0.68      0.27      0.38        49

    accuracy                           0.99      5236
   macro avg       0.84      0.63      0.69      5236
weighted avg       0.99      0.99      0.99      5236
```

```
Target Variable 32: earthquake
Class Labels: [0 1]
              precision    recall  f1-score   support

           0       0.98      0.99      0.98      4757
           1       0.87      0.81      0.84       479

    accuracy                           0.97      5236
   macro avg       0.93      0.90      0.91      5236
weighted avg       0.97      0.97      0.97      5236
```

```
Target Variable 33: cold
Class Labels: [0 1]
              precision    recall  f1-score   support

           0       0.99      0.99      0.99      5149
           1       0.53      0.38      0.44        87

    accuracy                           0.98      5236
   macro avg       0.76      0.69      0.72      5236
weighted avg       0.98      0.98      0.98      5236
```

```
Target Variable 34: other_weather
Class Labels: [0 1]
              precision    recall  f1-score   support

           0       0.95      0.99      0.97      4954
           1       0.47      0.15      0.23       282

    accuracy                           0.95      5236
   macro avg       0.71      0.57      0.60      5236
weighted avg       0.93      0.95      0.93      5236

```

```
Target Variable 35: direct_report
Class Labels: [0 1]
              precision    recall  f1-score   support

           0       0.88      0.96      0.92      4260
           1       0.70      0.44      0.54       976

    accuracy                           0.86      5236
   macro avg       0.79      0.70      0.73      5236
weighted avg       0.85      0.86      0.85      5236
```
