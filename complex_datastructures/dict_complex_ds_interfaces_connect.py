from netmiko import ConnectHandler
from  getpass import getpass
from pprint import pprint

device1 = {
    "host" : 'cisco3.lasthop.io',
    "username" : 'pyclass',
    "password" : getpass(),
    "device_type" : 'cisco_ios',
    #session_log = 'my_session.txt'
}

net_connect = ConnectHandler(**device1)
print(net_connect.find_prompt())
#output = net_connect.send_command("show ip int brief", use_textfsm=True)
output_1 = net_connect.send_command("show interfaces", use_textfsm=True)
#pprint(output)
#print("\n")
#print(output[0])
#print("\n")
#print(output[0]['ipaddr'])
print(output_1)
print('*' * 12)
print('*' * 12)
print(type(output_1))
print('*' * 12)
value = output_1[0]
print(value)
print()
print(type(value))
print()
#print(type(value[0]))
print()
print(value.keys())
#print(value['address'])
#print(value['mac'])
new_interfaces = output_1
print(type(new_interfaces)
