
from pages.base_pages import BasePage


class OrderPage(BasePage):

    def set_order(self, name, name_locator, surname, surname_locator, address, address_locator, station,
                  station_locator, number_phone, number_phone_locator, station_list_locator, button_next,
                  date, date_locator, day_locator, days, days_locator, color_locator, comment, comment_locator,
                  final_order_button, agree_order_locator):
        self.input_text_to_element(name_locator, name)
        self.input_text_to_element(surname_locator, surname)
        self.input_text_to_element(address_locator, address)
        self.input_text_to_element(station_locator, station)
        self.click_element(station_list_locator)
        self.input_text_to_element(number_phone_locator, number_phone)
        self.click_element(button_next)
        self.input_text_to_element(date_locator, date)
        self.click_element(day_locator)
        self.click_element(days)
        self.click_element(days_locator)
        self.click_element(color_locator)
        self.input_text_to_element(comment_locator, comment)
        self.click_element(final_order_button)
        self.click_element(agree_order_locator)

