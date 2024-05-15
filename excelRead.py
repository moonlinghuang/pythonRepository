import xlrd
from netmiko.exceptions import AuthenticationException,NetmikoTimeoutException
from netmiko import ConnectHandler

workbook = xlrd.open_workbook(r"D:\linux.xlsx")
sheet = workbook.sheet_by_index(0)

for index in range(1,sheet.nrows):
    hostname = sheet.row(index)[0].value
    ipaddr = sheet.row(index)[1].value
    username = sheet.row(index)[2].value
    password = sheet.row(index)[3].value
    secret = sheet.row(index)[4].value
    vendor = sheet.row(index)[5].value

    device = {
        'device_type': vendor,
        'ip': ipaddr,
        'username': username,
        'password': password,
        'secret': secret
    }

    try:
        net_connect = ConnectHandler(**device)
        net_connect.enable()
        output = net_connect.send_command("cat /etc/os-release")
        print(output)
    except AuthenticationException:
        print("Authentication Failed with {}".format(device['ip']))
    except NetmikoTimeoutException:
        print("NetmikoTimeout Failed with {}".format(device['ip']))
    except Exception as unknown_error:
        print("=========SOMETHING UNKNOWN HAPPEN WITH {} ===========")