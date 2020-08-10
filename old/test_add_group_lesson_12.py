from model.group import Group

def test_add_group(app):
  app.group.create_group(Group(name="group", header="gh", footer="gf"))

def test_add_empty_group(app):
  app.group.create_group(Group(name="", header="", footer=""))
