from model.group import Group
from fixture.application import Application
import pytest

# @ pytest.fixture - для pytest обозначает функцию, инициализирующую фикстуру
@pytest.fixture
def app(request):
  # инициализация фикстуры
  fixture = Application()
  # указание на то, как фикстура должна быть разрушена
  request.addfinalizer(fixture.destroy)
  return fixture

def test_add_group(app):
  app.session.login(username="admin", password="secret")
  app.group.create_group(Group(name="group", header="gh", footer="gf"))
  app.session.logout()

def test_add_empty_group(app):
  app.session.login(username="admin", password="secret")
  app.group.create_group(Group(name="", header="", footer=""))
  app.session.logout()
