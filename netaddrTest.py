from netaddr import IPAddress,IPNetwork
import  ipaddress
def check_ip_address(ipaddr):
    ip_attributes = []
    ipaddress1 = IPAddress(ipaddr)

    if ipaddress1.is_ipv4_private_use():
        ip_attributes.append("ip address is private")
    else:
        ip_attributes.append("ip address is public")

    if ipaddress1.is_unicast():
        ip_attributes.append("ip address is unicast")
    elif ipaddress1.is_multicast():
        ip_attributes.append("ip address is multicast")
    if ipaddress1.is_loopback():
        ip_attributes.append("ip address is loopback")

    return "\n".join(ip_attributes)

def operate_on_ip_network(ipnet):
    net_attributes = []
    net = IPNetwork(ipnet)
    net_attributes.append("network ip address is "+ str(net.network)+"and network mask is "+str(net.netmask))

    net_attributes.append("the broadcast is "+str(net.broadcast))
    net_attributes.append("ip version is "+ str(net.version))
    net_attributes.append("infomation known about this network is "+ str(net.info))
    net_attributes.append("the ipv6 representation is "+str(net.ipv6()))
    net_attributes.append("the network size is "+ str(net.size))
    net_attributes.append("generating a list of ip addresses inside the subnet")

    for ip in net:
        net_attributes.append("\t"+str(ip))
    return "\n".join(net_attributes)

# ipaddr = input("please enter the ip address:")
# print(check_ip_address(ipaddr))

ipnet = input("please enter the ip network:")
print(operate_on_ip_network(ipnet))

