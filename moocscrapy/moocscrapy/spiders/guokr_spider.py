import scrapy
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
			yield item