import re
import subprocess
from netaddr import IPNetwork, AddrFormatError
from prettytable import PrettyTable


def nmap_report(data):
    bytes_data = data.decode('utf-8')
    mac_flag = ""
    ip_flag = ""
    host_table = PrettyTable(["IP", "MAC", "Vendor"])
    numbers_of_hosts = bytes_data.count('Host is up')
    for line in bytes_data.split("\n"):
        if "MAC Address:" in line:
            mac = line.split("(")[0].replace("MAC Address: ","")
            vendor = line.split("(")[1].replace(")","")
            mac_flag = "ready"
        elif "Nmap scan report for" in line:
            ip = re.search(r"Nmap scan report for (.*)", line).groups()[0]
            ip_flag = "ready"

        if mac_flag == "ready" and ip_flag == "ready":
            host_table.add_row([ip, mac, vendor])
            mac_flag = ""
            ip_flag = ""

    print("number of live hosts is {}".format(numbers_of_hosts))
    print(host_table)

network = "192.168.182.1/24"

try:
    IPNetwork(network)
    p = subprocess.Popen(["sudo", "nmap", "-sP", network], stdout=subprocess.PIPE)
    nmap_report(p.stdout.read())
except AddrFormatError:
    print("please Enter a valid network IP address in x.x.x.x/y format")