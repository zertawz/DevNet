import json
from netmiko import ConnectHandler
import os

RED = "\033[91m"
GREEN = "\033[92m"
RESET = "\033[0m"

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
    print(output)

def question_17(net_connect):
    output = net_connect.send_config_from_file("config/no_loopback_R01.conf")


def get_inventory():
    with open("data/hosts.json", 'r') as hosts:
        data = json.load(hosts)
    return data


def question_20():
    hosts = get_inventory()
    for host in hosts:        
        if host["hostname"][0].lower()=="r":
            #we get rid of hostname parameter in the dict (causes trouble with netmiko)
            connection_params = {key: value for key, value in host.items() if key != 'hostname'}
            net_connect2 = ConnectHandler(**connection_params)
            output = net_connect2.send_command(f"show running-config interface GigabitEthernet0/0.99")
            print(output)
            net_connect2.disconnect()


def question_21():
    hosts = get_inventory()
    for host in hosts:
        configuration_file = f"config/vlan_{host["hostname"]}.conf"
        #Verify if the configuration file searched exists
        if not os.path.exists(configuration_file):
            print(f"Fichier de configuration {configuration_file} introuvable. Passer à l'itération suivante.")
            continue  #Jump to next iteration
        else:
            print(f"Fichier de configuration {configuration_file} trouvé. On pousse la configuration")
            try:
                connection_params = {key: value for key, value in host.items() if key != 'hostname'}
                net_connect2 = ConnectHandler(**connection_params)
                net_connect2.send_config_from_file(configuration_file)
                net_connect2.disconnect()
                print(f"{GREEN}Configuration {configuration_file} envoyé avec succès{RESET}")

            except:
                print(f"{RED}Erreur avec la configuration {configuration_file}{RESET}")

if __name__ == "__main__":    

    r01 = {
        'device_type': 'cisco_ios',
        'host':   '172.16.100.126',
        'username': 'cisco',
        'password': 'cisco',
        'port': 22
    }
    net_connect = ConnectHandler(**r01)
    
    #question_9(net_connect)
    #question_10(net_connect)
    #question_11(net_connect)
    #question_12(net_connect)
    #question_13(net_connect)
    #question_14(net_connect)
    #question_15(net_connect)
    #question_16(net_connect)
    #question_17(net_connect)
    #hosts = get_inventory()
    #print(hosts)
    #question_20()
    question_21()
    net_connect.disconnect()