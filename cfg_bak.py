from netmiko import ConnectHandler
from datetime import datetime
with open("D:\linux.txt") as devices_file:
    devices = devices_file.readlines()
for line in devices:
    line = line.strip('\n')
    ipaddr = line.split(',')[0]
    username = line.split(',')[1]
    password = line.split(',')[2]
    enable_password = line.split(',')[3]
    vendor = line.split(',')[4]

    back_command = "cat /etc/os-release"

    print(str(datetime.now())+"connecting to device {}".format(ipaddr))
    net_connect = ConnectHandler(device_type=vendor,ip=ipaddr,username=username,password=password,secret=enable_password)
    net_connect.enable()
    running_config = net_connect.send_command(back_command)
    print(str(datetime.now())+"saving config from device {}".format(ipaddr))
    f = open("dev_"+ipaddr+"_.cfg", "w")
    f.write(running_config)
    f.close()
    print("========================================================")
