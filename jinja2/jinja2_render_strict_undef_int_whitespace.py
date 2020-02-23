from __future__ import unicode_literals, print_function
from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment
from jinja2 import Template

# env = Environment()
# env.loader = FileSystemLoader('.')
env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader('.')
# env.loader = FileSystemLoader([".",'./templates/'])

my_vars = {"primary_ip": True}
template_file = "int_config_strip_whitespace.j2"

template = env.get_template(template_file)
output = template.render(**my_vars)
print(output)
