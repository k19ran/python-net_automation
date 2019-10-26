import yaml

filename = input("Enter a filenamee:")
with open(filename) as f:
    yaml_out = yaml.load(f)
print(yaml_out)
print(type(yaml_out))
#print(yaml_out[1])
