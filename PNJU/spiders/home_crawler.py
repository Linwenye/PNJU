import logging
import re
import sys
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.http import Request, FormRequest, HtmlResponse
from PNJU import config

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    handlers=[logging.StreamHandler(sys.stdout)])


class HomeCrawler(scrapy.Spider):
    name = 'home'

    start_urls = ['http://p.nju.edu.cn/portal/index.html?v=201606170634']

    post_headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.8,en;q=0.6",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36",
        "Referer": "http://p.nju.edu.cn/portal/index.html?v=201606170634",
    }

    def start_requests(self):
        return [Request('http://p.nju.edu.cn/portal/index.html?v=201606170634', meta={'cookiejar': 1},
                        callback=self.post_login)]

    # 使用FormRequeset模拟表单提交
    def post_login(self, response):
        return [FormRequest(url='http://p.nju.edu.cn/portal_io/login',
                            meta={'cookiejar': response.meta['cookiejar']},
                            headers=self.post_headers,
                            formdata={
                                'username': config.username,
                                'password': config.password,
                            },
                            callback=self.after_login,
                            )]

    def after_login(self, response):
        pass

    def parse(self, response):
        pass
