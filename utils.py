import socket
import phonenumbers
import requests
from phonenumbers import geocoder
import os 
import platform

def tool_name():
    print('''
 ___                                               ____________
|%%%|                                             |@@@@@@@@@@@@|
|%%%|  ____       ___   _________   ____________  |@@@@________|       
|%%%| |%%%%\     |%%%| |%%% _____| |%%%______%%%| |@@@|
|%%%| |%%%%%\    |%%%| |%%%|_____  |%%|      |%%| |@@@|       ___
|%%%| |%%%%%%\   |%%%| |%%%_____|  |%%|      |%%| |@@@|      |@@@|
|%%%| |%%%|\%%\  |%%%| |%%%|       |%%|      |%%| |@@@|______|@@@|
|%%%| |%%%| \%%\ |%%%| |%%%|       |%%|______|%%| |@@@@@@@@@@@@@@|
|___| |___|  \_______| |___|       |____________| |______________|By: Tech-Sec
For more visit: https://github/Tech-Sec
''')


def domain_name():
    print(socket.gethostbyname(input('Domain name: ')))


def your_ip():
    your_ip=requests.get('https://geolocation-db.com/json/').json() 
    print('Your public IP address: ',your_ip.get('IPv4'))
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    print('Your device name: ',hostname)
    print('Your private IP address ',ip_address)


def ip_lookup():
    enter_ip = input('IP Address: ')
    response = requests.get(f"https://geolocation-db.com/json/{enter_ip}&position=true").json()
    for key, value in response.items():
        print(key, ' : ', value)


def ph_num_lookup():
    your_ph_num = input('Your Number: ')
    phone_number = phonenumbers.parse(your_ph_num)
    # put your phonenumber with the country code eg:+1xxxxxxxx
    print(geocoder.description_for_number(phone_number,
                                          'en'))


    from phonenumbers import carrier
    service_provider = phonenumbers.parse(your_ph_num)
    # put your phonenumber with the country code eg:+1xxxxxxxx
    print(carrier.name_for_number(service_provider,
                                  'en'))
    
    
def ip_grabber():
    if platform.system == 'Windows':
        print('IP-Grabber is not supported on Windows')
    else:
        os.system('cd IP-Grabber && sudo chmod 777 * && bash ip-grabber.sh')
