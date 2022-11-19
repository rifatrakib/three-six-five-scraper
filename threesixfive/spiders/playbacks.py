import json
import os

import scrapy

from threesixfive.items import MediaSource
from threesixfive.spiders.utils import read_secrets


class PlaybacksSpider(scrapy.Spider):
    name = "playbacks"
    base_url = "https://edge.api.brightcove.com/playback/v1"

    def start_requests(self):
        with open("data/lessons/video.json") as reader:
            data = json.loads(reader.read())

        secrets = read_secrets(self.name)
        headers, cookies = secrets["headers"], secrets["cookies"]

        for doc in data:
            ext_id = doc["video"]["extId"]
            url = f"{self.base_url}/accounts/6258000438001/videos/{ext_id}"
            extra_data = {
                "course_name": doc["course_name"],
                "chapter_name": doc["chapter_name"],
                "lesson_name": doc["video"]["name"],
            }

            yield scrapy.Request(
                url=url,
                headers=headers,
                cookies=cookies,
                callback=self.parse,
                cb_kwargs=extra_data,
            )

    def parse(self, response, **kwargs):
        data = response.json()
        sources = data["sources"]
        course_name = kwargs["course_name"]
        chapter_name = kwargs["chapter_name"]
        lesson_name = kwargs["lesson_name"]

        subtitle = None
        for item in data["text_tracks"]:
            if item["id"]:
                link = item["src"]
                subtitle = link.replace("http://", "https://") if link else None

            if subtitle:
                break

        for source in sources:
            if source.get("container", None) == "MP4":
                source["key"] = "video"
                source["subtitle"] = subtitle

            source["course_name"] = course_name
            source["chapter_name"] = chapter_name
            source["lesson_name"] = lesson_name

            yield MediaSource(**source)

        location = "logs/responses/playbacks"
        if not os.path.isdir(location):
            os.mkdir(location)

        with open(f"{location}/playbacks.json", "w") as writer:
            writer.write(json.dumps(data, indent=4))
