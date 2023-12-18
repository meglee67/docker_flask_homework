# this code is copied and modified from https://github.com/hantswilliams/HHA_504_2023/blob/main/WK8/code/docker_example_3_compose/flask2/app.py

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello from Flask App 2 !!!! \n This is a completly new flask application. \n Pretty cool! \n'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
