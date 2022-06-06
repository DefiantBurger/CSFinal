import os

folders = ["input/", "logs/", "output/"]
for f in folders:
    if not os.path.isdir(f):
        os.mkdir(f)

with open("version_control.json", "x") as f:
    f.write("{}")