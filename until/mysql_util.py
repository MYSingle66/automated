# -*- coding:utf-8 -*-
# @Time: 2022/9/28 12:15
# @Author: 小杨同学
# @Email: 541667133@qq.com
# @File: mysql_util.py
# 导入PyMySQL库
import json

import pymysql

from until.settings import DB_CONFIG

# 导入数据库的配置信息
class MysqlUtil:
    def __init__(self):
        # 读取配置文件，初始化pymysql数据库连接
        self.db = pymysql.connect(**DB_CONFIG)
        # 创建数据库游标  返回字典类型的数据
        self.cursor = self.db.cursor(cursor=pymysql.cursors.DictCursor)

    def select_first_data(self, sql):
        """
        查询第一条数据
        """
        try:
            # # 提交，防止事务冲突
            # self.conn.commit()

            # 执行 sql 语句
            self.cursor.execute(sql)
        except Exception as e:
            print("执行sql异常:%s" % e)
        else:
            # 获取查询到的第一条数据
            first_data = self.cursor.fetchone()
            # print(first_data)
            # 将返回结果转换成 str 数据格式，禁用acsii编码
            first_data = json.dumps(first_data, ensure_ascii=False)
            return first_data

    def select_all_data(self, sql):
        """
        查询结果集
        """
        try:
            self.cursor.execute(sql)
        except Exception as e:
            print("执行sql异常:%s" % e)
        else:
            first_data = self.cursor.fetchall()
            first_data = json.dumps(first_data, ensure_ascii=False)
            return first_data

    def get_count(self, sql):
        """
        获取数据条数
        """
        self.conn.commit()
        return self.cursor.execute(sql)

    def del_data(self, sql):
        """
        删除数据
        """
        res = {}
        try:
            # 执行SQL语句
            result = self.cursor.execute(sql)
            # print(result)
            if result != 0:
                # 提交修改
                self.conn.commit()
                res = {'删除成功'}
            else:
                res = {'没有要删除的数据'}
        except:
            # 发生错误时回滚
            self.conn.rollback()
            res = {'删除失败'}
        return res

    def update_data(self, sql):
        """
        修改数据
        """
        try:
            self.cursor.execute(sql)
            self.conn.commit()
            res = {'更新成功'}
        except Exception as e:
            self.conn.rollback()
            res = {'更新删除'}
        return res

    def insert_data(self, sql, data):
        """
        新增数据
        """

        try:
            self.cursor.execute(sql, data)
            self.conn.commit()
            res = {data, '新增成功'}
        except Exception as e:
            res = {'新增失败', e}
        return res

    # 关闭对象，staticmethod静态方法，可以直接使用类名.静态方法
    @staticmethod
    def close(self):
        # 关闭游标对象
        if self.cursor is not None:
            self.cursor.close()
        # 关闭数据库对象
        if self.db is not None:
            self.db.close()


if __name__ == '__main__':
    mysql = MysqlUtil()
    res = mysql.select_first_data('select * from login')
    print(res)