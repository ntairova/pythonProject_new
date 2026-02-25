# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from model.contact import Contact


class TestCreateContact:
    # def setup_method(self):
    #     self.wd = webdriver.Chrome(
    #         service=Service(ChromeDriverManager().install())
    #     )
    #     self.wd.implicitly_wait(30)

    def test_create_new_contact(self):
        self.open_home_page()
        self.app.login()
        self.open_new_contact_page()
        self.fill_contact_form(Contact("fnm", "mn", "lnm", "nick", "title_test", "company", "test_address", "54321545",
                               '1111111', "98765432", "2", "test@test.com", "test2@test.com", "test3@test.com",
                               "test.com", "1", "March", "2000", "1", "March", "2001"))
        self.return_to_home_page(wd)
        self.logout(wd)

    # def logout(self, wd):
    #     wd.find_element(By.LINK_TEXT, "Logout").click()

    def return_to_home_page(self, wd):
        wd.find_element(By.LINK_TEXT, "home page").click()
        wd.get("http://localhost/addressbook/index.php")

    def fill_contact_form(self, wd, contact):
        print(contact)
        # FILL CONTACT FORM
        wd.find_element(By.NAME, "firstname").click()
        wd.find_element(By.NAME, "firstname").clear()
        wd.find_element(By.NAME, "firstname").send_keys(contact.firstname)
        wd.find_element(By.NAME, "middlename").click()
      #  wd.find_element(By.NAME, "theform").click()
        wd.find_element(By.NAME, "middlename").clear()
        wd.find_element(By.NAME, "middlename").send_keys(contact.middlename)
        #wd.find_element(By.NAME, "theform").click()
        wd.find_element(By.NAME, "lastname").click()
        wd.find_element(By.NAME, "lastname").clear()
        wd.find_element(By.NAME, "lastname").send_keys(contact.lastname)
        wd.find_element(By.NAME, "nickname").click()
        wd.find_element(By.NAME, "nickname").clear()
        wd.find_element(By.NAME, "nickname").send_keys(contact.nickname)
        wd.find_element(By.NAME, "title").click()
        wd.find_element(By.NAME, "title").clear()
        wd.find_element(By.NAME, "title").send_keys(contact.title)
        wd.find_element(By.NAME, "company").click()
        wd.find_element(By.NAME, "company").clear()
        wd.find_element(By.NAME, "company").send_keys(contact.company)
        wd.find_element(By.NAME, "address").click()
        wd.find_element(By.NAME, "address").clear()
        wd.find_element(By.NAME, "address").send_keys(contact.address)
        wd.find_element(By.NAME, "home").click()
        wd.find_element(By.NAME, "home").clear()
        wd.find_element(By.NAME, "home").send_keys(contact.home)
        wd.find_element(By.NAME, "mobile").click()
        wd.find_element(By.NAME, "mobile").clear()
        wd.find_element(By.NAME, "mobile").send_keys(contact.mobile)
        wd.find_element(By.NAME, "work").click()
        wd.find_element(By.NAME, "work").clear()
        wd.find_element(By.NAME, "work").send_keys(contact.work)
        wd.find_element(By.NAME, "fax").click()
        wd.find_element(By.NAME, "fax").clear()
        wd.find_element(By.NAME, "fax").send_keys(contact.fax)
        # wd.find_element_by_xpath("//div[@id='content']/form/label[13]").click()
        wd.find_element(By.NAME, "email").click()
        wd.find_element(By.NAME, "email").clear()
        wd.find_element(By.NAME, "email").send_keys(contact.email)
        wd.find_element(By.NAME, "email2").click()
        wd.find_element(By.NAME, "email2").clear()
        wd.find_element(By.NAME, "email2").send_keys(contact.email2)
        wd.find_element(By.NAME, "email3").click()
        wd.find_element(By.NAME, "email3").clear()
        wd.find_element(By.NAME, "email3").send_keys(contact.email3)
        wd.find_element(By.NAME, "homepage").click()
        wd.find_element(By.NAME, "homepage").clear()
        wd.find_element(By.NAME, "homepage").send_keys(contact.homepage)
        wd.find_element(By.NAME, "bday").click()
        Select(wd.find_element(By.NAME, "bday")).select_by_visible_text(contact.bday)
        wd.find_element(By.NAME, "bmonth").click()
        Select(wd.find_element(By.NAME, "bmonth")).select_by_visible_text(contact.bmonth)
      #   wd.find_element(By.NAME, "byear").click()
      #   wd.find_element(By.NAME, "byear").clear()
      #   wd.find_element(By.NAME, "byear").send_keys(contact.byear)
      #   wd.find_element(By.NAME, "aday").click()
      #   Select(wd.find_element(By.NAME, "aday")).select_by_visible_text(contact.aday)
      #   wd.find_element(By.NAME, "amonth").click()
      #   Select(wd.find_element(By.NAME, "amonth")).select_by_visible_text(contact.amonth)
      #   wd.find_element(By.NAME, "ayear").click()
      #   wd.find_element(By.NAME, "ayear").clear()
      #   wd.find_element(By.NAME, "ayear").send_keys(contact.ayear)
        wd.find_element(By.NAME, "theform").click()
        wd.find_element(By.XPATH, "//div[@id='content']/form/input[20]").click()

    def open_new_contact_page(self, wd):
        wd.find_element(By.LINK_TEXT, "add new").click()
        wd.get("http://localhost/addressbook/edit.php")


    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/group.php")

    def tearDown(self):
        self.wd.quit()


