import json
from napalm import get_network_driver


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
    with open(file_path, 'r') as variables:
        data = json.load(variables)



def question_32():
    pass


def question_34():
    pass



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
    question_29(device)
    #question_30(device)
    #question_31()
    #question_32()
    #question_34()