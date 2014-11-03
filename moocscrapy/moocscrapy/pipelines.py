# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import requests
import json

class MoocscrapyPipeline(object):
    
    def process_item(self, item, spider):
    	url = "http://localhost:9200/moocsearch/course/" + item['id'] + '/_create'
    	payload = {'title': item['title'], 'link': item['link'], 
    			   'image':item['image'], 'site': item['site']}
    	headers = {'content-type': 'application/json'}

    	requests.put(url, data=json.dumps(payload), headers=headers);

        return item