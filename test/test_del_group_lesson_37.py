from model.group import Group
import random

def test_delete_some_group(app, db, check_ui):
  if len(db.get_group_list()) == 0:
    app.group.create_group(Group(name="group", header="gh", footer="gf"))
  old_groups = db.get_group_list()
  group = random.choice(old_groups)
  app.group.delete_group_by_id(group.id)
  new_groups = db.get_group_list()
  assert len(old_groups) - 1 == len(new_groups)
  old_groups.remove(group)
  assert old_groups == new_groups
  if check_ui:
    #с clean - это моя самодеятельность, ибо в уроке вроде как сравниваются разные списки. В ui нету хедера и футера как в бд
    def clean(group):
        return Group(id=group.id, name=group.name.strip())
    assert sorted(map(clean, new_groups), key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
