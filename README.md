# House Price Prediction Web Application

<p align="center">
  <img src="https://img.freepik.com/free-vector/hand-drawn-rising-house-prices-illustration_23-2150801646.jpg" alt="House Price Prediction Logo" width="560"/>
</p>

This web application predicts house prices based on various features using a machine learning model. It's built with Flask and uses a pre-trained model for quick predictions.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Setup](#setup)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Model Training](#model-training)

## Features

- 🏠 Predict house prices based on multiple features
- 🚀 Fast predictions using a pre-trained model
- 🌐 Web-based interface for easy access
- 📊 Minimalist and responsive design

## Technologies Used

- Python 3.8+
- Flask
- Scikit-learn
- Pandas
- Pickle
- HTML/CSS

## Demo

https://github.com/user-attachments/assets/a2a9bc84-f5cd-4229-99a3-e0c72b6d1b8d

## Setup

1. Clone the repository:
   ```
   git clone https://github.com/Krakken190/House_Price_Prediction.git
   cd House_Price_Prediction
   ```
2. Create and activate a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate 
   ```
3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```
4. Train the model (if `houseprice.pkl` doesn't exist):
   ```
   python train_model.py
   ```
5. Run the Flask application:
   ```
   python app.py
   ```
6. Open your web browser and go to `http://127.0.0.1:5000/`

## Usage

1. Fill in the house features in the web form.
2. Click the "Predict Price" button.
3. View the predicted house price on the result page.

## Project Structure

![structure for houseJPG](https://github.com/user-attachments/assets/bcf92056-c9da-4f12-8e9e-37a8eadcdb8d)


## Model Training

The machine learning model is trained using the `train_model.py` script. It uses a Linear Regression model with preprocessing steps for both numerical and categorical features. The trained model is saved as `houseprice.pkl`.

To retrain the model with new data:

1. Update the `Housing.csv` file with your dataset.
2. Run `python train_model.py`.
3. The new model will replace the existing `houseprice.pkl` file.

<p align="center">
  Made with 💫 by <a href="https://github.com/Krakken190">Prajwal Dongre</a>
</p>


   


   
   
