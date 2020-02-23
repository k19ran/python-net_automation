from __future__ import unicode_literals, print_function
from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment
from jinja2 import Template

# env = Environment()
# env.loader = FileSystemLoader('.')
env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader('.')
# env.loader = FileSystemLoader([".",'./templates/'])

bgp_vars = {
    "bgp_peer1":True,
    "peer_ip1":"10.1.1.1",
    "bgp_policy":True,
}
template_file = "nested_cond.j2"

template = env.get_template(template_file)
output = template.render(**bgp_vars)
print(output)
