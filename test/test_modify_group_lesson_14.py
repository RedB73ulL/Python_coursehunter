from model.group import Group

def test_modify_first_group_name(app):
  if app.group.count() == 0:
    app.group.create_group(Group(name="group"))
  app.group.modify_first_group(Group(name="Modify name"))

def test_modify_first_group_header(app):
  if app.group.count() == 0:
    app.group.create_group(Group(header="gh"))
  app.group.modify_first_group(Group(header="Modify header"))
