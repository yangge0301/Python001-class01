# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

class MaoyanPipeline:
    def process_item(self, item, spider):
        # return item
        film_name = item['film_name']
        film_type = item['film_type']
        film_date = item['film_date']
        output = f'|{film_name}|\t|{film_type}|\t|{film_date}|\n\n'
        with open('./maoyan-work2.csv','a+',encoding='utf-8') as acticle:
            acticle.write(output)
            acticle.close()
        return item
