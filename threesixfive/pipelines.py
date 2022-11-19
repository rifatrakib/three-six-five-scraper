import json
import os
from datetime import datetime

from itemadapter import ItemAdapter
from scrapy import signals


class JSONPipeline:
    @classmethod
    def from_crawler(cls, crawler):
        pipeline = cls()
        crawler.signals.connect(pipeline.spider_opened, signals.spider_opened)
        crawler.signals.connect(pipeline.spider_closed, signals.spider_closed)
        return pipeline

    def spider_opened(self, spider):
        spider_name = spider.name

        location = "data/base"
        if not os.path.isdir(location):
            os.mkdir(location)

        self.file = open(f"{location}/{spider_name}-base.json", "w")
        header = "[\n"
        self.file.write(header)

    def spider_closed(self, spider):
        footer = "]\n"
        self.file.write(footer)
        self.file.close()

        spider_name = spider.name
        with open(f"data/base/{spider_name}-base.json", "r") as reader:
            data = reader.read()

        data = data.rpartition(",")
        data = data[0] + data[-1]
        data = json.loads(data)
        with open(f"data/base/{spider_name}-base.json", "w") as writer:
            writer.write(json.dumps(data, indent=4))

        self.post_process(spider_name)

    def process_item(self, item, spider):
        data = ItemAdapter(item).asdict()
        for key, value in data.items():
            if isinstance(value, datetime):
                data[key] = str(value)
        line = json.dumps(data, indent=4) + ",\n"
        self.file.write(line)
        return item

    def post_process(self, spider_name):
        with open(f"data/base/{spider_name}-base.json", "r") as reader:
            data = json.loads(reader.read())

        location = f"data/{spider_name}"
        if not os.path.isdir(location):
            os.mkdir(location)

        splits = {}
        for doc in data:
            key = doc["key"]
            if key not in splits:
                splits[key] = []
            splits[key].append(doc)
        print(splits.keys())
        for split, split_data in splits.items():
            with open(f"{location}/{split}.json", "w") as writer:
                writer.write(json.dumps(split_data, indent=4))
