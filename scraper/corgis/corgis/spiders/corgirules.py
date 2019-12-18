# -*- coding: utf-8 -*-
import scrapy
from corgis.items import CorgisItem


class CorgirulesSpider(scrapy.Spider):
    name = 'corgirules'
    allowed_domains = ['gettyimages.es']
    start_urls = ['https://www.gettyimages.es/fotos/pembroke-welsh-corgi?sort=best&mediatype=photography&phrase=pembroke%20welsh%20corgi']

    def parse(self, response):
        mlitems = CorgisItem()

        mlitems['imagenes'] = response.xpath('//figure[@class="gallery-mosaic-asset__figure"]//@src').extract()
        
        yield mlitems
        
