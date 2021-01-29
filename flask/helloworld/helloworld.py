# 1.导入Flask类
from flask import Flask, request, jsonify, url_for

# 2.创建Flask对象接收一个参数__name__，它会指向程序所在的包
from werkzeug.utils import redirect


class Config():
    DEBUG = True


app = Flask(__name__)
app.config.from_object(Config)

# 从配置文件中加载配置
# app.config.from_pyfile('config.py')
# 加载指定环境变量名称所对应的相关配置
# app.config.from_envvar('FLASKCONFIG')


# 3.装饰器的作用是将路由映射到视图函数index
@app.route('/')
def index():
    return "helloworld"


# 指定访问视图函数demo1,访问路径为/demo1
@app.route('/demo1')
def demo1():
    return 'demo1'


# 路由传递参数,整数
# @app.route('/user/<int:user_id>')
# def user_info(user_id):
#     return 'the num is %d' % user_id


# 路由传递参数,字符串,不指定path默认就是字符串
@app.route('/user/<path:user_id>')
def user_info(user_id):
    # print(type(user_id))
    return 'hello %s' % user_id


@app.route('/demo2', methods=['GET', 'POST'])
def demo2():
    # 直接从请求中取到请求方式并返回
    return request.method


# 生成json数据响应体
@app.route('/demo4')
def demo4():
    json_dict = {
        "user_id": 10,
        "user_name": "laowang"
    }
    return jsonify(json_dict)
# 重定向
@app.route('/demo5')
def demo5():
    return redirect('https://www.baidu.com')

# 重定向，反解析到别的视图
@app.route('/demo6')
def demo6():
    return redirect(url_for('demo1'))
# 返回自定义的状态码
@app.route('/demo7')
def demo7():
    return '状态码为666', 666
# 4.Flask应用程序实例的run方法,启动WEB服务器
# 如果当前模块是程序的入口模块（也称顶级模块、脚本文件）
if __name__ == '__main__':
    # app.run(host="0.0.0.0", port=5000, debug=True)
    app.run()