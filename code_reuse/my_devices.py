#from netmiko import ConnectHandler
from  getpass import getpass

password = getpass()
API_KEY = 'asdasjhfsjhfskjdfsdkjfsdj'

router3 = {
    "host" : 'cisco3.lasthop.io',
    "username" : 'pyclass',
    "password" : password,
    "device_type" : 'cisco_ios',
    #session_log = 'my_session.txt'
}
router4 = {
       "host" : 'cisco3.lasthop.io',
       "username" : 'pyclass',
       "password" : password,
       "device_type" : 'cisco_ios',
       #session_log = 'my_session.txt'
  }


#net_connect = ConnectHandler(**device1)
#print(net_connect.find_prompt())
#net_connect.disconnect()
