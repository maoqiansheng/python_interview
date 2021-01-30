from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def index():
    print(request.data)
    print(request.form)
    print(request.args)
    print(request.cookies)
    print(request.headers)
    print(request.method)
    print(request.url)
    print(request.files)

    return "helloworld"


if __name__ == '__main__':
    app.run()