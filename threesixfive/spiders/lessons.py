import json
import os

import scrapy

from threesixfive.items import Asset
from threesixfive.spiders.utils import read_secrets


class LessonsSpider(scrapy.Spider):
    name = "lessons"
    base_url = "https://api.365datascience.com/courses"

    def start_requests(self):
        with open("data/courses/courses.json") as reader:
            data = json.loads(reader.read())

        urls = []
        for doc in data:
            slug = doc["slug"]
            urls.append(f"{self.base_url}/{slug}/player")

        secrets = read_secrets(self.name)
        headers, cookies = secrets["headers"], secrets["cookies"]

        for doc in data:
            slug = doc["slug"]
            url = f"{self.base_url}/{slug}/player"
            course_name = doc["name"]

            yield scrapy.Request(
                url=url,
                headers=headers,
                cookies=cookies,
                callback=self.parse,
                cb_kwargs={"course_name": course_name},
            )

    def parse(self, response, **kwargs):
        data = response.json()
        sections = data["sections"]
        course_name = kwargs["course_name"]

        for index, section in enumerate(sections):
            assets = section["assets"]
            chapter_id = section["id"]
            chapter_order = section["order"]
            chapter_name = section["name"]
            for asset in assets:
                if "video" in asset and asset["video"]:
                    asset["key"] = "video"
                elif "type" in asset:
                    asset["key"] = asset["type"]

                asset["section"] = index + 1
                asset["course_name"] = course_name
                asset["chapter_id"] = chapter_id
                asset["chapter_name"] = chapter_name
                asset["chapter_order"] = chapter_order

                yield Asset(**asset)

        location = "logs/responses/lessons/"
        if not os.path.isdir(location):
            os.mkdir(location)

        identifier = data["slug"]
        with open(f"{location}/{identifier}.json", "w") as writer:
            writer.write(json.dumps(data, indent=4))
