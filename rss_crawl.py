import feedparser
import json
import ssl

# INIT SSL
if hasattr(ssl, '_create_unverified_context'):
    ssl._create_default_https_context = ssl._create_unverified_context

# LOAD
source_data = "./data/sources.json"
sources = json.load(open(source_data, "r"))
source_urls = [(k, v) for k,v in sources.items()]

# SCRAPE
scrape = []
for source, url in source_urls:
    rss = feedparser.parse(url)

    result = {
        "source": source,
        "url": url,
        "rss": rss,
        "entries": rss.entries
    }

    scrape.append(result)


# STORE
data_dir = "./data/RSS_objects.jsonl"
count = 0

with open(data_dir, "w") as f:
    for _ in scrape:

        source = _["source"]
        base_url = _["url"]

        for i in _["entries"]:
            count += 1
            i["id"] = count

            f.write(json.dumps(i))
            f.write("\n")
