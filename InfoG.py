from utils import *
tool_name()
your_ip()
print('''
[1]Get website IP address

[2]IP lookup

[3]Phone no. lookup

[4]IP-Grabber

''')
try:
    while True:
        command= input('InfoG> ')
        if command == '1':
            domain_name()
        elif command == '2':
            ip_lookup()
        elif command == '3':
            ph_num_lookup()
        elif command == '4':
            ip_grabber()
        else:
            print('Enter a valid command')

except KeyboardInterrupt:
    tool_name()
