from __future__ import unicode_literals, print_function
from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment
from jinja2 import Template

# env = Environment()
# env.loader = FileSystemLoader('.')
env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader('.')
# env.loader = FileSystemLoader([".",'./templates/'])

base_intf = "GigabitEthernet0/1/"
intf_list = []
for intf_number in range(24):
    intf_name = f"GigabitEthernet0/1/{intf_number}"
    intf_list.append(intf_name)
    print(intf_list)
    break
my_vars = { "intf_list":intf_list,}
template_file = "for_loop2.j2"

template = env.get_template(template_file)
output = template.render(**my_vars)
print(output)
