# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo


class CorgisPipeline(object):
    def __init__(self):
        self.conn = pymongo.MongoClient(
            'localhost',
            27017
        )
        db = self.conn['imagenes']
        self.collection = db['imagenes_tb']


    def process_item(self, item, spider):
        self.collection.insert(dict(item))
        return item

    def get_all_items(self):
        return self.collection.find()
