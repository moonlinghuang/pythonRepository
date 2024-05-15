import platform
import smtplib
from datetime import datetime
def check_feature(feature,string):
    if feature in string.lower():
        return True
    else:
        return False

def get_value_from_string(key,string):
    value = "NONE"
    for line in string.split("\n"):
        if key in line:
            value = line.split(":")[1].strip()
    return value
cpu_features = []
with open('/proc/cpuinfo') as cpus:
    cpu_data = cpus.read()
    num_of_cpus = cpu_data.count("processor")
    cpu_features.append("Number of Processors: {0}".format(num_of_cpus))

    one_processor_data = cpu_data.split("processor")[1]
    print(one_processor_data)
    if check_feature('vmx', one_processor_data):
        cpu_features.append("cpu Virtualization: enabled")
    if check_feature('cpu_meltdown', one_processor_data):
        cpu_features.append("Know bugs: cpu meltdown")

    model_name = get_value_from_string("model name",one_processor_data)
    cpu_features.append("model name: {0}".format(model_name))

    cpu_mhz = get_value_from_string("cpu MHz",one_processor_data)
    cpu_features.append("CPU MHz: {0}".format(cpu_mhz))


with open('/proc/meminfo') as memory:
    memory_data = memory.read()
    total_memory = get_value_from_string("MemTotal",memory_data).replace('kB',"")
    free_memory = get_value_from_string("MemFree",memory_data).replace("kB","")
    swap_memory = get_value_from_string("SwapTotal",memory_data).replace("kB","")
    total_memory_in_gb = "Total Memory in GB:{0}".format(int(total_memory)/1024)
    free_memory_in_gb = "Free Memory in GB:{0}".format(int(free_memory) / 1024)
    swap_memory_in_gb = "Swap Memory in GB:{0}".format(int(swap_memory) / 1024)
    memory_features = [total_memory_in_gb,free_memory_in_gb,swap_memory_in_gb]

time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")


Data_sent_in_Email = ""
Header = """From: PythonEnterpriseAutomationBot <srv.jira@lotuscars.com.cn
To: To Administrator <mengling.huang@lotuscars.com.cn>
Subject: Monitoring System Report"""

Data_sent_in_Email += Header
Data_sent_in_Email += "==============Time Now is {0}==============\n".format(time_now)
Data_sent_in_Email += "\n=========================system information======================\n"
Data_sent_in_Email += """
system type: {0}
hostname: {1}
kernal version: {2}
system version: {3}
machine architeture: {4}
python verson: {5}
""".format(platform.system(),
           platform.uname()[1],
           platform.uname()[2],
           platform.version(),
           platform.machine(),
           platform.python_version())

Data_sent_in_Email += "\n=====================cpu information===================\n"
Data_sent_in_Email += "\n".join(cpu_features)

Data_sent_in_Email += "\n======================memory information=========================\n"
Data_sent_in_Email += "\n".join(memory_features)

fromaddr = 'srv.jira@lotuscars.com.cn'
toaddr = 'mengling.huang@lotuscars.com.cn'
username = 'srv.jira@lotuscars.com.cn'
password = 'm6TB0Vr1@O'

server = smtplib.SMTP('smtp.office365.com:587')
server.ehlo()
server.starttls()
server.login(username, password)
print(Data_sent_in_Email)
server.sendmail(fromaddr, toaddr, Data_sent_in_Email)
server.quit()