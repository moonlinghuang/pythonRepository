import subprocess
# p = subprocess.Popen(["grep","subprocess"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
# stdout,stderr = p.communicate(input=b"welcome to subprocess module \nthis line is a new line and does not contain the require string")
#
# print("==================output is==================={}".format(stdout))
# print("==================error is==================={}".format(stderr))
def ping_destination(ip):
    p = subprocess.Popen(['ping',ip, '-c', '3'], stdout=subprocess.PIPE, stdin=subprocess.PIPE)
    stdout,stderr = p.communicate(input=ip)
    if p.returncode==0:
        print("Host is alive")
        return True, stdout
    else:
        print("Host is down")
        return False,stderr
while True:
    print(ping_destination(input("please input a  ip :")))
