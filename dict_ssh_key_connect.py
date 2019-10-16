from netmiko import ConnectHandler
from  getpass import getpass

device1 = {
    "host" : 'cisco3.lasthop.io',
    "username" : 'testuser',
    "device_type" : 'cisco_ios',
    "use_keys" : True,
    "key_file" : "/home/kiran/.ssh/test_rsa"
    #session_log = 'my_session.txt'
}

net_connect = ConnectHandler(**device1)
print(net_connect.find_prompt())
net_connect.disconnect()
