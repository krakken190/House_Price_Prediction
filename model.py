import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
import pickle

def prepare_data():
    try:
        # load the data
        data = pd.read_csv('Housing.csv')
    except FileNotFoundError:
        print("Warning: house_data.csv not found. Using dummy data.")
        data = pd.DataFrame({
            'price': np.random.randint(1000000, 20000000, 1000),
            'area': np.random.randint(1000, 10000, 1000),
            'bedrooms': np.random.randint(1, 6, 1000),
            'bathrooms': np.random.randint(1, 5, 1000),
            'stories': np.random.randint(1, 5, 1000),
            'mainroad': np.random.choice(['yes', 'no'], 1000),
            'guestroom': np.random.choice(['yes', 'no'], 1000),
            'basement': np.random.choice(['yes', 'no'], 1000),
            'hotwaterheating': np.random.choice(['yes', 'no'], 1000),
            'airconditioning': np.random.choice(['yes', 'no'], 1000),
            'parking': np.random.randint(0, 4, 1000),
            'prefarea': np.random.choice(['yes', 'no'], 1000),
            'furnishingstatus': np.random.choice(['furnished', 'semi-furnished', 'unfurnished'], 1000)
        })
    
    # Separating features and target
    X = data.drop('price', axis=1)
    y = data['price']
    
    return X, y

def create_model():
    # Defining categorical and numerical columns
    categorical_features = ['mainroad', 'guestroom', 'basement', 'hotwaterheating', 'airconditioning', 'prefarea', 'furnishingstatus']
    numerical_features = ['area', 'bedrooms', 'bathrooms', 'stories', 'parking']
    
    # Creating preprocessing steps
    categorical_transformer = Pipeline(steps=[
        ('onehot', OneHotEncoder(drop='first', sparse_output=False))
    ])
    
    numerical_transformer = Pipeline(steps=[
        ('scaler', StandardScaler())
    ])
    
    # Creating the preprocessor
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', numerical_transformer, numerical_features),
            ('cat', categorical_transformer, categorical_features)
        ])
    
    # Creating the model pipeline
    model = Pipeline([
        ('preprocessor', preprocessor),
        ('regressor', LinearRegression())
    ])
    
    return model

def train_and_save_model():
    X, y = prepare_data()
    model = create_model()
    model.fit(X, y)
    
    # Saving the model
    with open('houseprice.pkl', 'wb') as f:
        pickle.dump(model, f)
    
    print("Model trained and saved as 'houseprice.pkl'")

if __name__ == "__main__":
    train_and_save_model()