import json
import os


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


modules = ["courses"]
for module in modules:
    prepare_headers_and_cookies(module)
