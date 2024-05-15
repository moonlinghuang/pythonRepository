import matplotlib.pyplot as plt
import time
from pysnmp.entity.rfc3413.oneliner import cmdgen

# plt.plot([1,2,3,4],[10,20,30,40],label='first')
# plt.plot([5,6,7,8],[50,60,70,80],label='second')
# plt.xlabel("numbers")
# plt.ylabel("tensssss")
# plt.title("generat it out")
# plt.legend()
# plt.show()

cmdGen = cmdgen.CommandGenerator()

snmp_community = cmdgen.CommunityData('public')
snmp_ip = cmdgen.UdpTransportTarget(('10.167.130.71', 22))
snmp_oids = [".1.3.6.1.4.1.9.2.2.1.1.6.3", ".1.3.6.1.4.1.9.2.2.1.1.8.3"]

slots = 0
input_rates = []
output_rates = []
while slots <= 50:
    errorIndication, errorStatus, errorIndex, varBinds = cmdGen.getCmd(snmp_community, snmp_ip, *snmp_oids)

    input_rate = str(varBinds[0]).split("=")[1].strip()
    output_rate = str(varBinds[1]).split("=")[1].strip()

    input_rates.append(input_rate)
    output_rates.append(output_rate)

    time.sleep(5)
    slots = slots + 1
    print(slots)

time_range = range(0, slots)

print(input_rates)
print(output_rates)

plt.plot(time_range, input_rates, label="input rate")
plt.plot(time_range, output_rates, label='output rate')
plt.xlabel('time slot')
plt.ylabel('rate slot')
plt.title('rate')
plt.legend()
plt.show()
