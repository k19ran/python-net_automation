import yaml

my_data = {
        'device_name': 'my_device',
        'ip_addr': '1.1.1.1',
        'username': 'cisco',
        'password': 'pwd'
        }

some_list = list(range(10))
my_data['some_list'] = some_list
my_data['null_value'] = None
my_data['a_bool'] = False

#filename=sample1.yml
with open("misc_list_dict_sample.yml", "rt") as f:
    yaml.dump(my_data,f,default_flow_style=True)
