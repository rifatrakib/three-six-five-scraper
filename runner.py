from utils import prepare_headers_and_cookies, run_spider

modules = [
    "courses",
    "lessons",
    "playbacks",
    "videos",
]

for module in modules:
    prepare_headers_and_cookies(module)
    run_spider(module)
