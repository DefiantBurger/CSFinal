import os
import shutil
import json
from version_controller import VersionController

versionController = VersionController("version_control.json")
print(versionController.get())