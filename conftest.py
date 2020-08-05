from fixture.application import Application
import pytest

# @ pytest.fixture - для pytest обозначает функцию, инициализирующую фикстуру
@pytest.fixture(scope="session")  # параметр для запуска фикстуры в кадом тесте/в сессии
def app(request):
  # инициализация фикстуры
  fixture = Application()
  # указание на то, как фикстура должна быть разрушена
  request.addfinalizer(fixture.destroy)
  return fixture
