import requests,random

F = '\033[2;32m' #اخضر
Z = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
U = '\x1b[1;37m'#ابیض

print(f"""           
[+] my user ? @Howend
""")

Token_tele = input(f"Token > ")
print("  "*10)
Id_tele = input(f"iD > ")
print('  '*25)

L7Nrandom_num_Letter ="1234567890qwertyuiopasdfghjklzxcvbnm"
def L7Nd(user):
    L7NClicks = 0
    url = requests.post('https://www.instagram.com/accounts/web_create_ajax/attempt/',headers ={'Host':'www.instagram.com',
'content-length':'85',
'sec-ch-ua':'" Not A;Brand";v="99", "Chromium";v="101"',
'x-ig-app-id':'936619743392459',
'x-ig-www-claim':'0',
'sec-ch-ua-mobile':'?0',
'x-instagram-ajax':'81f3a3c9dfe2',
'content-type':'application/x-www-form-urlencoded',
'accept':'*/*',
'x-requested-with':'XMLHttpRequest',
'x-asbd-id':'198387',
'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.40 Safari/537.36',
'x-csrftoken':'jzhjt4G11O37lW1aDFyFmy1K0yIEN9Qv',
'sec-ch-ua-platform':'"Linux"',
'origin':'https://www.instagram.com',
'sec-fetch-site':'same-origin',
'sec-fetch-mode':'cors',
'sec-fetch-dest':'empty',
'referer':'https://www.instagram.com/accounts/emailsignup/',
'accept-encoding':'gzip, deflate, br',
'accept-language':'en-IQ,en;q=0.9',
'cookie':'csrftoken=jzhjt4G11O37lW1aDFyFmy1K0yIEN9Qv',
'cookie':'mid=YtsQ1gABAAEszHB5wT9VqccwQIUL',
'cookie':'ig_did=227CCCC2-3675-4A04-8DA5-BA3195B46425',
'cookie':'ig_nrcb=1'},data=f'email=aakmnnsjskksmsnsn%40gmail.com&username={user}&first_name=&opt_into_one_tap=false')
    if '{"message":"feedback_required","spam":true,"feedback_title":"Try Again Later","feedback_message":"We limit how often you can do certain things on Instagram to protect our community. Tell us if you think we made a mistake.","feedback_url":"repute/report_problem/scraping/","feedback_appeal_label":"Tell us","feedback_ignore_label":"OK","feedback_action":"report_problem","status":"fail"}' in url.text:
        print(f"Bad User > {user}")
     
    elif  '"errors": {"username":' in url.text or  '"code": "username_is_taken"' in url.text:
        print(f"Bad User > {user}")
        L7NClicks+=1
   
    else: 
        print(f"Climed User > {user}")
        L7N1=f"""
 New Climed Sir.?  
 UserName : ❲ @{user} ❳‌‌ 
 Clicks : ❲ {L7NClicks} ❳‌‌  
 DevLoper : ❲ @Howend , @fakeShe❳‌‌  """
        requests.post(f"https://api.telegram.org/bot{Token_tele}/sendMessage?chat_id={Id_tele}&text="+str(L7N1))

def L7Nend():
    while True:
	       a = str(''.join((random.choice(L7Nrandom_num_Letter) for i in range(1))))
	       c = str(''.join((random.choice(L7Nrandom_num_Letter) for i in range(1))))
	       b = str(''.join((random.choice(L7Nrandom_num_Letter) for i in range(1))))
	       k1 = a+b+b+'_'+a
	       k2 = a+'_'+b+'_'+c
	      
	       L7Nus = k1,k2
	       user = random.choice(L7Nus)
	       L7Nd(user)
L7Nend()