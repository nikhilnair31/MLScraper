import joblib
import time;
import pandas as pd
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
#To avoid getting dataconverstion warnings
import warnings
from sklearn.exceptions import DataConversionWarning
warnings.filterwarnings(action='ignore', category=DataConversionWarning)

def getdata():
    global df
    df = pd.read_csv('Training\DataSVMbig.csv').fillna(0)
    df = df.drop(['tag', 'text', 'atext'],axis=1)
    cleandata(df)

def cleandata(df):
    global X, Xx, X_train,X_test, y_train, y_test, Y
    Y = []
    for val in df['content']:
        if(val == 'NC'):
            Y.append(0)
        else:
            Y.append(1)
    X = StandardScaler().fit_transform(df.drop(['content'],axis=1))
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size = 0.10)

def trainModel():
    ker = 'rbf'
    class_weight = {0:1, 1:3}
    print("\n", class_weight, "\t", ker.upper(), "\n")
    svclassifier = SVC(kernel=ker, gamma='auto', class_weight = class_weight)
    svclassifier.fit(X_train, y_train)
    joblib.dump(svclassifier, "modelVersions\svm_%s.pkl" % time.time()) 
    return svclassifier

# Run while testing for performance metrics
def stats(svclassifier):
    y_pred = svclassifier.predict(X_test)
    print("\n", confusion_matrix(y_test,y_pred), "\n")
    print(classification_report(y_test,y_pred))

getdata()
stats(trainModel())