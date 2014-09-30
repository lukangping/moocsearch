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
		for sel in response.xpath('//dl[@class="zhibo_dl zhibo_dl_linshi"]/dd[@class="title title_linshi"]'):
			item = MoocscrapyItem()
			item['title'] = sel.xpath('a/@title').extract()[0]
			item['link'] = sel.xpath('a/@href').extract()[0]

			m = re.search('(?<=mooc\/)\d+', item['link'])
			if m:
				item['id'] = 'topu_' + str(m.group(0))
			yield item