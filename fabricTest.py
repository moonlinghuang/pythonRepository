from fabric.api import *
#env.user = 'root'
env.hosts = ['root@192.168.182.129:22', 'root@192.168.182.132:22']
env.passwords = {
    'root@192.168.182.129:22': 'eve',
    'root@192.168.182.132:22': 'root',
}



def detect_host_type():
    output = run("uname -s ")
    if output.failed:
        print("something wrong happen,please check the logs")
    elif output.succeeded:
        print("command executed successfully")
def list_all_files_in_directory():
    directory = prompt("please enter full path to the directory to list",default="/root")
    sudo("cd {0};ls -htlr".format(directory))

def main_tasks():
    detect_host_type()
    list_all_files_in_directory()
