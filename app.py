from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)

# Loading the trained model
with open('houseprice.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get form data
        input_data = {
            'area': float(request.form['area']),
            'bedrooms': int(request.form['bedrooms']),
            'bathrooms': int(request.form['bathrooms']),
            'stories': int(request.form['stories']),
            'mainroad': request.form['mainroad'],
            'guestroom': request.form['guestroom'],
            'basement': request.form['basement'],
            'hotwaterheating': request.form['hotwaterheating'],
            'airconditioning': request.form['airconditioning'],
            'parking': int(request.form['parking']),
            'prefarea': request.form['prefarea'],
            'furnishingstatus': request.form['furnishingstatus']
        }
        
        # Converting input_data to a DataFrame
        input_df = pd.DataFrame([input_data])
        
        # Making prediction
        predicted_price = model.predict(input_df)[0]
        
        return render_template('result.html', price=predicted_price)
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)