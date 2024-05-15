import  telnetlib
username = 'root'
password = 'Inspur1!'

cnx = telnetlib.Telnet(host='10.167.170.233')
cnx.read_until('username:')
cnx.write(username+'\n')
cnx.read_until("Password:")
cnx.write(password+'\n')
cnx.read_until(">")
cnx.write("en"+"\n")
cnx.read_until("#")
cnx.write("ip a"+'\n')
output = cnx.read_until("#")
print(output)