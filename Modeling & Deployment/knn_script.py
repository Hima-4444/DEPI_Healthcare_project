import joblib
import mlflow
import mlflow.sklearn
import pandas as pd
import numpy as np
import math
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import scipy.stats as stats
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier,VotingClassifier
from xgboost import XGBClassifier
from lightgbm import LGBMClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import AdaBoostClassifier
from sklearn.linear_model import SGDClassifier
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.decomposition import PCA
import xgboost as xgb
import lightgbm as lgb
from tqdm import tqdm
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

import warnings
warnings.filterwarnings('ignore')

df_filtered = pd.read_csv('oral_cancer_filtered.csv')
# df = pd.read_csv('oral_cancer_Selected.csv')

x = df_filtered.drop('Oral Cancer (Diagnosis)', axis=1)  
y =df_filtered['Oral Cancer (Diagnosis)'] 

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42, stratify=y)

scaler=StandardScaler()
X_train_scaled=scaler.fit_transform(X_train)
X_test_scaled=scaler.transform(X_test)

mlflow.set_experiment('Oral Cancer Deployment')
with mlflow.start_run():
    model = KNeighborsClassifier(n_neighbors=5)
    
    model.fit(X_train_scaled, y_train) 
    y_pred = model.predict(X_test_scaled)
    
    f1 = f1_score(y_test, y_pred)
    accuracy = accuracy_score(y_test, y_pred)
    
    print(f"F1 Score: {f1}")
    print(f"Accuracy: {accuracy}")

    mlflow.log_param('n_neighbors', 5)
    mlflow.log_param('random_state', 42)
    mlflow.log_param('test_size', 0.2)

    mlflow.log_metric('accuracy', accuracy)
    mlflow.log_metric('f1_score', f1)

    mlflow.sklearn.log_model(model, "model")
    print("Model saved to MLflow.")
