import re

from file_name_models import FileNameModels


def search_relationship(file):
    pattern = re.compile('(?P<name>OneToOneField|ForeignKey|ManyToManyField)')
    result = pattern.findall(file)
    return result


class ReadFileModels(FileNameModels):

    def __init__(self):
        super().__init__()
        self.relationship = ['OneToOneField', 'ForeignKey', 'ManyToManyField']

    @staticmethod
    def generator_read_file(lists_files):
        return [open(file, 'r') for file in lists_files]

    @property
    def get_files_with_relationship(self):
        _files = self.generator_read_file(self.get_files_from_target_dirs())
        files_having_relationship_model = []
        for _file in _files:
            with _file as f:
                for field in search_relationship(f.read()):
                    if field in self.relationship:
                        files_having_relationship_model.append(f)

        return list(set(files_having_relationship_model))

    @property
    def get_relationship_line(self):
        files = self.generator_read_file(self.get_files_from_target_dirs())
        lines = []
        for file in files:
            with file as f:
                file_per_line_list = f.readlines()
                for line in file_per_line_list:
                    for relationship in self.relationship:
                        if relationship in line:
                            lines.append(line)
        return lines

