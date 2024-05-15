import  re
intf_ip = '''Gi0/0/0.705        10.103.17.5         YES NRRAM UP        UP
Gi0/0/0.900         86.121.75.31            YES NRRAM UP            UP
Gi0/0/0.911         10.200.101.242          YES NRRAM UP            UP
Gi0/0/0.7000        unassigned              YES unset up            up
'''
# match = re.search("\d+\.+\d+\.+\d+\.+\d",intf_ip)
# match2 = re.findall("\d+\.+\d+\.+\d+\.+\d",intf_ip)
# match3 = re.search("(\d+\.+\d+\.+\d+\.+\d)\s+(\w+)",intf_ip)
# if match:
#     print(match.group())
# print("=================match1==============")
# if match2:
#     print(match2)
# print("==================match2==============")
# if match3:
#     print(match3)


# for line in intf_ip.split("\n"):
#     print("========")
#     print(line)
#     match = re.search(r"(?P<interface>\w+\d\/\d\/\d.\d+)\s+(?P<ip>\d+.\d+.\d+.\d+)",line)
#
#     if match:
#         ipaddr = match.groupdict()
#        # print(ipaddr)
#         if ipaddr["ip"].startswith('10'):
#             print("subnet is cofigured on "+ipaddr['interface']+" and ip is "+ipaddr['ip'])

addr = re.findall(r"(?P<interface>\w+\d\/\d\/\d.\d+)\s+(?P<ip>\d+.\d+.\d+.\d)",intf_ip)
print(addr)


