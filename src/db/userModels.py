#!/usr/bin/python3
#coding=utf-8

##############################################
#
# Author:       Shen Wenrui
# Date:         20180526
# Description:
#
##############################################

import mysql.connector
import logging

from .dbsettings import dbconnector_freeId

logger = logging.getLogger("database")



class userModels():
    def __init__(self):
        self.__db = dbconnector_freeId

    def dbTest(self):
        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = self.__db.cursor()
        # 使用 execute()  方法执行 SQL 查询
        cursor.execute("SELECT VERSION()")
        # 使用 fetchone() 方法获取单条数据.
        data = cursor.fetchone()
        logger.info("Database version : %s " % data)

    def getAllUserInfo(self):
        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = self.__db.cursor()

        # SQL 查询语句
        sql = "SELECT * FROM FreeAppleIdUserInfo "

        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取所有记录列表
            results = cursor.fetchall()
            logger.info("User info rows' size: %d" % len(results))
            for row in results:
                Id_P = row[0]
                userEmail = row[1]
                applePassword = row[2]
                LastName = row[3]
                FirstName = row[4]
                BirthDay = row[5]
                Address = row[6]
                City = row[7]

                # 打印结果
                logger.info("Id_P: %d, \tuserEmail: %s, \tapplePassword: %s, \tLastName: %s, \tFirstName: %s," \
                            " \tBirthDay: %s, \tAddress: %s, \tCity: %s" % \
                      (Id_P, userEmail, applePassword, LastName, FirstName, BirthDay, Address, City))
        except Exception as err:
            logger.error(repr(err))

    # select by email:
    #def insertNewUserInfo(self):
    # Update
    # Delete


