from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'Hey, wlcome to my project.'

@app.route('/health)
def health():
  return 'Server is up and running.'
