from netmiko import ConnectHandler
from  getpass import getpass
from my_devices import router3,router4,API_KEY

#print(router3)
print(API_KEY)

net_connect = ConnectHandler(**router4)
print(net_connect.find_prompt())
net_connect.disconnect()
