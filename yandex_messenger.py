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
        self.driver.find_element(by=By.XPATH, value=xpath).click()
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
        xpath = '//div[@class="business-review-dialog-form__gratitude"]//button'
        self.driver.find_element(by=By.XPATH, value=xpath).click()
        # Wait about a minute before continuing (yes, this can be prettier, but to lazy).
        # self.sleep()
        # self.sleep()
        # self.sleep()
        # self.sleep()
