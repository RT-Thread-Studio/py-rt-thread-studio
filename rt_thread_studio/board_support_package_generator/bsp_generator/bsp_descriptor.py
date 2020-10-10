import yaml
from . import chip
from . import board

class BspDescriptor(object):
    """
    This is the project generator class, it contains the basic parameters and methods in all type of projects
    """

    def __init__(self):
        self.pkg_type = "Board_Support_Packages"
        self.pkg_vendor = "RealThread"
        self.pkg_version = "0.1.1"
        self.yaml_version = 3
        self.features = []
        self.features_zh = []
        self.docs = []
        self.board = board.Board()
        self.chip = chip.Chip()
        self.template_projects = []
        self.example_projects = []

    def load(self, template_file_path):
        with open(template_file_path, mode='r', encoding="utf-8") as f:
            data = f.read()
        pack_dict = yaml.load(data, Loader=yaml.FullLoader)

        self.pkg_type = pack_dict["pkg_type"]
        self.pkg_vendor = pack_dict["pkg_vendor"]
        self.pkg_version = pack_dict["pkg_version"]
        self.yaml_version = pack_dict["yaml_version"]
        self.features = pack_dict["features"]
        self.features_zh = pack_dict["features_zh"]
        self.docs = pack_dict["docs"]
        self.board.load(pack_dict["board"])
        self.chip.load(pack_dict["chip"])
        self.template_projects = pack_dict["template_projects"]
        self.example_projects = pack_dict["example_projects"]

        return True

    def dump(self, file):
        pack_dict = dict()
        pack_dict["pkg_type"] = self.pkg_type
        pack_dict["pkg_vendor"] = self.pkg_vendor
        pack_dict["pkg_version"] = self.pkg_version
        pack_dict["yaml_version"] = self.yaml_version
        pack_dict["features"] = self.features
        pack_dict["features_zh"] = self.features
        pack_dict["docs"] = self.docs
        pack_dict["board"] = self.board.dump()
        pack_dict["chip"] = self.chip.dump()
        pack_dict["template_projects"] = self.template_projects
        pack_dict["example_projects"] = self.example_projects
        with open(file, mode='w', encoding='utf-8') as f:
            yaml.Dumper.ignore_aliases = lambda *args : True
            yaml.dump(pack_dict, f, allow_unicode=True,default_flow_style=False)
