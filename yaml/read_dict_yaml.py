import yaml

filename = input("Enter a filename:")
with open(filename) as f:
    yaml_out = yaml.load(f)
print(f"output of the values in the file:{yaml_out}")
print(f"datatype of this file:{type(yaml_out)}")
print()
print(f"items in this dict are:{yaml_out.items()}")
print()
print(f"keys in this dict are:{yaml_out.keys()}")
print()
print(f"printing only values of the keys in this file:{yaml_out['key1']},{yaml_out['key2']},{yaml_out['key3']},{yaml_out['key4']}")
print()
print(f"values in this dict are:{yaml_out.values()}")
print()
output = print(f"values in this dict are:{yaml_out.values()}")
print(f"data type of output of values:{output}")




