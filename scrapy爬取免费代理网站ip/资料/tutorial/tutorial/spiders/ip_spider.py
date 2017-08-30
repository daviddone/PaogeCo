import scrapy


class QuotesSpider(scrapy.Spider):
    name = "ips"
    # allowed_domains = ["xicidaili.com"]
    def start_requests(self):
        urls = [
            'http://www.xicidaili.com',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        ip_list = response.css("table#ip_list tr")
        f = open("ips.txt","w")
        self.log("ip_list len is %d" %len(ip_list))
        print(type(ip_list))
        print(len(ip_list))
        for item in ip_list:
            print(str(item))
            print(len(item.css("h2")))
            print(len(item.css("tr.subtitle")))
            if len(item.css("h2")) == 0 and len(item.css("tr.subtitle")) == 0:
                print("aaaaaaaaaa")
                ip = item.xpath("td[2]/text()")[0].extract()  #xpath 第二个td下的数据
                port = item.xpath("td[3]/text()")[0].extract()
                ip2 = item.css("td")[1].css("td::text")[0].extract()  #css td列表中的第二个
                # ip1 = item.xpath("td[4]/text()")[0].extract()
                f.writelines("%s %s \n"%(ip,port))
                print(ip)
                print(type(ip2))
                print(ip2)
            self.log('item%s' % item)
        f.close()
