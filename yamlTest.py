import  yaml
from pprint import pprint
with open(r'./test.yaml','r',encoding='utf-8') as file:
    yaml_data = yaml.load(file, Loader=yaml.FullLoader)

print(yaml_data)
print("==================================")
pprint(yaml_data)

print(yaml_data['data']['NAMESPACE'])