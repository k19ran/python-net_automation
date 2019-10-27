import yaml
import json

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

#filename=sample1.json
with open("output_file.json", "wt") as f:
    json.dump(my_data,f,indent=4)
# print to stdout as python representation
print("python")
print("#" * 10)
print(my_data)
print()
print("JSON")
print("#" * 10)
print(json.dumps(my_data))
