from selenium.webdriver.common.by import By


class OrderPageLocations:

    HEADER_ORDER_BUTTON = (By.XPATH, "//div[contains(@class, 'Header_Nav')]/button[contains(text(), 'Заказать')]")
    DOWN_ORDER_BUTTON = [By.XPATH, "//*[contains(@class, 'Button_Middle')]"]
    HEADER_ORDER_PAGE = [By.XPATH, "//div[contains(text(), 'Для кого самокат')]"]
    INPUT_NAME = (By.XPATH, "//input[@placeholder = '* Имя']")
    INPUT_SURNAME = [By.XPATH, "//input[@placeholder = '* Фамилия']"]
    INPUT_ADDRESS = [By.XPATH, "//input[@placeholder = '* Адрес: куда привезти заказ']"]
    INPUT_STATION = [By.XPATH, "//input[@placeholder = '* Станция метро']"]
    STATION_LIST = [By.XPATH, "//div[@class = 'select-search__select']"]
    INPUT_PHONE = [By.XPATH, "//input[@placeholder = '* Телефон: на него позвонит курьер']"]
    NEXT_BUTTON = [By.XPATH, "//button[contains(text(), 'Далее')]"]
    HEADER_RENT_PAGE = [By.XPATH, "//div[contains(text(), 'Про аренду')]"]
    INPUT_DATE_DELIVERY = [By.XPATH, "//input[@placeholder = '* Когда привезти самокат']"]
    DAY_TEXT = [By.XPATH, '//div[contains(text(), "25")]']
    INPUT_RENTAL_TIME = [By.XPATH, "//div[contains(text(), '* Срок аренды')]"]
    RENTAL_TIME = [By.XPATH, "//*[contains(text(), 'сутки')]"]
    CHECK_BOX_COLOR = [By.XPATH, "//label[contains(text(), 'чёрный жемчуг')]"]
    INPUT_COMMENT = [By.XPATH, "//input[@placeholder = 'Комментарий для курьера']"]
    FINISH_ORDER_BUTTON = [By.XPATH, "//div[contains(@class, 'Order_Buttons')]/button[contains(text(), 'Заказать')]"]
    AGREE_BUTTON = [By.XPATH, "//button[contains(text(), 'Да')]"]
    CHECK_ORDER = [By.XPATH, "//button[contains(text(), 'Посмотреть статус')]"]
