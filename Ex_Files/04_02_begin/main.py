from flask import Flask

app = Flask(__name__) #name with dunderscore 


#define a route
@app.route("/")
def hello():
  return "Hello, World!"

app.run(debug=True)