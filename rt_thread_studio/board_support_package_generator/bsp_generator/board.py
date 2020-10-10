class Board(object):
    """
    This is the project generator class, it contains the basic parameters and methods in all type of projects
    """

    def __init__(self):
        self.name = ""
        self.version = ""
        self.vendor = ""
        self.description_zh = ""
        self.description_en = ""
        self.small_image = ""
        self.large_image = ""
        self.sale_contact_cn = ""
        self.sale_contact_global = ""
        self.buy_url_cn = " "
        self.buy_url_global = ""
        self.price_cn = ""
        self.price_global = ""
        self.debugger = ""
        self.debug_interface = ""
        self.emulator_machine = ''

    def dump(self):
        return dict(
            name=self.name,
            version=self.version,
            vendor=self.vendor,
            description_zh=self.description_zh,
            description_en=self.description_en,
            small_image=self.small_image,
            large_image=self.large_image,
            sale_contact_cn=self.sale_contact_cn,
            sale_contact_global=self.sale_contact_global,
            buy_url_cn=self.buy_url_cn,
            buy_url_global=self.buy_url_global,
            price_cn=self.price_cn,
            price_global = self.price_global,
            debugger = self.debugger,
            debug_interface =self.debug_interface,
            emulator_machine = self.emulator_machine)

    def load(self, dict_in):
        self.name = dict_in["name"]
        self.version = dict_in["version"]
        self.vendor = dict_in["vendor"]
        self.description_zh = dict_in["description_zh"]
        self.description_en = dict_in["description_en"]
        self.small_image = dict_in["small_image"]
        self.large_image = dict_in["large_image"]
        self.sale_contact_cn = dict_in["sale_contact_cn"]
        self.sale_contact_global = dict_in["sale_contact_global"]
        self.buy_url_cn = dict_in["buy_url_cn"]
        self.buy_url_global = dict_in["buy_url_global"]
        self.price_cn = dict_in["price_cn"]
        self.price_global = dict_in["price_global"]
        self.debugger = dict_in["debugger"]
        self.debug_interface = dict_in["debug_interface"]
        self.emulator_machine = dict_in["emulator_machine"]
