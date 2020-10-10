class Project(object):
    """
    This is the project generator class, it contains the basic parameters and methods in all type of projects
    """

    def __init__(self,project_type="rt-thread|@full|@4.0.2"):
        self.project_description = ""
        self.project_name = ''
        self.project_type = project_type
        self.builtin_files = []
        self.external_files = []

    def dump(self):
        return dict(
            project_description=self.project_description,
            project_name=self.project_name,
            project_type=self.project_type,
            builtin_files=self.builtin_files,
            external_files=self.external_files)
