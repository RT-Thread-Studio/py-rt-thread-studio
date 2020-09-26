from pathlib import Path

from . import bsp_parser


class BspChecker(object):

    def __init__(self,
                 bsp_location):
        self.bsp_path = Path(bsp_location)
        self.series_dict = None
        self.pack_dict = None
        self.current_location = None
        self.parser = bsp_parser.BspParser(bsp_location)

    def check_built_in_files(self):
        for project in self.parser.all_projects:
            project_name = project["project_name"]
            self.current_location = "project_name: " + project_name
            built_in_files_list = self.parser.get_builtin_file_from_project(project)
            if self.is_file_exist_in_bsp(built_in_files_list):
                pass
            else:
                return False
        return True

    def check(self):
        return self.check_built_in_files()

    def is_file_exist_in_bsp(self, files):
        for file in files:
            if file != "none":
                file_path = self.bsp_path.joinpath(file)
                if str(file_path).endswith("*"):
                    if file_path.parent.exists():
                        pass
                    else:
                        return False
                elif not file_path.exists():
                    print("ERROR @ : " + str(self.current_location))
                    print("file '{0}' is not found in package".format(file))
                    return False
                else:
                    pass
        return True


if __name__ == "__main__":
    bsp_path = "C:\\RT-ThreadStudio111full\\repo\\Local\\Board_Support_Packages\\RealThread\\STM32H750-ART-Pi\\0.3.0"
    bsp_checker = BspChecker(bsp_path)
    bsp_checker.check()
