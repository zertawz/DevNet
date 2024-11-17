import json
from jinja2 import Template, Environment,  FileSystemLoader

env = Environment(loader=FileSystemLoader("templates"))

def load_json_data_from_file(file_path):
    pass

def render_network_config(template_name, data):
    pass


def save_built_config(file_name, data):
    pass


def create_vlan_config_cpe_marseille():
    """
        Must return two values : router config and the switch config
    """
    pass


def create_vlan_config_cpe_paris():
    """
        Must return two values : router config and the switch config
    """
    pass


if __name__ == "__main__":
    """
        process question 1 to 5:
    """
    # r02_config, esw2_config = create_vlan_config_cpe_marseille()
    # save_built_config('config/vlan_R02.conf', r02_config)
    # save_built_config('config/vlan_ESW2.conf', esw2_config)
    
    # r03_config, esw3_config = create_vlan_config_cpe_paris()
    # save_built_config('config/vlan_R03.conf', r03_config)
    # save_built_config('config/vlan_ESW3.conf', esw3_config)
