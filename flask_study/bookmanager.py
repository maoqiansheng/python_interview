from flask import Flask, request, flash, url_for, render_template
from flask_wtf.csrf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import redirect
import pymysql

pymysql.install_as_MySQLdb()
app = Flask(__name__)
# 开启CSRF保护
CSRFProtect(app)
# 数据库配置


app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:mao1314520@127.0.0.1:3306/library'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# 设置密码
app.config['SECRET_KEY'] = "jfkdjfkdkjf"
db = SQLAlchemy(app)


# 定义模型类
# Author 作者（一方）
class Author(db.Model):
    __tablename__ = 'authors'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    # 关系属性和反向引用
    books = db.relationship('Book', backref='author')


class Book(db.Model):
    __tablename__ = 'book'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    # 外键
    author_id = db.Column(db.Integer, db.ForeignKey('authors.id'))


# 展示
@app.route('/')
def show_page():
    authors = Author.query.all()
    # book_list = []
    # for book in books:
    #     item = dict()
    #     item[book.author.name] = book.name
    #     book_list.append(item)
    # print(book_list)
    return render_template('books.html', authors=authors)


# 添加书籍
@app.route('/add_book/', methods=['POST', 'GET'])
def add_book():
    # 1、从表单获取参数
    author_name = request.form.get('author')
    book_name = request.form.get('book')
    # 2、参数是否存在校验
    if not all([author_name, book_name]):
        return '作者或书籍为空'
    # 3、通过作者名字查询作者对象
    author = Author.query.filter(Author.name == author_name).first()
    # 如果作者存在
    if author:
        # 查询书籍对象是否存在
        book = Book.query.filter(Book.name == book_name, Book.author_id == author.id).first()
        if book:
            flash('该作者已经添加过该书籍')
        else:
            book = Book(name=book_name, author_id=author.id)
            db.session.add(book)
            db.session.commit()
    # 反之。作者存在
    else:
        new_author = Author(name=author_name)
        db.session.add(new_author)
        db.session.commit()
        # 添加书记并关联外键
        book = Book(name=book_name, author_id=new_author.id)
        db.session.add(book)
        db.session.commit()
    # 5.重定向展示页
    return redirect(url_for('/'))


# 删除书籍
@app.route('/delete_book/<int:book_id>')
def delete_book(book_id):
    # 1.根据编号获取书籍对象
    book = Book.query.get(book_id)

    # 2.删除书籍
    db.session.delete(book)
    db.session.commit()

    # 3.重定向页面展示
    return redirect(url_for('/'))


# 删除作者
@app.route('/delete_author/<int:author_id>')
def delete_author(author_id):
    # 1.通过编号获取作者对象
    author = Author.query.get(author_id)

    # 2.删除作者书籍
    for book in author.books:
        db.session.delete(book)

    # 3.删除作者对象
    db.session.delete(author)
    db.session.commit()

    # 4.重定向展示页面
    return redirect(url_for('/'))


if __name__ == '__main__':
    db.drop_all()
    db.create_all()
    au1 = Author(name='老王')
    au2 = Author(name='老尹')
    au3 = Author(name='老刘')
    # 把数据提交给用户会话
    db.session.add_all([au1, au2, au3])
    # 提交会话
    db.session.commit()

    bk1 = Book(name='老王回忆录', author_id=au1.id)
    bk2 = Book(name='我读书少，你别骗我', author_id=au1.id)
    bk3 = Book(name='如何才能让自己更骚', author_id=au2.id)
    bk4 = Book(name='怎样征服美丽少女', author_id=au3.id)
    bk5 = Book(name='如何征服英俊少男', author_id=au3.id)
    # 把数据提交给用户会话
    db.session.add_all([bk1, bk2, bk3, bk4, bk5])
    # 提交会话
    db.session.commit()

    app.run(debug=True)
