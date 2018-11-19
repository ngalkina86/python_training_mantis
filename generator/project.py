import json
from model.project import Project
import random
import string
import os.path
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of projects", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/project.json"

for o,a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix,maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + ""*10
    return prefix + "".join([random.choice(symbols) for i in range (random.randrange(maxlen))])


testdata =[
    Project(name=random_string("name",10), description=random_string("description",10),status = random_string("status",10),
       inherit_global = random_string("inherit_global",10),view_state = random_string("view_state",10))
    for i in range(n)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file,"w") as f:
    f.write(json.dumps(testdata,default = lambda x: x.__dict__,indent = 2))