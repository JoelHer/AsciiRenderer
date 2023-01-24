from flask import Flask, request, jsonify
from threading import Thread
import random
app = Flask(__name__)

@app.route('/')
def home():
  return 'Alive!'
def run():
  app.run(host='0.0.0.0',port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()