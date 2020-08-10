from model.group import Group

def test_delete_first_group(app):
  if app.group.count() == 0:
    app.group.create_group(Group(name="group", header="gh", footer="gf"))
  app.group.delete_first_group()
