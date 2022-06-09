from classes.file import File
import os

class InputFile(File):
    def load(self, output_path: str, version_control: dict) -> dict:
        version = 1
        name = self.get_name()
        if name in version_control:
            version = version_control[name] + 1
        version_control[name] = version

        verFolderName = f"{name}-v{version}"

        if os.path.isdir(f"output/{verFolderName}"):
            raise ValueError(f"Folder with version: ({version}) already exist")
        else:
            os.mkdir(f"output/{verFolderName}")

        os.system(f"cd output/{verFolderName} \
			&& jar xvf ../../{self.path} > ../../logs/{verFolderName}.txt")

        return version_control