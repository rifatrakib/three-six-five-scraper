## IMPORTANT!!!

This directory will store the `JSON` data in different files after having scraped from the URLs. We can classify the JSON files stored in this directory into `two categories` as follows:

1. There will be a `base` folder which will contain the non-classified JSON data scraped directly after having gone through some basic validation with `Pydantic` models. There will be one JSON file for each scraper.

2. There will be some other folders named according to the names of each spider, and these will contain classified data in different JSON files containing parts of the responses scraped. Together, these files will make the whole response body. These classifications are made for easy retrieval and analysis of data later.
