from model.group import Group

def test_modify_first_group_name(app):
  app.group.modify_first_group(Group(name="Modify name"))

def test_modify_first_group_header(app):
  app.group.modify_first_group(Group(header="Modify header"))
