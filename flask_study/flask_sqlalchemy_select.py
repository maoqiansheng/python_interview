from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_study.flask_sqlalchemy_study import User, Role, db
from sqlalchemy import not_, and_
import pymysql
pymysql.install_as_MySQLdb()

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:mao1314520@127.0.0.1:3306/test"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)

# @app.route('/')
# def index():
# user_wang = User.query.filter_by(name='wang').all()
# user = User.query.first()
# users = User.query.all()
# g_user = User.query.filter(User.name.endswith('g')).all()
# get_user = User.query.get(1)
# no_wang_user = User.query.filter(User.name != 'wang').all()
# not_wang_user = User.query.filter(not_(User.name == 'wang')).all()
# endswith_163 = User.query.filter(and_(User.name != 'wang', User.email.endswith('163.com'))).all()
# print(user_wang)
# print(user)
# print(users)
# print(g_user)
# print(get_user)
# print(no_wang_user)
# print(not_wang_user)
# print(endswith_163)
# db.session.delete(user)
# db.session.commit()
# user1 = User.query.first()
# user1.name = 'mao'
# db.session.commit()
# print(user1)
# 关联查询
role1 = Role.query.first()
print(role1)
print(role1.users)
user3 = User.query.get(3)
print(user3.role_id)
print(user3.role)  #  backref='role'




    # return 'ok'


if __name__ == '__main__':
    app.run()
