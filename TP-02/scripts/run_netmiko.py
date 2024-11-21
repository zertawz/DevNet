import json
from netmiko import ConnectHandler

def question_9(net_connect):
    print(net_connect)
    print(net_connect.__dict__)
    print(f"Adresse IP : {net_connect.host}")
    print(f"Type d'appareil : {net_connect.device_type}")

def question_10(net_connect):
    output = net_connect.send_command("show ip int brief")
    print(output)

def question_11(net_connect):
    output = net_connect.send_command("show ip int brief",use_textfsm=True)
    print(output)
    print(type(output))


def question_12(net_connect):
    output = net_connect.send_command("sh ip route",use_textfsm=True)
    print(output)
    print(type(output))

def question_13(net_connect):
    output = net_connect.send_command("show ip int brief",use_textfsm=True)
    interfaces = []
    for item in output:
        #get a list with the interfaces (maybe usefull later)
        interfaces.append(item['interface'])
        suboutput = net_connect.send_command(f"sh run | s {item['interface']}")
        print(suboutput)


def question_14(net_connect):
    commands = [
        'interface loopback 1',
        'ip address 192.168.1.1 255.255.255.255',
        'description loopback interface from netmiko'
        ]
    net_connect.send_config_set(commands)


def question_15(net_connect):
    commands = [
        'no interface loopback 1',
        'no ip address 192.168.1.1 255.255.255.255',
        'no description loopback interface from netmiko'
        ]
    net_connect.send_config_set(commands)

def question_16(net_connect):
    output = net_connect.send_config_from_file("config/loopback_R01.conf")
    #print(output)



def question_17(net_connect):
    output = net_connect.send_config_from_file("config/no_loopback_R01.conf")


def get_inventory():
    with open("data/hosts.json", 'r') as hosts:
        data = json.load(hosts)
    return data


def question_20():
    hosts = get_inventory()
    for host in hosts:
        print(host)
        if host["hostname"][0].lower()=="r":
            net_connect2 = ConnectHandler(**host)
            net_connect2.send_command(f"sh run | s interface g0/0.99")
            net_connect2.disconnect()


def question_21():
    pass

if __name__ == "__main__":    

    r01 = {
        'device_type': 'cisco_ios',
        'host':   '172.16.100.126',
        'username': 'cisco',
        'password': 'cisco',
        'port': 22
    }
    net_connect = ConnectHandler(**r01)
    
    question_9(net_connect)
    question_10(net_connect)
    question_11(net_connect)
    question_12(net_connect)
    question_13(net_connect)
    question_14(net_connect)
    question_15(net_connect)
    question_16(net_connect)
    question_17(net_connect)
    hosts = get_inventory()
    print(hosts)
    question_20()
    #question_21()