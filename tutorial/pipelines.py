# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html



# import csv
# from tutorial import settings

# def write_to_csv(item):
#    writer = csv.writer(open(settings.csv_file_path, 'a'), lineterminator='\n')
#    writer.writerow([item[key] for key in item.keys()])

# class WriteToCsv(object):
#     # def __init__(self):
#     #     mkdirs(settings['csv_file_path'])

#     def process_item(self, item, spider):
#         write_to_csv(item)
#         return item


class TutorialPipeline(object):
    def process_item(self, item, spider):
        return item
