# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import psycopg2


class SrealityPipeline:
    def __init__(self):
        hostname = 'db-scrapy'
        username = 'postgres'
        password = '12345' # your password
        database = 'postgres'

        ## Create/Connect to database
        self.connection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)
        
        ## Create cursor, used to execute commands
        self.cur = self.connection.cursor()
        
        ## Create quotes table if none exists
        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS flats(
            id serial PRIMARY KEY, 
            title text,
            img text
        )
        """)

    def process_item(self, item, spider):
        self.cur.execute(""" insert into flats (title, img) values (%s,%s)""", (
            item["title"],
            item["img"]
        ))

        ## Execute insert of data into database
        self.connection.commit()
        return item

    def close_spider(self, spider):

        ## Close cursor & connection to database 
        self.cur.close()
        self.connection.close()
