class HomePage():
    def __init__(self, driver):
        self.driver = driver
        self.welcome_link_id = 'welcome'
        self.logout_link_linkText = 'Logout'
        self.data_table = 'panel_resizable_1_1'

    def click_welcome(self):
        self.driver.find_element_by_id(self.welcome_link_id).click()

    def click_logout_link(self):
        self.driver.find_element_by_link_text(self.logout_link_linkText).click()

    def get_table_data(self):
        data = self.driver.find_element_by_id(self.data_table)
        print(data)
