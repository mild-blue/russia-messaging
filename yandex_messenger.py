from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

from messenger import Messenger


class YandexMessenger(Messenger):
    url: str

    def __init__(self):
        Messenger.__init__(self, 'https://passport.yandex.ru/auth')

    def write_review(self, review):
        # go to reviews
        xpath = '//div[@class="tabs-select-view__title _name_reviews"]'
        self.driver.find_element(by=By.XPATH, value=xpath).click()
        self.sleep()

        # Give stars. All stars seem the same, this should click the first available, i.e. 1 star rating.
        xpath = '//div[@class="business-rating-edit-view__star _size_s _wide"]'
        self.driver.find_elements(by=By.XPATH, value=xpath)[4].click()
        self.sleep()

        # Write your message.
        xpath = '//textarea[@class="textarea__control"]'
        review_field = self.driver.find_element(by=By.XPATH, value=xpath)
        self.write_text(review_field, review)
        self.sleep()

        # Submit.
        xpath = '//div[@class="business-review-form__controls"]//button[@class="button _view_primary _ui _size_medium"]'
        self.driver.find_element(by=By.XPATH, value=xpath).click()
        self.sleep()

        # Click ok.
        xpath = '//div[@class="business-review-dialog-form__gratitude"]//button'
        self.driver.find_element(by=By.XPATH, value=xpath).click()

        # Wait for a while before continuing (yes, this can be prettier, but to lazy).
        self.sleep()
        self.sleep()
        self.sleep()
        self.sleep()

    def scroll_down(self, presses: int):
        list_element = self.driver.find_element(by=By.XPATH,
                                                value='//div[@class="search-list-view__quarantine-warning"]')
        action_chains = ActionChains(self.driver)  # initialize ActionChain object
        action_chains.click(list_element)
        i = 0
        while i < presses:
            action_chains.send_keys(Keys.PAGE_DOWN)
            action_chains.perform()
            self.sleep()
            i = i + 1
