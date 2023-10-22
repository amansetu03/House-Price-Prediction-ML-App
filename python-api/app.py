from flask import Flask,request,jsonify
from api import predict_price

app = Flask(__name__)

@app.route('/')

def home():
    return "hello world"


@app.route('/predict',methods = ['POST'])
def predict():
    loc = request.form.get('loc')
    sqft = int(request.form.get('sqft'))
    bath = int(request.form.get('bath'))
    bhk = int(request.form.get('bhk'))

    price = predict_price(loc,sqft,bath,bhk)
    result = {"Price":str(price)}
    
    return jsonify(result)

if __name__ == "__main__":
    app.run(host='http://codeplace.pythonanywhere.com', port=2545,debug=True)