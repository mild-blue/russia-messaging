import time
from math import sqrt

import numpy as np

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from settings import WEBDRIVER_PATH


class Messenger:
    url: str

    def __init__(self, url):
        self.url = url
        self.seconds_to_sleep = 15  # seconds to wait after page loading
        options = Options()
        # options.add_argument("--headless") # can be enabled when fully automated
        options.add_argument("--no-sandbox")
        options.add_argument("start-maximized")
        options.add_argument("disable-infobars")
        options.add_argument("--disable-extensions")
        options.add_argument("window-size=1920,1080")
        self.driver = webdriver.Chrome(options=options, executable_path=WEBDRIVER_PATH)
        self.driver.maximize_window()
        self.driver.get(self.url)
        self.sleep()

    def quit(self):
        self.driver.quit()

    def sleep(self):
        random_time = np.random.normal(loc=self.seconds_to_sleep, scale=sqrt(self.seconds_to_sleep))
        time.sleep(random_time)

