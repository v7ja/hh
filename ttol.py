import requests, random, datetime
from colorama import Fore
R = Fore.RED
P = Fore.GREEN
s = Fore.LIGHTRED_EX
y = Fore.YELLOW
fz = datetime.datetime.now()
Z = '\033[1;31m' ; X = '\033[1;33m' ; F = '\033[2;32m' ; B = '\x1b[38;5;208m' ; Y = '\033[1;34m' ; C = "\033[1;97m" ; E = '\033[1;31m' ; G = '\033[1;32m' ; S = '\033[1;33m' ; A = '\033[1;31m' ; logo =f""" 
                    {Z}< {C}cHecker Tik v3{Z} >    
     {C}    ╔{Z}══════════{C}═════════════════════{Z}═════════{C}╗
      {Z}   ║{C}<{X}\{C}> {C} Programier{A}  : {C}@kckkkkc{Z}           ║
      {C}   ║{C}<{X}\{C}>  {C}Telegram{A}    : {C}@ShePython{C}         ║
      {C}   ║{C}<{X}\{C}>  {C}YouTube{A}     : {C}r2-{C}                ║
      {A}   ║{C}<{X}\{C}>  {C}Second Account{Z}  : {C}@KeePusa{A}       ║
      {C}   ╚{Z}══════════{C}══════════════════════{Z}════════{C}╝
""" ; print(logo)
sa="4"
if sa =="4":
    uesr = ''   
    chars2 = 'qwertyuiopasdfghjklzxcvbnm1234567890._'
    amount = 5000
    amount = int(amount)

    length2 = 4
    length2 = int(length2)

    for password in range(amount):
        password = ''

        for item in range(length2):
            password = ''
        for item in range(length2):
            password += random.choice(chars2)

        
        with open('user.txt', 'a') as x:
            x.write(uesr + password + '\n')
j = requests.get('https://pastebin.com/raw/jsXm5HCA').text
x2 = requests.get('https://pastebin.com/raw/08NqbfeS').text
use="user.txt"
ID = input(R+"Enter Your id Account -> :")
token = input(R+'EnTer Your Token ->:')
headers={
"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36",
"Connection": "close",
"Host": "www.tiktok.com",
"Accept-Encoding": "gzip, deflate",
"Cache-Control": "max-age=0"}
file = open(use, "r")
while True:
	Check = file.readline().split('\n')[0]
	if Check == '':
		break
	tiklog = f'https://www.tiktok.com/@{Check}'
	rq = requests.get(tiklog, headers=headers)
	if rq.status_code == 404:
		print(P+'[+] Available >> {}'.format(Check))
		tele = (
			f'https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={j}\n⦗ 𝘂𝘀𝗲𝗿 ⦘ | ⦗ {Check} ⦘\n{x2}')
		re = requests.post(tele)
		with open('Tik-HuNt.txt', 'a') as x:
			x.write(Check + '\n')
	elif rq.status_code == 200:
		print(s+'[-] NoT Available >> {}'.format(Check))



