import os
import shutil
import json
from classes.version_controller import VersionController
from classes.input_file import InputFile

versionController = VersionController("version_control.json")
versionControl = versionController.get()

inputFile = InputFile('input/joseph-cicalese-craps-7.jar')
print(inputFile.get_name())

versionController.update(versionControl)
