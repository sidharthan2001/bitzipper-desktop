# build bd008e3bc9
# (auto) 547815
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return 'ok'
