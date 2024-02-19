import os
import time
try :
    import requests
    import user_agent
    import datetime
    import webbrowser
    import pyfiglet
    import threading
    import signal
except ImportError as error :
    os.system('pip install requests')
    os.system('pip install user_agent')
    os.system('pip install datetime')
    os.system('pip install webbrowser')
    os.system('pip install pyfiglet')
    os.system('pip install threading')
    os.system('pip install signal')
    os.system('cls'if os.name=='nt' else'clear')
    time.sleep(1)
    print('Done.')
    exit()
import instaloader
import requests
from time import sleep
import os
import sys
from user_agent import generate_user_agent
import datetime
import random
import requests
from colorama import Fore,Back
import time
import sys as n
import time as mm
import secrets
from user_agent import generate_user_agent
os.system('clear')
B="\033[1;30m" # Black
R="\033[1;31m" # Red
G="\033[1;32m" # Green
Y="\033[1;33m" # Yellow
Bl="\033[1;34m" # Blue
P="\033[1;35m" # Purple
C="\033[1;36m" # Cyan
W="\033[1;37m" # White
print(C+   """  

""")
Z = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
Z1 = '\033[2;31m' #احمر ثاني
F = '\033[2;32m' #اخضر
A = '\033[2;34m'#ازرق
Y = '\033[1;34m' #ازرق فاتح
M = '\x1b[1;37m'#ابیض
U = '\x1b[1;37m'#ابیض
X = '\033[1;33m' #اصفر
Y = '\033[1;34m' #ازرق فاتح
M = '\x1b[1;37m'#ابیض
S = '\033[1;33m'
R = '\033[1;31m' #احمر
F = '\033[2;32m' #اخضر
C = "\033[1;97m" #ابيض
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح.
C1 = '\033[2;35m'
import json
import requests
import os
import random
from user_agent import generate_user_agent
import datetime
import json
from time import sleep
from os import system
from datetime import date
												

print('')
cookies=sid = input('SEASOON ID :')
os.system("clear")
H="\x1b[38;5;208m" #


a=0
v=0
def HANI():
 head={'Cookie':'mid=YF55GAALAAF55lDR3NkHNG4S-vjw; ig_did=F3A1F3B5-01DB-457B-A6FA-6F83AD1717DE; ig_nrcb=1; shbid=13126; shbts=1616804137.1316793; rur=PRN; ig_direct_region_hint=ATN; csrftoken=ot7HDQ6ZX2EPbVQe1P9Nqvm1WmMkzKn2; ds_user_id=46165248972; sessionid='+sid}
 while True:
#  mal=['male','femal']
#  gen=random.choice(mal)
  user='angel.gator'
  num='123'
  rng=int("".join(random.choice(num)for i in range(1)))
  name=str("".join(random.choice(user)for i in range(rng)))
  hani=requests.get(f'https://www.instagram.com/web/search/topsearch/?context=blended&query={name}',headers=head).json()
  hhan = 0
  
  try:
    while True:
    	global a,z,t,x,ll
    	hhan+=1
    	email = user=str(hani['users'][hhan]['user']['username'])
    	a+=1
    	print(f'\033[1;33m[{a}]«--» : [{email}] ')
    	user = email+'@hotmail.com'
    	with open('user123.txt', 'a') as (HA):
	   		HA.write(f'{user}\n')
  except IndexError:
  	print(Z+'STOP Event Error ')     
          
        		
	
	

                                      
                                   
print(f"""
{B}Welcome to the hunting tool insta   
{Z}┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓           
{X}┃   {M}❖ @ K_Q_A {Z}         ➠         {M}@ H_6_N{X}  
{F}┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛               """)
print(' ➘  ')
print('\033[1;33m ســحب لـــســتــه عشوائي [1]\nحـــــــــــذف لـــــــــســــتــــه [0]')
try:
	print('')
	HA = int(input(' \033[1;36m  : اختار رقم للاستمرار [❖]  '))
	os.system("clear")
except ValueError as error:
	os.system('clear')
	print('Error - خـطـا')
	exit()
if HA ==1:
	HANI()		
elif HA ==0:
    O()	 
else:
	os.system('clear')
	print('Error')
	exit()
