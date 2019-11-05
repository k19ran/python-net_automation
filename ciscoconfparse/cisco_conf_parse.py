from ciscoconfparse import CiscoConfParse
from pprint import pprint

cisco_obj = CiscoConfParse("cisco1.txt")
print(cisco_obj)
print()
my_obj = """
interface GigabitEthernet0/0/0
 ip address 10.220.88.22 255.255.255.0
 negotiation auto
!
interface GigabitEthernet0/0/1
 no ip address
 shutdown
 negotiation auto
!
"""
my_parse = CiscoConfParse(my_obj.splitlines())
pprint(my_parse)
pprint(dir(my_parse))
cisco_int = cisco_obj.find_objects(r"^interface")
pprint(cisco_int)
print(cisco_int[0].text)
pprint(dir(cisco_int))
print(cisco_int[0].children)

for child in cisco_int[0].children:
    print(child.txt)




