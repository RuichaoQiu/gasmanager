# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import sys
import MySQLdb
import hashlib
from scrapy.exceptions import DropItem
from scrapy.http import Request

class MySQLStorePipeline(object):
    def __init__(self):
        self.conn = MySQLdb.connect(host="localhost", # your host, usually localhost
                         user="root", # your username
                          passwd="", # your password
                          db="GMData", charset="utf8", use_unicode=True)
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        try:
            self.cursor.execute('INSERT INTO testdata(name, address, price) VALUES ("%s","%s","%s")' % (item['name'][0].encode('utf-8'),item['address'][0].encode('utf-8'),item['price'][0].encode('utf-8')))

            self.conn.commit()


        except MySQLdb.Error, e:
            print "Error %d: %s" % (e.args[0], e.args[1])


        return item