# Disaster Response Pipeline Project

**Author:** Sajid Al Sanai

**License:** MIT License

## Table of Contents

## Instructions:
1. Ensure that you have initialised your local Python environment and installed all relevant Python packages required by this project.

    ```bash
    git clone https://github.com/sajidsarker/disaster-response.git
    cd disaster-response.git
    pip install virtualenv
    virtualenv env
    source env/bin/activate
    pip install -r requirements.txt
    ```

2. Run the following commands in the project's root directory to set up your database and model.

    - To run ETL pipeline that cleans data and stores in database
        `python data/process_data.py data/messages.csv data/categories.csv data/DisasterResponse.db`
    - To run ML pipeline that trains classifier and saves
        `python models/train_classifier.py data/DisasterResponse.db models/classifier.pkl`

3. Run the following command in the **/app** directory to run your web app.
    `python run.py`

4. Navigate to http://0.0.0.0:3001/ in your web browser

## 4. Files

The directory structure for this repository is detailed below:

```bash
/
├── Documentation/
│   └── Documentation.html
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
