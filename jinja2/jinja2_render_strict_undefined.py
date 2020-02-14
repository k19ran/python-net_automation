from __future__ import unicode_literals, print_function
from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment
from jinja2 import Template

# env = Environment()
# env.loader = FileSystemLoader('.')
env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader('.')
# env.loader = FileSystemLoader([".",'./templates/'])

filename = "bgp_config.j2"
#with open(filename) as f:
#    my_template = f.read()

template_vars = {
    "bgp_as": 22,
    "router_id": "1.1.1.1",
    "peer_1": "10.20.30.1",
    "remote_as": 44
}

template = env.get_template(filename)
output = template.render(**template_vars)
print(output)
