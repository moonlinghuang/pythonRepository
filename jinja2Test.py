from jinja2 import Template
import yaml
from pprint import pprint
yaml_data = yaml.load(open('./test.yaml', 'r', encoding='utf-8'), Loader=yaml.FullLoader)

router_day0_template=Template('''
hostname {{hostname}}
int {{mgmt_intf}}
    no shutdown
    ip add {{mgmt_ip}} {{mgmt_subnet}}
lldp run
''')
switch_day0_template = Template('''
hostname {{hostname}}
aaa new-model
aaa session-id unique
aaa authentication login default local
aaa authorization exec default local none
vtp mode transparent
vlan 10,20,30,40,50,60,70,80,90,100,200

int {{mgmt_inf}}
  no switchport
  no shut
  ip address {{mgmt_ip}} {{mgmt_subnet}}
''')
for device, config in yaml_data['dc1'].items():
    if config['device_template'] == 'viosl2_template':
        device_template = router_day0_template
    elif config['device_template'] == 'viosl3_template':
        device_template = switch_day0_template

    print("rendering now device {}".format(device))
    day0_device_config = device_template.render(config)
    print(day0_device_config)
    print("="*30)

