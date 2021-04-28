from function import *
from discord_handler import *
from selenium import webdriver
import time
from dotenv import load_dotenv
#load_dotenv()

configs = {}
with open("config.json", "r") as c:
    configs = json.load(c)

dcbot.run(configs["Discord_APIKEY"])
