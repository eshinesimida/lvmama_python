# -*- coding: utf-8 -*-
import MySQLdb
import uuid
import random

class xiechengDAO(object):
    def __init__(self,host="*****",user="*****",password="2423324", db="fsdjlf"
                         ):
        self.host = host
        self.db = db
        self.user = user
        self.password = password



    def savehotellink(self,listPageInfo):
        db = MySQLdb.connect(self.host,self.user,self.password,self.db,use_unicode=1,charset='utf8')
        cursor = db.cursor()
        for hotel in listPageInfo:
            try:
                    id = uuid.uuid1()
                    cursor.execute("insert IGNORE into lvmama(jingqu,province,author,ID,comment,time)values(%s,%s,%s,%s,%s,%s)" ,
                                   (hotel["jingqu"],hotel["province"],hotel["author"],hotel["ID"],hotel["comment"],hotel["time"]))
            except Exception,e:
                print hotel["ID"]
        db.commit()
        cursor.close()
        db.close()

    