class Chip(object):
    """
    This is the project generator class, it contains the basic parameters and methods in all type of projects
    """

    def __init__(self):
        self.device_vendor = ""
        self.family_name = ""
        self.series_name = ""
        self.sub_series_name = ""
        self.chip_name = ""
        self.rx_name = ""
        self.tx_name = ""
        self.clock_source = ""
        self.source_freq = ''
        self.target_freq = ''
        self.uart_name = ""

    def dump(self):
        return dict(
            device_vendor=self.device_vendor,
            family_name=self.family_name,
            series_name=self.series_name,
            sub_series_name=self.sub_series_name,
            chip_name=self.chip_name,
            rx_name=self.rx_name,
            tx_name=self.tx_name,
            clock_source=self.clock_source,
            source_freq=self.source_freq,
            target_freq=self.target_freq,
            uart_name=self.uart_name)

    def load(self, dict_in):
        self.device_vendor = dict_in["device_vendor"]
        self.family_name = dict_in["family_name"]
        self.series_name = dict_in["series_name"]
        self.sub_series_name = dict_in["sub_series_name"]
        self.chip_name = dict_in["chip_name"]
        self.rx_name = dict_in["rx_name"]
        self.tx_name = dict_in["tx_name"]
        self.clock_source = dict_in["clock_source"]
        self.source_freq = dict_in["source_freq"]
        self.target_freq = dict_in["target_freq"]
        self.uart_name = dict_in["uart_name"]
