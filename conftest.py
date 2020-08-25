from fixture.application import Application
import pytest
import json
import os.path
import importlib
import jsonpickle
from fixture.db import DbFixture

fixture = None
target = None

#34
def load_config(file):
  global target
  if target is None:
    # прикрепляем путь к джейсону(определяем дерикторию в которой файл находится(преобразуем путь в абсолютн(__file__)))
    config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
    with open(config_file) as f:
      target = json.load(f)
  return target

# @ pytest.fixture - для pytest обозначает функцию, инициализирующую фикстуру
@pytest.fixture #(scope="session")  # параметр для запуска фикстуры в кадом тесте/в сессии
def app(request):
  global fixture
  browser = request.config.getoption("--browser")
  #34
  web_config = load_config(request.config.getoption("--target"))["web"]
  if fixture is None or not fixture.is_valid():
    # инициализация фикстуры
    fixture = Application(browser=browser, base_url=web_config['baseUrl'])
  fixture.session.ensure_login(username=web_config['username'], password=web_config['password'])
  return fixture

@pytest.fixture(scope="session", autouse=True)
def stop(request):
  def fin():
    fixture.session.ensure_logout()
    fixture.destroy()
  # указание на то, как фикстура должна быть разрушена
  request.addfinalizer(fin)
  return fixture

# функция для добавления собственных параметров запуска тестов
def pytest_addoption(parser):
  parser.addoption("--browser", action="store", default="chrome")
  parser.addoption("--target", action="store", default="target.json")

# 31
def pytest_generate_tests(metafunc):
  for fixture in metafunc.fixturenames:
    if fixture.startswith("data_"):
      testdata = load_form_module(fixture[5:])
      metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])
# 32
    elif fixture.startswith("json_"):
      testdata = load_form_json(fixture[5:])
      metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])

#31
def load_form_module(module):
  return importlib.import_module("data.%s" % module).testdata

#32
def load_form_json(file):
  with open (os.path.join(os.path.dirname(os.path.abspath(__file__)), "data/%s.json" % file)) as f:
    return jsonpickle.decode(f.read())

#34
@pytest.fixture(scope="session")
def db(request):
  db_config = load_config(request.config.getoption("--target"))["db"]
  dbfixture = DbFixture(host=db_config["host"], name=db_config["name"], user=db_config["user"], password=db_config["password"])
  def fin():
    dbfixture.destroy()
  request.addfinalizer(fin)
  return dbfixture
