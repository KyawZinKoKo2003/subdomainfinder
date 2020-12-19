import requests
import time
from colorama import Fore,Back,Style
import os
banner='''
:'######::'##::::'##:'########::'########:'####:'##::: ##:'########::'########:'########::
'##... ##: ##:::: ##: ##.... ##: ##.....::. ##:: ###:: ##: ##.... ##: ##.....:: ##.... ##:
 ##:::..:: ##:::: ##: ##:::: ##: ##:::::::: ##:: ####: ##: ##:::: ##: ##::::::: ##:::: ##:
. ######:: ##:::: ##: ########:: ######:::: ##:: ## ## ##: ##:::: ##: ######::: ########::
:..... ##: ##:::: ##: ##.... ##: ##...::::: ##:: ##. ####: ##:::: ##: ##...:::: ##.. ##:::
'##::: ##: ##:::: ##: ##:::: ##: ##:::::::: ##:: ##:. ###: ##:::: ##: ##::::::: ##::. ##::
. ######::. #######:: ########:: ##:::::::'####: ##::. ##: ########:: ########: ##:::. ##:
:......::::.......:::........:::..::::::::....::..::::..::........:::........::..:::::..::
           
                       Writer:: Kyaw Zin KO KO '''


time.sleep(1)
green=Fore.GREEN
print(Style.BRIGHT+green+banner)
time.sleep(3)


url=str(input(green+'[+]Enter the name of domain you want to find [+] --> '))
time.sleep(1)
print("Finding for susbdomains...")
sub_domains=open("url.txt",'r')
real_sub=sub_domains.read()
real_subdomains=real_sub.splitlines()
for subdomain in real_subdomains:
    result=f"https://{subdomain}.{url}"
    try:
        requests.get(result)
    except requests.ConnectionError:
        pass
    else:
        print("subdomain found at",result)
