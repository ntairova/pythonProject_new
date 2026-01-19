import pytest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException

import application
from group import Group
from application import Application

@pytest.fixture
def app(request):
    fixture=Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_group(app):
    app.login(password='secret', username = 'admin')
    app.create_group(Group("test_group", "test_header", "test_footer"))
    app.logout()

def test_add_empty_group(app):
    app.login(password='secret', username = 'admin')
    app.create_group(Group("", "", ""))
    app.logout()

