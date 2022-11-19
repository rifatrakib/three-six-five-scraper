import json
import os
import subprocess
from pathlib import Path


def prepare_headers_and_cookies(name):
    with open(f"curls/{name}.txt") as reader:
        lines = reader.readlines()[1:-1]

    headers = {}
    cookies = {}
    for line in lines:
        key, value = line[6:-4].split(": ")
        if key == "cookie":
            for cookie in value.split("; "):
                key, value = cookie.split("=", 1)
                cookies[key] = value
        else:
            headers[key] = value

    location = "secrets"
    if not os.path.isdir(location):
        os.mkdir(location)

    secrets = {"headers": headers, "cookies": cookies}
    with open(f"{location}/{name}.json", "w") as writer:
        writer.write(json.dumps(secrets, indent=4))


def run_spider(spider_name):
    location = f"logs/{spider_name}"
    Path(f"{location}").mkdir(parents=True, exist_ok=True)
    logger = f"{location}/{spider_name}-logs.log"
    command = f"scrapy crawl {spider_name} 2>&1 | tee {logger}"
    subprocess.run(command, shell=True)
