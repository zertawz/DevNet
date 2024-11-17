import json
from jinja2 import Template, Environment, FileSystemLoader

#ALlow us not to precise each time the folder were the template is stored.
env = Environment(loader=FileSystemLoader("templates"))

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


if __name__ == "__main__":
    #Verify if jinja is able to see the templates
    #print(env.list_templates())

    #process R2
    r2_data = load_json_data_from_file(file_path='data/R2.json')
    r2_config = render_network_config(template_name='R2.j2', data=r2_data)
    save_built_config('config/R2.conf', r2_config)

    #process ESW2
    esw2_data = load_json_data_from_file(file_path='data/ESW2.json')
    esw2_config = render_network_config(template_name='ESW2.j2', data=esw2_data)
    save_built_config('config/ESW2.conf', esw2_config)