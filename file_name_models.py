import os
from config import Config


class FileNameModels:

    def __init__(self):
        self.target_dirs = Config().target_dir
        self.files = []

    def get_dirs_target_dir(self):
        dirs_with_models = os.scandir(self.target_dirs)

        with dirs_with_models as entries:
            collection_dirs = [entry for entry in entries if entry.is_dir()]

        return collection_dirs

    def get_files_from_target_dirs(self):
        for folder in self.get_dirs_target_dir():
            _files = [self.files.append(file.path) for file
                      in os.scandir(self.target_dirs +
                      f'{folder.name}') if file.is_file() and 'models' in file.name]
        return self.files

