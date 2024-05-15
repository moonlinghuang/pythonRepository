import yaml
from jinja2 import Environment,FileSystemLoader
yaml_data = yaml.load(open("test.yaml", "r", encoding="utf-8"), Loader=yaml.FullLoader)
template_dir = "./"
template_env = Environment(loader=FileSystemLoader(template_dir), trim_blocks=True, lstrip_blocks=True)
for device, config in yaml_data['dc1'].items():
    if config['device_template'] == 'viosl2_template':
        device_template = template_env.get_template("router_day1_template.j2")
    elif config['device_template'] == 'viosl3_template':
        device_template = template_env.get_template("switch_day1_template.j2")

    print("rendering now device {}".format(device))
    day0_device_config = device_template.render(config)
    print(day0_device_config)
    print("="*30)