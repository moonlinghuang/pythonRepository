import netmiko

R1={
    'device_type': 'linux',
    'ip': '101.167.130.71',
    'username': 'root',
    'password': 'Inspur1!',
    'secret': 'Inspur1!'
}

from netmiko import  ConnectHandler
from netmiko.exceptions import  AuthenticationException,NetmikoTimeoutException
try:
    connection = ConnectHandler(**R1)
    connection.enable()
    output = connection.send_command('cat /etc/os-release',strip_command=False,strip_prompt=False)
    print(output)
    connection.disconnect()
except NetmikoTimeoutException:
    print("timeout {0}".format(R1['ip']))
except AuthenticationException:
    print("auth fault {0}".format(R1['ip']))