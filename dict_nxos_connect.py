from netmiko import ConnectHandler
from getpass import getpass

nxos_1 = {
"host" : "nxos2.lasthosp.io","username" : "pyclass", "password" : getpass(), "device_type" : "cisco_nxos"
}
net_connect = ConnectHandler(**nxos_1)
print(net_connect.find_prompt())
