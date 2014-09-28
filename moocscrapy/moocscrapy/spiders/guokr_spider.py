import scrapy
from moocscrapy.items import MoocscrapyItem

class GuokrSpider(scrapy.Spider):
	name = "guokr"
	allowed_domains = ["guokr.com"]
	start_urls = [
		"http://mooc.guokr.com/course/"
	]

	def parse(self, response):
		for sel in response.xpath('//a[@class="listinglink"]'):
			item = MoocscrapyItem()
			item['title'] = sel.xpath('text()').extract()[0]
			item['link'] = sel.xpath('@href').extract()[0]
			yield item