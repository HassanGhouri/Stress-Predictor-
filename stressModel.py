# Importing the libraries
import pandas as pd
import mysql.connector
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.tree import DecisionTreeRegressor


def modelMaker():
    """
    Make and train regression tree model
    :return:  model, Categorical, variable encoder.
    """

    # Connect to SQL database
    db = mysql.connector.connect(user="root", password="Check ReadME", database="StressPerdict")
    cursor = db.cursor()
    query = "SELECT * FROM stressdataset"
    cursor.execute(query)

    # Fetch the data from the cursor
    data = cursor.fetchall()
    df = pd.DataFrame(data)

    cursor.close()
    db.close()

    # Create a Pandas DataFrame from the fetched data
    X = df.iloc[:, 1:-1].values
    y = df.iloc[:, -1].values

    cursor.close()
    db.close()

    # Convert the Blood pressure from string fraction form to float
    for row in X:

        if "/" in row[6]:
            bp = row[6]
            if "/" in bp:
                num, denom = map(int, bp.split("/"))
                row[6] = num / denom
            else:
                row[6] = float(bp) if bp else None  # Handle empty values

    # Encoding Categorical variables (Gender, BMI category, Sleep Disorder)
    ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [0, 5, 9])], remainder="passthrough")
    X = ct.fit_transform(X)

    # Split the dataset into the Training set and Test set
    x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Training the Decision Tree Regression model on the dataset
    regressor = DecisionTreeRegressor()
    regressor.fit(x_train, y_train)

    return regressor, ct


def prepData(X, ct):
    """
    Preps input for model, returns transformed input
    :param X: Input
    :param ct: categorical encoder
    :return: X (prepared input)
    """
    # Convert the Blood pressure from string fraction form to float
    for row in X:
        if "/" in row[6]:
            bp = row[6]
            if "/" in bp:
                num, denom = map(int, bp.split("/"))
                row[6] = num / denom
            else:
                row[6] = float(bp) if bp else None  # Handle empty values

    # Encoding Categorical variables (Gender, BMI category, Sleep Disorder)
    X = ct.transform(X)

    return X
