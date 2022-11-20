import json
from pathlib import Path

import scrapy

from threesixfive.spiders.utils import format_folder_and_file_name, read_secrets


class VideosSpider(scrapy.Spider):
    name = "videos"

    def start_requests(self):
        with open("data/playbacks/video.json") as reader:
            data = json.loads(reader.read())

        secrets = read_secrets(self.name)
        headers, cookies = secrets["headers"], secrets["cookies"]

        for doc in data:
            url = doc["src"]
            extra_data = {
                "course_name": doc["course_name"],
                "chapter_name": doc["chapter_name"],
                "lesson_name": doc["lesson_name"],
            }

            yield scrapy.Request(
                url=url,
                headers=headers,
                cookies=cookies,
                callback=self.parse,
                cb_kwargs=extra_data,
            )

    def parse(self, response, **kwargs):
        course_name = kwargs["course_name"]
        chapter_name = kwargs["chapter_name"]
        lesson_name = kwargs["lesson_name"]
        data = response.body

        course_name = format_folder_and_file_name(course_name)
        chapter_name = format_folder_and_file_name(chapter_name)
        lesson_name = format_folder_and_file_name(lesson_name)
        location = f"data/videos/{course_name}/{chapter_name}"
        Path(location).mkdir(parents=True, exist_ok=True)

        with open(f"{location}/{lesson_name}.mp4", "wb") as writer:
            writer.write(data)

        print(f"Saved new video {location}/{lesson_name}.mp4")
