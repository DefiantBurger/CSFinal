import os
import shutil
import json

print("loading version control")
with open('version_control.json', 'r') as f:
	versionControl = json.load(f)


def load_file_data(fileName: str):
	splitName = fileName.split("-")
	return {
		"firstName": splitName[0],
		"lastName": splitName[1],
		"assignmentID": splitName[2],
		"classSet": splitName[3]
	}


for inFile in os.listdir("input"):
	print("listing", inFile)
	if inFile.endswith(".jar"):
		print("extracting", inFile)
		fileName = inFile.removesuffix(".jar")

		data = load_file_data(fileName)
		
		version = 1
		if fileName in versionControl:
			version = versionControl[fileName] + 1
		versionControl[fileName] = version

		verFolderName = f"{fileName}-v{version}"

		if os.path.isdir('output/' + verFolderName):
			raise ValueError(f"Folder with version: ({version}) already exist")

		os.system(f'7z e input/{inFile} -ooutput/{verFolderName} > logs/{verFolderName}.txt')

		for extracted in os.listdir(f"output/{verFolderName}")[:]:
			if not extracted.endswith(".java"):
				os.remove(f"output/{verFolderName}/{extracted}")


print("saving version control")
with open('version_control.json', 'w') as f:
	json.dump(versionControl, f, indent=2)


print("done")