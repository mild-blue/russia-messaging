from selenium.webdriver.common.by import By

from logger import logger
from settings import MESSAGE, PAGE_DOWN_PRESSES
from yandex_messenger import YandexMessenger

if __name__ == '__main__':
    yandex_messenger = YandexMessenger()
    logger.info("1. Browser window with Yandex.ru login page should be opened by now.")
    logger.info("2. Login (for example with your fake gmail account).")
    logger.info("3. Navigate to: https://yandex.ru/maps")
    logger.info("4. Navigate to random area in Russia")
    logger.info("5. Search for a venue type (for example `ресторан` for `restaurant`)")
    yandex_messenger.sleep()
    input("When done, press Enter to continue...")

    # Scroll to show more venues.
    yandex_messenger.scroll_down(PAGE_DOWN_PRESSES)

    venues = yandex_messenger.driver.find_elements(by=By.XPATH, value='//a[@class="search-snippet-view__link-overlay"]')
    venue_links = []
    for venue in venues:
        venue_links.append(venue.get_attribute('href'))
    logger.info(
        f'Going to review {len(venue_links)} venues. To increase or decrease this number, '
        f'modify the value of PAGE_DOWN_PRESSES in settings.py')
    for link in venue_links:
        yandex_messenger.driver.get(link)
        yandex_messenger.sleep()
        try:
            yandex_messenger.write_review(MESSAGE, link)
            logger.info(f'Successfully reviewed {link}')
        except:
            logger.exception(f'Unsuccessful for {link}')
    yandex_messenger.quit()
