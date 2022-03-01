import logging

from yandex_messenger import YandexMessenger

if __name__ == '__main__':
    # Create a custom logger
    logger = logging.getLogger()
    logger.setLevel('DEBUG')

    # Create handlers
    stdout_handler = logging.StreamHandler()

    stdout_handler.setLevel(logging.INFO)

    # Create formatters and add it to handlers
    logging_format = logging.Formatter('%(asctime)s - %(process)d - %(levelname)s - %(name)s - %(message)s')
    stdout_handler.setFormatter(logging_format)

    # Add handlers to the logger
    logger.addHandler(stdout_handler)

    yandex_messenger = YandexMessenger()
    logger.info("1. Browser window with Yandex.ru login page should be opened by now.")
    logger.info("2. Login (for example with your fake gmail account.")
    logger.info("3. In tNavigate to: https://yandex.ru/maps")
    logger.info("4. Navigate to random area in Russia")
    logger.info("5. Search for a venue type (for example `ресторан` for `restaurant`)")
    input("When done, press Enter to continue...")
    # yandex_messenger.driver.get('https://yandex.ru/maps')
    yandex_messenger.quit()
