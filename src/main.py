from flask import Flask
from module.decorator import validate_token
import socket
app = Flask(__name__)

@app.route('/')
def health():
    return 'status, healthy! v.0.0.1', 200

@app.route('/hello')
@validate_token('Data.Reader')
def hello_world():
    return 'Hello, World!'

@app.route('/hostname')
def get_hostname():
    return socket.gethostname()

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=80,debug=True)