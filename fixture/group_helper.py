from selenium.webdriver.common.by import By



class GroupHelper:
    def __init__(self, app):
        self.app = app

    def return_to_groups_page(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "group page").click()

    def create_group(self, group):
        wd = self.app.wd
        self.open_create_group_page()
        # Fill group form
        wd.find_element(By.XPATH, "//div[@id='content']/form/input[4]").click()
        self.type("group_name", group.group_name)
        self.type("group_header", group.header)
        self.type("group_footer", group.footer)
        # SUBMIT GROUP CREATION
        wd.find_element(By.NAME, "submit").click()
        self.return_to_groups_page()

    def type(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element(By.NAME, field_name).clear()
            wd.find_element(By.NAME, field_name).click()
            wd.find_element(By.NAME, field_name).send_keys(text)

    def open_create_group_page(self):
        wd = self.app.wd
        # create_group
        wd.find_element(By.LINK_TEXT, "groups").click()


