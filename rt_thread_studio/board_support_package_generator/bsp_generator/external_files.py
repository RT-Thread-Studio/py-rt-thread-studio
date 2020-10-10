class ExternalFiles(object):
    """
    This is the project generator class, it contains the basic parameters and methods in all type of projects
    """
    def __init__(self):
        self.package_type = "",
        self.package_vendor = "",
        self.package_name = "",
        self.package_version = "",
        self.source_path_offset = "",
        self.target_path_offset = "",
        self.files_and_folders = list()

    def dump(self):
        return dict(
            package_type=self.package_type,
            package_vendor=self.package_vendor,
            package_name=self.package_name,
            package_version=self.package_version,
            source_path_offset=self.source_path_offset,
            target_path_offset=self.target_path_offset,
            files_and_folders=self.files_and_folders)
