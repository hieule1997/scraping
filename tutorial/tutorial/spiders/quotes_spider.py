import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'https://hyipclub.club/?fbclid=IwAR0p82YKx_wBMMVwSQvQGrkdfNpZPf1C_0rZqGdZIWmu193oABClffVu0bQ',
    ]

    def parse(self, response):
        for ibox in response.css('div.khunglon'):
            yield {
            "rpkhung" :  ibox.css('div.thanhbar div.nameprogram a::text').get() ,
            "lifetime" :  ibox.css('div.khunggiua1 div.khung-p2 ul li span::text').getall()[0],
            "Monitored" :   ibox.css('div.khunggiua1 div.khung-p2 ul li span::text').getall()[1],
            "Investment" :   ibox.css('div.khunggiua2 div.khung-p3 ul li span::text').getall()[0],
            "Payout" :   ibox.css('div.khunggiua2 div.khung-p3 ul li span::text').getall()[1],
            "Options" :   ibox.css('div.khunggiua2 div.khung-p3 ul li span img::attr(alt)').getall(),
            "Forum" :   ibox.css('div.khunggiua2 div.khung-p3 ul li span a::text').getall(),
            "status" : ibox.css('div.khunggiua3 div span::text').get(),
            "good" : ibox.css('div.khunggiua4 div.k-vote1 div.s-vote1 ul li.li-good span::text').get(),
            "bad" : ibox.css('div.khunggiua4 div.k-vote1 div.s-vote1 ul li.li-bad span::text').get(),
            "MinMax" : ibox.css('div.khunggiua4 div.khung-p4 ul li span::text').getall()[0],
            "Referral" : ibox.css('div.khunggiua4 div.khung-p4 ul li span::text').getall()[1],
            "Withdrawal" : ibox.css('div.khunggiua4 div.khung-p4 ul li span::text').getall()[2],
            "icon" : ibox.css('div.khunggiua4 div.khung-p4 ul li span a img::attr(alt)').getall(),
            "Payment" : ibox.css('div.khungplan1 p img::attr(alt)').getall(),
            "khungplan" : ibox.css('div.khungplan p::text').get(),
            }
            