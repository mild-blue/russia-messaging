import time

import numpy as np
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options

from settings import WEBDRIVER_PATH


def sleep_keyboard():
    random_time = abs(np.random.normal(0, 0.2))
    time.sleep(random_time)


class Messenger:
    url: str

    def __init__(self, url):
        self.url = url
        self.seconds_to_sleep = 5  # seconds to wait after page loading
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
        random_time = abs(np.random.normal(loc=self.seconds_to_sleep, scale=0.5 * self.seconds_to_sleep))
        time.sleep(random_time)

    def write_review(self, review, link):
        pass

    def write_text(self, review_field, review):
        action_chains = ActionChains(self.driver)  # initialize ActionChain object
        action_chains.click(review_field)
        for char in review:
            action_chains.send_keys(char)
            action_chains.perform()
            sleep_keyboard()

    def scroll_down(self, presses: int):
        pass
