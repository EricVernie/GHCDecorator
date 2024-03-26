from flask import Flask
from module.decorator import validate_token
app = Flask(__name__)

@app.route('/')
def health():
    return 'status, healthy!'

@app.route('/hello')
@validate_token('Data.Reader')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(host="20.160.177.105",port=80,debug=True)