from function import *
from discord_handler import *
from selenium import webdriver
import time
from dotenv import load_dotenv
load_dotenv()

dcbot.run(os.getenv("Discord_APIKEY"))

