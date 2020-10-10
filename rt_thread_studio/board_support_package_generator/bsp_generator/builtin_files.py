class BuiltinFiles(object):
    """
    This is the project generator class, it contains the basic parameters and methods in all type of projects
    """

    def __init__(self):
        self.source_path_offset = "",
        self.target_path_offset = "",
        self.files_and_folders = list()

    def dump(self):
        return dict(source_path_offset=self.source_path_offset,
                    target_path_offset=self.target_path_offset,
                    files_and_folders=self.files_and_folders)
