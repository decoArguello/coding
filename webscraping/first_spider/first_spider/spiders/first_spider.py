import scrapy


class FirstSpyder(scrapy.Spider):
    name = "first"

    def start_requests(self):
        urls = [
            'https://www.fincaraiz.com.co/sitemap.aspx'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-1]
        filename = f'{page}.html'
        with open(filename, 'wb') as f:
            f.write(response.css("script") )
            print("###############################################################")
            print("###############################################################")
            print("###############################################################")
            print("###############################################################")
            print("###############################################################")
            print(response.css("script"))
            # f.# write(sec4)
        self.log(f'Saved file {filename}')

    