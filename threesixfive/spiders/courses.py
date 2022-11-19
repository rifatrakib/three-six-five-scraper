import json
import os

import scrapy

from threesixfive.items import Course, Module, Page, Recommendation, UpcomingCourse
from threesixfive.spiders.utils import read_secrets


class CoursesSpider(scrapy.Spider):
    name = "courses"

    def start_requests(self):
        url = "https://api.365datascience.com/courses"
        secrets = read_secrets(self.name)
        headers, cookies = secrets["headers"], secrets["cookies"]
        yield scrapy.Request(
            url=url,
            headers=headers,
            cookies=cookies,
            callback=self.parse,
        )

    def parse(self, response):
        data = response.json()
        courses = data["courses"]
        modules = data["modules"]
        page = data["page"]
        recommendations = data["recommendations"]
        upcoming_courses = data["upcoming"]

        for course in courses:
            yield Course(**course)

        for module in modules:
            yield Module(**module)

        yield Page(**page)
        yield Recommendation(**recommendations)

        for upcoming_course in upcoming_courses:
            yield UpcomingCourse(**upcoming_course)

        location = "logs/responses/courses"
        if not os.path.isdir(location):
            os.mkdir(location)

        with open(f"{location}/courses.json") as writer:
            writer.write(json.dumps(data, indent=4))
