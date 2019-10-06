from netmiko import ConnectHandler
from getpass import getpass

password = getpass()

cisco_1 = {
"host" : "cisco3.lasthop.io","username" : "pyclass", "password" : password, "device_type" : "cisco_ios"
}

net_connect = ConnectHandler(**cisco_1)
print(net_connect.send_command("show version"))
