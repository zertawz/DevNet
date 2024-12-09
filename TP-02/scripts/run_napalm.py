import json
from napalm import get_network_driver
from jinja2 import Template, Environment,  FileSystemLoader

env = Environment(loader=FileSystemLoader("templates"))

def get_inventory():
    pass


def get_json_data_from_file(file):
    pass

def question_26(device):
    commands = ['show ip int brief']
    output = device.cli(commands)
    print(output)


def question_27(device):
    pass


def question_28(device):
    output = device.get_arp_table()
    print(output)

def question_29(device):
    pass


def question_30(device):
    device.load_merge_candidate(filename="config/loopback_R01_napalm.conf")
    print(device.compare_config())
    #apply the changes
    device.commit_config()
    command = ["show ip int brief"]
    output = device.cli(command)
    print(output["show ip int brief"])

def question_31():
    with open("data/ospf.json", 'r') as variables:
        data = json.load(variables)
        variables.close()
    template = env.get_template("ospf.j2")
    for router in data:
        conf = template.render(router)
        with open(f"config/ospf_{router["hostname"].lower()}.conf", 'w') as f:
            f.write(conf)
            f.close()




def question_32():
    with open("data/hosts.json", 'r') as hosts:
        data = json.load(hosts)
    for host in data:
        if "r" in host["hostname"].lower():
            driver = get_network_driver('ios')
            device  = driver(hostname=host["ip"], username=host["username"], password=host["password"])
            device.open()
            device.load_merge_candidate(filename=f"config/ospf_{host["hostname"].lower()}.conf")
            print(device.compare_config())
            #apply the changes
            device.commit_config()


def question_34():
    with open("data/hosts.json", 'r') as hosts:
        data = json.load(hosts)
    for host in data:
        driver = get_network_driver('ios')
        device  = driver(hostname=host["ip"], username=host["username"], password=host["password"])
        device.open()
        config = device.get_config()
        print(config["running"])
        with open(f"config/{host["hostname"].upper()}.bak", 'w') as f:
            f.write(config["running"])
            f.close()

if __name__ == "__main__":
    r01 = {
        'hostname':'172.16.100.126',
        'username': "cisco",
        'password': "cisco"
    }

    driver = get_network_driver('ios')
    device  = driver(**r01)
    device.open()
    
    #question_26(device)
    #question_27(device)
    #question_28(device)
    #question_29(device)
    question_30(device)
    #question_31()
    #question_32()
    #question_34()