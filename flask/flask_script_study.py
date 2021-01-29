from flask import Flask
from flask_script import Manager
app = Flask(__name__)

manager = Manager(app)
@app.route('/')
def index():
    return "helloworld"


if __name__ == '__main__':
    manager.run()
