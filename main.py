from function import *
import os
import os.path
from discord_handler import *
from selenium import webdriver
import time
from dotenv import load_dotenv

# load_dotenv()
if os.path.isfile("config.json"):
    configs = {}
    with open("config.json", "r") as c:
        configs = json.load(c)
else:
    configs = dict(os.environ)
dcbot.run(configs["Discord_APIKEY"])
