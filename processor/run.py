import os
import shutil
import json
from classes.version_controller import VersionController
from classes.input_file import InputFile

versionController = VersionController("version_control.json")
versionControl = versionController.get()

inputFile = InputFile("input/test-person-validator-3.jar")
versionControl = inputFile.load("output", versionControl)

versionController.update(versionControl)
