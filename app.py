from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "Index!"

@app.route('/', methods=['GET'])
def index():
  a = 5
  func()
  return render_template('age.html')

@app.route("/members/<string:name>/")
def getMember(name):
    return name

if __name__ == "__main__":
    app.run()

#Creating a virtual environment for Flask
#python3 -m venv venv
#source venv/bin/activate
