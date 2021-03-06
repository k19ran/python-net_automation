from netmiko import ConnectHandler
from getpass import getpass

password = getpass()

nxos_1 = {
"host" : "nxos1.lasthop.io","username" : "pyclass", "password" : password, "device_type" : "cisco_nxos"
}
nxos_2 = {
   "host" : "nxos2.lasthop.io","username" : "pyclass", "password" : password, "device_type" : "cisco_nxos"
  }
for device in (nxos_1,nxos_2):
    net_connect = ConnectHandler(**device)
    print(net_connect.find_prompt())
