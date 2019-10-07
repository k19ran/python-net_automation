from netmiko import ConnectHandler
from getpass import getpass

password = getpass()

nxos_2 = {
"host" : "nxos2.lasthop.io","username" : "pyclass", "password" : password, "device_type" : "cisco_nxos"
}

net_connect = ConnectHandler(**nxos_2)
print(net_connect.find_prompt())
#print(net_connect.send_command("show version"))

command = 'delete bootflash:nxos2-startup-config'

output = net_connect.send_command(command, expect_string=r'y')
#output += net_connect.send_command('y', expect_string=r'confirm')
output += net_connect.send_command('y', expect_string=r'#')
print(output)
