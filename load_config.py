import json
import os
import logging

logger = logging.getLogger(__name__)

# LOAD TOKEN
with open("config.json") as config:
    logger.info(">>> Loading Token ... ")
    data = json.load(config)
    token = data["KEY"]
    api_key = data["TWITTER_KEY"]
    api_secret = data["TWITTER_SECRET"]
    bearer_token = data["BEARER_TOKEN"]

# LOAD TOKEN
os.environ["KEY"] = token
os.environ["BEARER_TOKEN"] = bearer_token
os.environ["TWITTER_KEY"] = api_key
os.environ["TWITTER_SECRET"] = api_secret
logger.info(">>> Token in Environment ... ")
