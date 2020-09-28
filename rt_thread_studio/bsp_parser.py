import json
import logging
import os
from pathlib import Path
from string import Template

import yaml


class BspParser(object):
    """
    This is the project generator class, it contains the basic parameters and methods in all type of projects
    """

    def __init__(self,
                 bsp_path):
        self.bsp_path = Path(bsp_path)
        self.pack_dict = None
        self.selected_project_dict = None
        self.__dsc2dict()
        self.all_projects = []
        self.select_all_project()

    def select_all_project(self):

        self.all_projects = self.template_projects + self.example_projects

        return True

    def __dsc2dict(self):
        desc_file_path = None
        for file in os.listdir(self.bsp_path):
            if ".yaml" in file:
                desc_file_path = file
                with open(self.bsp_path.joinpath(desc_file_path), mode='r', encoding="utf-8") as f:
                    data = f.read()
                self.pack_dict = yaml.load(data, Loader=yaml.FullLoader)
                break
        if not desc_file_path:
            for file in os.listdir(self.bsp_path):
                if ".json" in file:
                    desc_file_path = file
                    with open(self.bsp_path.joinpath(desc_file_path), mode='r', encoding="utf-8") as f:
                        data = f.read()
                    self.pack_dict = json.loads(data)
                    break
        if self.pack_dict:
            # bsp version <3 ,template_projects is named default_projects
            if "template_projects" in self.pack_dict.keys():
                self.template_projects = self.pack_dict["template_projects"]
            else:
                self.template_projects = self.pack_dict["default_projects"]
            self.example_projects = self.pack_dict["example_projects"]
        else:
            return False
        return True

    @staticmethod
    def get_builtin_file_from_project(project):
        internal_files_folders_list = []
        try:
            builtin_files_dict_list = project["builtin_files"]
            for builtin_files_dict in builtin_files_dict_list:
                source_path_offset = builtin_files_dict["source_path_offset"]
                for item in builtin_files_dict["files_and_folders"]:
                    internal_files_folders_list.append(Path(source_path_offset).joinpath(item))
            return internal_files_folders_list
        except Exception as e:
            logging.error("BSP parser error:{0}".format(e))
            return []

    def get_external_package_list(self):
        external_packages_dict_list = []
        package_relative_path_list = []
        for project in self.all_projects:
            external_files = project["external_files"]
            for external_file in external_files:
                package_type = external_file["package_type"]
                package_name = external_file["package_name"]
                package_vendor = external_file["package_vendor"]
                package_version = external_file["package_version"]
                package_relative_path = Path(package_type).joinpath(package_vendor, package_name, package_version)
                if package_relative_path not in package_relative_path_list:
                    package_relative_path_list.append(package_relative_path)
                    external_packages_dict_list.append(dict(
                        {'package_type': package_type,
                         'package_name': package_name,
                         'package_vendor': package_vendor,
                         'package_version': package_version,
                         'package_relative_path': str(package_relative_path.as_posix())}))
                else:
                    continue
        return external_packages_dict_list

    def generate_bsp_project_create_json_input(self, output_project_path):
        bsp_test_dict = dict()
        para_json_tmp_str = """{
	"parameter": {
		"bsp_path": "$bsp_path",
		"project_name": "$project_name",
		"output_project_path": "$output_project_path",
		"from_example": $from_example,
		"example_name": "$example_name",
		"project_type": "$project_type",
		"action": "create_project"
	}
}"""
        for project in self.template_projects:
            project_name = "template_" + project["project_type"].replace("|@", "_").replace("-", "_").replace(".", "_")
            para_json_tmp = Template(para_json_tmp_str)
            wstrs = para_json_tmp.substitute(bsp_path=str(Path(self.bsp_path).as_posix()),
                                             project_type=str(project['project_type']),
                                             project_name=str(project_name),
                                             output_project_path=str(output_project_path),
                                             from_example="false",
                                             example_name="")
            dict_lit = json.loads(wstrs)
            bsp_test_dict[project_name] = dict_lit
        for project in self.example_projects:
            project_name = "example_" \
                           + project["project_name"] \
                           + "_" \
                           + project["project_type"].replace("|@", "_").replace("-", "_").replace(".", "_")
            para_json_tmp = Template(para_json_tmp_str)
            wstrs = para_json_tmp.substitute(bsp_path=str(Path(self.bsp_path).as_posix()),
                                             project_type=str(project['project_type']),
                                             project_name=str(project_name),
                                             output_project_path=str(output_project_path),
                                             from_example="true",
                                             example_name=project["project_name"])
            dict_lit = json.loads(wstrs)
            bsp_test_dict[project_name] = dict_lit
        return bsp_test_dict


if __name__ == "__main__":
    # bsp_path = "C:\\Users\\yaxing.chen\\Documents\\sdk\\sdk-bsp\\sdk-bsp-stm32l475-atk-pandora"
    bsp_path = "C:\\Users\\yaxing.chen\\Documents\\sdk\\sdk-bsp\\sdk-bsp-stm32h750-realthread-artpi"
    bsp_parser = BspParser(bsp_path)
    print(bsp_parser.get_external_package_list())
    print(bsp_parser.generate_bsp_project_create_json_input("."))
