# dumpyaml.py

import sys
import pprint
import yaml


with open(sys.argv[1], 'r') as file:
    data = yaml.safe_load(file)
dup = yaml.dump(data, default_flow_style=False)

print(dup)

def dump(data, indent=''):
    for key, value in data.items():
        if isinstance(value, list):
            print(f"{indent}{key}: [")
            for x in value:
                print(f"{indent} ", x)
            print(f"{indent}]")
        elif isinstance(value, dict):
            print(f"{indent}{key}:", "{")
            dump(value, indent + ' ')
            print(f"{indent}}}")
        else:
            print(f"{indent}{key}: {value}")

dump(data)
