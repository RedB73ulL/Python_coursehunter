from fixture.application import Application
import pytest

fixture = None

# @ pytest.fixture - для pytest обозначает функцию, инициализирующую фикстуру
@pytest.fixture #(scope="session")  # параметр для запуска фикстуры в кадом тесте/в сессии
def app(request):
  global fixture
  if fixture is None:
    # инициализация фикстуры
    fixture = Application()
  elif not fixture.is_valid():
    fixture = Application()
  fixture.session.ensure_login(username="admin", password="secret")
  return fixture

@pytest.fixture(scope="session", autouse=True)
def stop(request):
  def fin():
    fixture.session.ensure_logout()
    fixture.destroy()
  # указание на то, как фикстура должна быть разрушена
  request.addfinalizer(fin)
  return fixture
