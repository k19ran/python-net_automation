from jinja2 import Template

bgp_config = """
router bgp {{ bgp_as }}
 bgp router-id 10.220.88.20
 bgp log-neighbor-changes
 neighbor 10.220.88.38 remote-as 44
"""

example_error = """
some text with expr {{ 13 + 3 }}
other expressions {{ 13 * 7 }}
hello
"""

my_template = bgp_config
j2_template = Template(my_template)
output = j2_template.render(bgp_as=22)
print(output)
print()
#my_template1 = example_error
#j2_template1 = Template(my_template1)
#output1 = j2_template1.rendor()
#print(output1) 
