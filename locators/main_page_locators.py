from selenium.webdriver.common.by import By


class MainPageLocators:
    SUBHEADER_FAQ = By.XPATH, "//div[text()='Вопросы о важном']"
    BUTTON_AGREE_COOKIE = (By.ID, 'rcc-confirm-button')
    QUESTION_LOCATOR = By.ID, "accordion__heading-{}"
    ANSWER_LOCATOR = By.ID, "accordion__panel-{}"
    HEADER_LOGO_SCOOTER = [By.XPATH, '//div[contains(@class, "Header_Logo")]/a[@href="/"]']
    HOME_PAGE_SCOOTER = [By.XPATH, "//div[contains(@class, 'Home_Header')]"]
    HEADER_LOGO_YANDEX = [By.XPATH, '//div[contains(@class, "Header_Logo")]/a[@href="//yandex.ru"]']
    YANDEX_DZEN_PAGE = [By.XPATH, '//div[text() = "Удобный и быстрый Яндекс Браузер"]']



