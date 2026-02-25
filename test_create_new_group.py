
from fixture.application import Application
from model.group import Group
import pytest


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_create_new_group(app):
    app.session.login("admin", "secret")
    app.group.create_group(Group("test_first_group_name", "test_header", "test_footer"))
    app.session.logout()

def test_create_new_empty_group(app):
    app.session.login("admin", "secret")
    app.group.create_group(Group("", "", ""))
    app.session.logout()

def test_create_new_group_without_footer(app):
    app.session.login("admin", "secret")
    app.group.create_group(Group('', ''))
    app.session.logout()


