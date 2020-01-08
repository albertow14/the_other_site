import scrapy
from corgis.items import CorgisItem


# queremos extraer todos los precios y titulos de los vinos con sus paginaciones
# Normalmente el parse nos sirve para definir el proceso de extraccion de las urls




class VinosCorteInglesSpider(scrapy.Spider):
    name = 'corgirules'
    allowed_domains = ['https://www.elcorteingles.es/']
    start_urls = ['https://www.elcorteingles.es/club-del-gourmet/vinos/espana/']

    def parse(self, response):
        mlitems = CorgisItem()

        mlitems['titulo'] = response.xpath('//h3[@class="info-name"]/a[1]/@title').extract()
        mlitems['precio'] = response.xpath('//div[@class="product-price "]/span/text()').extract()
        
        yield mlitems
        