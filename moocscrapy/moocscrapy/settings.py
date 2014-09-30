# -*- coding: utf-8 -*-

# Scrapy settings for moocscrapy project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'moocscrapy'

SPIDER_MODULES = ['moocscrapy.spiders']
NEWSPIDER_MODULE = 'moocscrapy.spiders'

ITEM_PIPELINES = {
    'moocscrapy.pipelines.MoocscrapyPipeline': 800,
}

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'moocscrapy (+http://www.yourdomain.com)'
