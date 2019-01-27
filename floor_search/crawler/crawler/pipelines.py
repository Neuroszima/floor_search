# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

# following solution for pipline used in scrapping method ported to django
# is a solution from following website:
# https://medium.com/@ali_oguzhan/how-to-use-scrapy-with-django-application-c16fabd0e62e

from scrappy.models import ScrapyItem
import json


class CrawlerPipeline():
    def __init__(self, unique_id, *args, **kwargs):
        self.unique_id = unique_id
        self.items = []

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            unique_id=crawler.settings.get('unique_id'), # this will be passed from django view
        )

    def close_spider(self, spider):
        # And here we are saving our crawled data with django models.

        # Project creator note:
        # This method is called, when a spider/crawler finishes it's work
        # here it is simple enough, when spider finishes processing elements and
        # can't find more, it saves a list of what he found as a json.dump,
        # along with other parameters to a Django "ScrapyItem" model

        item = ScrapyItem()
        item.unique_id = self.unique_id
        item.data = json.dumps(self.items)
        item.save()

    def process_item(self, item, spider):

        # Project creator note:
        # When creating pipeline, a process_item method is a must have
        # it decides what to do with every item that fulfills expectations of our search
        # here it just adds it to "items" list

        self.items.append(item['url'])
        return item
