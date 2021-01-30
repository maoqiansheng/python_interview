from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# 配置信息
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:mao1314520@127.0.0.1:3306/test"
# 设置压制警告信息,如果True会追踪数据库变化,会增加显著开销,所以建议设置为False
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# 创建SQLAlchemy类对象,关联app
db = SQLAlchemy(app)


# 编写模型类,继承db.Model
# 角色,用户之间的关系
class Role(db.Model):
    __tablename__ = "roles"  # 指定表名称
    # 参数1:表示整数类型,  参数2:表示主键
    id = db.Column(db.Integer, primary_key=True)
    # 角色名唯一的
    name = db.Column(db.String(64), unique=True)

    # 需要设置关系属性relationship(不会产生字段),设置在一方
    # 给Role添加了users关系属性, 查询格式: role.users
    # 给User添加了role关系属性(反向引用),查询格式: user.role
    users = db.relationship('User', backref='role')

    # 为了方便的看到对象输出的内容__repr__, 如果是普通类__str__
    def __repr__(self):
        return "<Role:%s>" % self.name


# 用户(多方)
class User(db.Model):
    __tablename__ = "users"  # 指定表名称
    # 参数1:表示整数类型,  参数2:表示主键
    id = db.Column(db.Integer, primary_key=True)
    # 用户名唯一的
    name = db.Column(db.String(64), unique=True)
    # 邮箱密码
    email = db.Column(db.String(64), unique=True)
    password = db.Column(db.String(64))

    # 外键
    role_id = db.Column(db.Integer, db.ForeignKey(Role.id))

    # 为了方便的看到对象输出的内容__repr__, 如果是普通类__str__
    def __repr__(self):
        return "<__repr__,User:%s,%s,%s,%s>" % (self.id, self.name, self.email, self.password)

    def __str__(self):
        return "<__str__, User:%s>" % (self.name)


if __name__ == '__main__':
    # 为了演示方便,先删除数据库表,和模型类关联的表
    db.drop_all()

    # 创建表,所有继承自dbModel的表
    db.create_all()

    # 创建测试数据
    ro1 = Role(name='admin')
    db.session.add(ro1)
    db.session.commit()
    # 再次插入一条数据
    ro2 = Role(name='user')
    db.session.add(ro2)
    db.session.commit()
    role3 = Role(name='manager')
    db.session.add(role3)
    db.session.commit()

    # 多条用户数据
    us1 = User(name='wang', email='wang@163.com', password='123456', role_id=ro1.id)
    us2 = User(name='zhang', email='zhang@189.com', password='201512', role_id=ro2.id)
    us3 = User(name='chen', email='chen@126.com', password='987654', role_id=ro2.id)
    us4 = User(name='zhou', email='zhou@163.com', password='456789', role_id=ro1.id)
    us5 = User(name='tang', email='tang@itheima.com', password='158104', role_id=ro2.id)
    us6 = User(name='wu', email='wu@gmail.com', password='5623514', role_id=ro2.id)
    us7 = User(name='qian', email='qian@gmail.com', password='1543567', role_id=ro1.id)
    us8 = User(name='liu', email='liu@itheima.com', password='867322', role_id=ro1.id)
    us9 = User(name='li', email='li@163.com', password='4526342', role_id=ro2.id)
    us10 = User(name='sun', email='sun@163.com', password='235523', role_id=ro2.id)
    db.session.add_all([us1, us2, us3, us4, us5, us6, us7, us8, us9, us10])
    db.session.commit()

    app.run(debug=True)
