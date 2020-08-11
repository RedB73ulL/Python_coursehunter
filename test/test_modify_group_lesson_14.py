from model.group import Group

def test_modify_first_group_name(app):
  if app.group.count() == 0:
    app.group.create_group(Group(name="group"))
  old_groups = app.group.get_group_list()
  app.group.modify_first_group(Group(name="Modify name"))
  new_groups = app.group.get_group_list()
  assert len(old_groups) == len(new_groups)

def test_modify_first_group_header(app):
  if app.group.count() == 0:
    app.group.create_group(Group(header="gh"))
  old_groups = app.group.get_group_list()
  app.group.modify_first_group(Group(header="Modify header"))
  new_groups = app.group.get_group_list()
  assert len(old_groups) == len(new_groups)