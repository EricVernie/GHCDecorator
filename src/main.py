from flask import Flask
from module.decorator import validate_token
app = Flask(__name__)

@app.route('/')
@validate_token('Data.Reader')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(port=80,debug=True)