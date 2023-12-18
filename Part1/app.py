# this code is copied and modified from https://github.com/hantswilliams/HHA_504_2023/blob/main/WK8/code/docker_example_1/app.py

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World! From a Flask app in a Docker container!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
