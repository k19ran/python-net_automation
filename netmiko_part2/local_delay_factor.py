from netmiko import ConnectHandler
from getpass import getpass

password = getpass()

cisco_3 = {
"host" : "cisco3.lasthop.io","username" : "pyclass", "password" : password, "device_type" : "cisco_ios"}

net_connect = ConnectHandler(**cisco_3)
print(net_connect.find_prompt())
print(net_connect.send_command("show version",delay_factor=10 ))

