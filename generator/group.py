from model.group import Group
import random
import string
import os.path
import jsonpickle
import getopt
import sys

try:
  opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
  getopt.usage()
  sys.exit(2)

n = 5
out = "data/groups.json"

for o, a in opts:
  if o == "-n":
    n = int(a)
  elif o == "-f":
    out = a

# генератор случайных строк
def random_string(prefix, maxlen):
  symbols = string.ascii_letters + string.digits + " " * 10
  return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [#[Group(name="", header="", footer="")] + [
  #Group(name=random_string("name", 20), header=random_string("header", 20), footer=random_string("footer", 20))
  #for i in range(n)
  Group(name=name, header=header, footer=footer)
  for name in ["", random_string("name", 20)]
  for header in ["", random_string("header", 20)]
  for footer in ["", random_string("footer", 20)]
]

# прикрепляем путь к джейсону(определяем дерикторию в которой файл находится(преобразуем путь в абсолютн(__file__)))
file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", out)

with open(file, "w") as out:
  jsonpickle.set_encoder_options("json", indent=2)
  out.write(jsonpickle.encode(testdata))
