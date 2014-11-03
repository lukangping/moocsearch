import scrapy
import re
from moocscrapy.items import MoocscrapyItem

class GuokrSpider(scrapy.Spider):
	name = "guokr"
	allowed_domains = ["guokr.com"]
	start_urls = [
		"http://mooc.guokr.com/course/"
	]

	def parse(self, response):
		for sel in response.xpath('//li[@class="course"]'):
			item = MoocscrapyItem()
			item['title'] = sel.xpath('h2//a//span/text()').extract()[0]
			item['link'] = sel.xpath('h2//a/@href').extract()[0]
			item['image'] = sel.xpath('a//img/@src').extract()[0]	
			item['site'] = 'guokr'

			m = re.search('(?<=course\/)\d+', item['link'])
			if m:
				item['id'] = 'guokr_' + str(m.group(0))

			yield item