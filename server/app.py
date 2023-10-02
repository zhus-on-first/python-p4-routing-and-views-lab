#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"

@app.route("/print/<string_param>")
def print_string(string_param):
    print(string_param)
    return f"{string_param}"

# Build a string to return as an HTTP response. 
# HTTP responses are text-based, so all data within must be string data. 
# Convert the integers to strings when adding to response.
@app.route("/count/<int:num>")
def count(num):
    result_list = ""
    for i in range(num):
        result_list += str(i) + "\n"
    return result_list

    # result_list = [str(i) for i in range(num + 1)]
    # result = "\n".join(result_list)

@app.route("/math/<int:num1>/<operation>/<int:num2>")
def math(num1, operation, num2):
    result = None
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "div":
        if num2 != 0:
            result = num1 / num2
        else:
            return "Can't divide by zero"
    elif operation == "%":
        result = num1 % num2
    else:
        return "Invalid operation."
    
    return str(result)
    
        
    

if __name__ == "__main__":
    app.run(port=5555, debug=True)
