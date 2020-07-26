# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class Maoyantop10Pipeline:
    # def process_item(self, item, spider):
    #     return item
    def process_item(self, item, spider):
        movie_name = item['movie_name']
        movie_type = item['movie_type']
        movie_start_time = item['movie_start_time']
        output = f'|{movie_name}|\t|{movie_type}|\t|{movie_start_time}|\n\n'
        with open(r'D:\pytest\Python-002\week01\homework_2\maoyantop10_2.csv', 'a+', encoding='utf-8') as article:
            article.write(output)
        return item