import pymysql


def main():
    # 创建连接
    coon = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='xxx1314520',
                           database='jing_dong', charset='utf8')

    # 创建游标
    cursor = coon.cursor()

    # 执行
    for i in range(100000):
        cursor.execute("insert into test_index values('ha-%d')" % i)

    # 提交数据
    coon.commit()


if __name__ == '__main__':
    main()
