from jinja2 import Template

bgp_config = """
router bgp {{ bgp_as }}
 bgp router-id {{ router_id }}
 bgp log-neighbor-changes
 neighbor {{ neighbor1 }} remote-as {{ remote_as }}
"""
my_vars = {
    "bgp_as":22,
    "router_id": "10.220.88.20",
    "neighbor1": "10.220.88.38",
    "remote_as": "44"
}
my_template = bgp_config
j2_template = Template(my_template)
output = j2_template.render(**my_vars)
#output = j2_template.render(bgp_as=22,router_id="10.220.88.20",neighbor1="10.220.88.38",remote_as=44)
print(output)
