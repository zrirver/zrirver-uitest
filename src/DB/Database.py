#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/8/21下午4:20
# @Author : zhaohe
from src.env import DATABASE
import time
import MySQLdb
import itertools


class Database:
    mydb = MySQLdb.connect(
        host=DATABASE["host"],
        port=DATABASE["port"],
        user=DATABASE["user"],
        passwd=DATABASE["passwd"],
        db=DATABASE["db"],
        )

    def delete_basket(self, xx_id):
        mycursor = self.mydb.cursor()
        mycursor.execute("use xxx")
        mycursor.execute("SELECT * FROM xx WHERE xx = {0}".format(xx_id))
        attribute_info = mycursor.fetchall()
        mycursor.execute("DELETE FROM xx WHERE xx = {0}".format(xx_id))
        self.mydb.commit()
        mycursor.close()

    @classmethod
    def get_order_status(cls, order_number):
        mycursor = cls.mydb.cursor()
        orders_status = mycursor.fetchall()[0][0]
        mycursor.close()
        return orders_status

    @classmethod
    def add_coupons(cls):
        mycursor = cls.mydb.cursor()
        mycursor.execute("use xx")
        i = 0
        column1 = ['a', 'b', 'c']
        column2 = [0, 1, 2]
        column3 = ['test']

        test_para = [column1, column2, column3]
        commands = []
        # 开始计算各个条件的笛卡尔集
        for item in itertools.product(*test_para):
            l1 = list(item)
            l1[6] = 'xxcode' + str(i)
            item = tuple(l1)
            mysql_command = "INSERT into xx".format(
                item)
            commands.append(mysql_command)
            i = i + 1
        print(i)

        cmds = commands[11:240]
        for cmd in cmds:
            print(cmd)
            try:
                mycursor.execute(cmd)
                cls.mydb.commit()
            except Exception as e:
                print(e)
                cls.mydb.rollback()
            print("sql执行完毕")
            time.sleep(1)
        mycursor.close()
