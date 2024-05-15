import multiprocessing
import multiprocessing as mp
from netmiko import ConnectHandler
from devices import device1, device2
from datetime import datetime

nodes = [device1, device2]

def connect_to_dev(device, mqueue):
    dev_id = device['ip']
    return_data = {}
    net_connect = ConnectHandler(**device)
    output = net_connect.send_command("cat /etc/os-release")
    return_data[dev_id] = output
    print("adding the result to the multiprocess queue")
    mqueue.put(return_data)


def proc():
    processes = []
    mqueue = multiprocessing.Queue()
    start_time = datetime.now()
    print("adding process to the list")
    for device in nodes:
        p = mp.Process(target=connect_to_dev, args=[device, mqueue])
        processes.append(p)
        p.start()

    print("joining the finished process to the main truck")
    for p in processes:
        p.join()

    result = []
    for p in processes:
        print("moving the result from the  queue to the results list")
        result.append(mqueue.get())
    print(result)
    print("="*50)
    # print(mqueue.get())
if __name__ == "__main__":
    proc()
