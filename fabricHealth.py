#!/usr/bin/python
__author__ = "mengling.huang"
__Email__ = "mengling.huang@lotuscars.com.cn"

from fabric.api import *
from fabric.context_managers import  *
from pprint import  pprint

env.hosts = ['root@192.168.182.129:22', 'root@192.168.182.132:22']
env.passwords = {
    'root@192.168.182.129:22': 'eve',
    'root@192.168.182.132:22': 'root',
}
env.roledefs = {
    'webapps': ['root@192.168.182.129:22'],
    'databases': ['root@192.168.182.132:22']
}
def discovery_commands():
    discovery_commands = {
        "uptime": "uptime|awk '{print $3,$4}'",
        "hostname": "hostname",
        "kernel_release": "uname -r",
        "architecture": "uname -m",
        "internal_ip": "hostname -I",
        "external_ip": "curl -s ipecho.net/plain;echo",
    }
    for operation,command in discovery_commands.items():
        print("========================={0}=======================".format(operation))
        output = run(command)

def health_commands():
    health_commands = {
        "used_memory": "free|awk '{print $3}'|grep -v free|head -n1",
        "free_memory": "free|awk '{print $4}'|grep -v shared|head -n1",
        "cpu_usr_percentage": "mpstat|grep -A 1 '%usr'|tail -n1|awk '{print $4}'",
        "number_of_process": "ps -A --no-headers|wc -l",
        "logged_users": "who",
        "top_load_average": "top -n 1 -b|grep 'load average:'|awk '{print $10 $11 $12}'",
        "disk_usage": "df -h|egrep 'Filesystem|/dev/sda*|nvme*'"
    }
    for operation,command in health_commands.items():
        print("========================={0}=======================".format(operation))
        output = run(command)

def get_system_health():
    discovery_commands()
    health_commands()


@roles('databases')
def validate_mysql():
    output = run("systemctl status mariadb")

@roles('webapps')
def validate_apache():
    output = run("systemctl status httpd")
