#!/usr/local/bin/python
from netmiko import  SSHDetect,Netmiko
device ={
    'device_type': 'autodetect',
    'host': '10.167.130.71',
    'username': 'root',
    'password': 'Inspur1!'
}

detect_device = SSHDetect(**device)
devie_type = detect_device.autodetect()
print(devie_type)
print(detect_device.potential_matches)

device['device_type'] = devie_type
connect = Netmiko(**device)