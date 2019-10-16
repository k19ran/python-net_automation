from netmiko import ConnectHandler, file_transfer
from  getpass import getpass

device1 = {
    "host" : 'cisco3.lasthop.io',
    "username" : 'pyclass',
    "password" : getpass(),
    "device_type" : 'cisco_ios',
    #session_log = 'my_session.txt'
}

source_file = "text_kigun.txt"
dest_file = "testx.txt"
direction = "put"
file_system = "bootflash:"

# create the netmiko ssh conenction
ssh_conn  = ConnectHandler(**device1)
transfer_dict = file_transfer(
    ssh_conn,
    source_file = source_file,
    dest_file = dest_file,
    file_system = file_system,
    direction = direction,
    overwrite_file = True,
)
print(transfer_dict)
ssh_conn.disconnect()

