from flask import Flask
from werkzeug.exceptions import abort

app = Flask(__name__)


@app.route('/game/<int:age>')
def play_game(age):
    # 异常抛出
    abort(405)

    return "helloworld"


#异常捕获
@app.errorhandler(405)
def page_not_found(e):
    print(e)
    return "找不到服务器资源,服务器搬家了"
if __name__ == '__main__':
    app.run()
