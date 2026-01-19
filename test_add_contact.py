# -*- coding: utf-8 -*-
import pytest

from application import Application
from contact import Contact

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_untitled_test_case(app):
    app.login("admin", "secret")
    app.add_new_contact(Contact("test_first", "middle_test", "last_test", "nicknm_test", "title_test", "comp_test",
                         "address_test", "123456456", "mob_test", "work_test", "fax", "nelya.tairova@gmail.com",
                         "nelya.tairova@gmail.com", "nelya.tairova@gmail.com", "http://tewretest.com", "3",
                         "January", "1988", "1", "February", "2001"))
    app.logout()





