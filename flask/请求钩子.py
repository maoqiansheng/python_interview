from flask import Flask

app = Flask(__name__)

@app.before_first_request
def first_request():
    print('我在视图函数第一次请求之前被调用')

@app.before_request
def before_request():
    print("我是在每次被调用前都会执行")

@app.after_request
def after_request(response):
    response.headers["Content-Type"] = "application/json"
    print(response.status)
    return response

@app.teardown_request
def teardown_request(e):
    print(e)
    print("teardown_request")

@app.route('/de')
def index():
    return "helloworld"


if __name__ == '__main__':
    app.run()
