import pymysql
from pymysql import InternalError

db = None


def __openConnect():
    # 打开数据库连接
    global db
    db = pymysql.connect("rm-2ze0gur4knf5f648joo.mysql.rds.aliyuncs.com",
                         "zhanglifan", "Larry@1987", "stock_trade")
    print("数据库连接已打开")
    # 使用 cursor() 方法创建一个游标对象 cursor
    return db.cursor()


def closeConnect(needCommit=False):
    # 关闭数据库连接
    global db
    if db is not None:
        if needCommit is True:
            db.commit()
            print("提交了事务")
    db.close()
    print("数据库连接已关闭")


def executeSqlBatch(sql):
    global db

    if db is None or db.open is False:
        cursor = __openConnect()
    else:
        cursor = db.cursor()
    try:
        cursor.execute(sql)
    except InternalError:
        print(sql)
        db.rollback()
        db.close()
        print("数据库连接已关闭")
        raise


def executeSql(sql, queryType=False):
    cursor = __openConnect()
    try:
        cursor.execute(sql)
    except InternalError:
        print(sql)
        db.rollback()
        db.close()
        print("数据库连接已关闭")
        raise

    if queryType is True:
        # 使用 fetchone() 方法获取单条数据.
        data = cursor.fetchall()
        db.close()
        print("数据库连接已关闭")
        return data
    else:
        db.commit()
        print("提交了事务")
        db.close()
        print("数据库连接已关闭")
