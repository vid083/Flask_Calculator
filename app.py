#importing flask
from flask import Flask, render_template, request, jsonify

#intialize or creating flask object
app = Flask(__name__)

#creating route
@app.route('/')
def home_page():
    return 'hello'

@app.route('/via_postman', methods=['POST'])
def calculator():
    if(request.method == 'POST'):
        data_postman = request.get_json()
        operation = data_postman['operation']
        num1 = int(data_postman['num1'])
        num2 = int(data_postman['num2'])
        try:
            if(operation == 'add'):
                r=num1+num2
                result = str(r)
            elif(operation == 'substract'):
                r=num1-num2
                result = str(r)
            elif(operation == 'multiply'):
                r=num1*num2
                result = str(r)
            elif(operation == 'divide'):
                r=num1/num2
                result = str(r)
            else:
                result = "enter add or substract or multiply or divide"
        except Exception as e: 
            print(e)
            result = e
        finally:
            return jsonify(result)

#run flask app
if __name__ == '__main__':
    app.run()