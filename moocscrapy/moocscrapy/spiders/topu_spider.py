import scrapy
import re
from moocscrapy.items import MoocscrapyItem

class TopuSpider(scrapy.Spider):
	name = "topu"
	allowed_domains = ["topu.com"]
	start_urls = [
		"http://www.topu.com/kvideo.php?do=search"
	]

	def parse(self, response):
		for sel in response.xpath('//dl[@class="zhibo_dl zhibo_dl_linshi"]/dt'):
			item = MoocscrapyItem()
			item['title'] = sel.xpath('a/@title').extract()[0]
			item['link'] = "http://www.topu.com" + sel.xpath('a/@href').extract()[0]
			item['image'] = "http://www.topu.com" + sel.xpath('a//img/@src').extract()[0]
			item['site'] = 'topu'

			m = re.search('(?<=mooc\/)\d+', item['link'])
			if m:
				item['id'] = 'topu_' + str(m.group(0))
			yield item