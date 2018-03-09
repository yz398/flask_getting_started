from flask import Flask, jsonify, request 
app = Flask(__name__)

@app.route("/", methods=["GET"])
def hello():
  """
  Returns the string "Hello, world" to the caller
  """
  return "Hello, world"
  
@app.route("/name", methods=["GET"])
def getData():
  """
  Returns the data dictionary below to the caller as JSON
  """
  data = {
    "name": "Yi Zhao"
  }
  return jsonify(data)

@app.route("/hello/<name>", methods=["GET"])
def changename(name):
  """
  Returns the data dictionary below to the caller as JSON
  """
  data1 = {
    "message": "Hello there, {0}".format(name)
  }
  return jsonify(data1)

@app.route("/sum", methods=["POST"])
def sum():
  r = request.get_json() # parses the POST request body as JSON
  s = r["a"] +r["b"] # adds JSON dict parameter "a" and "b" together
  return str(s), 200

@app.route("/distance", methods=["POST"])
def distance():
  """
  Returns the distance between two points
  """
  r = request.get_json() # parses the POST request body as JSON
  x1 = r["a"]  # adds JSON dict parameter "a" and "b" together
  x2 = r["b"]
  b = (x1[1]-x2[1])*(x1[1]-x2[1])
  a = (x1[0]-x2[0])*(x1[0]-x2[0])
  d = (a+b)**0.5
  answer ={
    "distance": d,
    "a":x1,
    "b":x2  
  }
#  d = sqrt(square(x1[0]-x2[0])+square(x1[1]-x2[1]))
#  return str(d), 200
  return jsonify(answer)
