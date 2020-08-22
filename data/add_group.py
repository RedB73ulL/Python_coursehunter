from model.group import Group
import random
import string

constant = [
    Group(name="name1", header="header1", footer="footer1"),
    Group(name="name2", header="header2", footer="footer2")
]

# генератор случайных строк
def random_string(prefix, maxlen):
  symbols = string.ascii_letters + string.digits + " " * 10
  return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [#[Group(name="", header="", footer="")] + [
  #Group(name=random_string("name", 20), header=random_string("header", 20), footer=random_string("footer", 20))
  #for i in range(5)
  Group(name=name, header=header, footer=footer)
  for name in ["", random_string("name", 20)]
  for header in ["", random_string("header", 20)]
  for footer in ["", random_string("footer", 20)]
]