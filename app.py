from flask import Flask
import socket
from mangum import Mangum

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World! loola pai gia I\'m host %s' % socket.gethostname()

handler = Mangum(app)  # Lambda entry point
