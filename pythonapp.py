
from flask import Flask
app=Flask(__name__)



@app.route("/add")
def hello():
    num1=request.args.get('num1',type=int)
    num2=request.args.get('num2',type=int)

    return f"Addition of 2 numbers {num1} + {num2}"

@app.route("/home")
def home():
    return "<h1>Hello</h1>"

@app.route("/sub")
def  sub():
    num1=request.args.get('num1',type=int)
    num2=request.args.get('num2',type=int)
    return f"Addition of 2 numbers {num1} * {num2}"

@app.route("/div")
def  sub():
    num1=request.args.get('num1',type=int)
    num2=request.args.get('num2',type=int)
    return f"Addition of 2 numbers {num1} / {num2}"

@app.route("/mul")
def  sub():
    num1=request.args.get('num1',type=int)
    num2=request.args.get('num2',type=int)
    return f"Addition of 2 numbers {num1} - {num2}"

if __name__=='__main__':
    app.run(debug=True)