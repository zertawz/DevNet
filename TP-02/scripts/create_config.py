import json
from jinja2 import Template, Environment,  FileSystemLoader

env = Environment(loader=FileSystemLoader("templates"))
#print(env.list_templates())

def load_json_data_from_file(file_path):
    with open(file_path, 'r') as variables:
        data = json.load(variables)
    return data

def render_network_config(template_name, data):
    template = env.get_template(template_name)
    return template.render(data)


def save_built_config(file_name, data):
    with open(file_name, 'w') as f:
        f.write(data)

def create_vlan_config_cpe_marseille():
    """
        Must return two values : router config and the switch config
    """
    r02_data = load_json_data_from_file(file_path='data/vlan_R02.json')
    esw2_data = load_json_data_from_file(file_path='data/vlan_ESW2.json')
    r02_config = render_network_config(template_name='vlan_router.j2', data=r02_data)
    esw2_config = render_network_config(template_name='vlan_switch.j2', data=esw2_data)
    return r02_config, esw2_config


def create_vlan_config_cpe_paris():
    """
        Must return two values : router config and the switch config
    """
    r03_data = load_json_data_from_file(file_path='data/vlan_R03.json')
    esw3_data = load_json_data_from_file(file_path='data/vlan_ESW3.json')
    r03_config = render_network_config(template_name='vlan_router.j2', data=r03_data)
    esw3_config = render_network_config(template_name='vlan_switch.j2', data=esw3_data)
    return r03_config, esw3_config


if __name__ == "__main__":
    """
        process question 1 to 5:
    """
    r02_config, esw2_config = create_vlan_config_cpe_marseille()
    save_built_config('config/vlan_R02.conf', r02_config)
    save_built_config('config/vlan_ESW2.conf', esw2_config)
    
    r03_config, esw3_config = create_vlan_config_cpe_paris()
    save_built_config('config/vlan_R03.conf', r03_config)
    save_built_config('config/vlan_ESW3.conf', esw3_config)
