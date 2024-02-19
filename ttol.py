import requests
import random


iD = input(' Enter ID Bot : ')
print('\n')
token = input(' Enter Token Bot : ')
print('\n')
user = 'qwertyuiopasdfghjklzxcvbnm1234567890'
#user = '1234567890'
zok=0
def zz():
 global zok
	while True:
 	try:
	 	us = str("".join(random.choice(user)for x in range(1)))
	 	um = str("".join(random.choice(user)for x in range(1)))
	 	ur = str("".join(random.choice(user)for x in range(1)))
	 	a1 = us+'.'+um+'.'+ur
	a2 = us+'_'+um+'_'+ur
			a3 = us+'_'+us+'.'+um
			a4 = us+'_'+um+'_'us
			a5 = us+'.'+um+'.'us
			a6 = ur+'_'+um+'.'+us
			a7 = ur+ur+um+um+'_'
			a8 = ur+um+um+um+'_'
			a9 = ur+ur+um+um+'.'
			a10 = ur+um+um+um+'.'
			a11 = ur+ur+ur+um+'_'
			a12 = ur+ur+ur+um+'.'
			a13 = '_'+ur+ur+um+um
			a14 = '.'+ur+ur+um+ur
			a15 = '_'+ur+um+um+um
			a16 = '.'+um+um+um+ur
			a17 = ur+'_'+ur+'_'+ur
			a18 = ur+'.'+ur+'.'+ur
			a19 = ur+'_'+us+'_'+ur
			a20 = ur+'.'+us+'.'+ur
			a21 = ur+'_'+ur+'_'+us
			a22 = ur+'.'+ur+'.'+us
			a23 = us+'_'+ur+'_'+ur
			a24 = us+'.'+ur+'.'+ur
			a25 = ur+'_'+um+'_'+ur
			a26 = ur+ur+ur+'.'+us
			a27 = ur+ur+ur+'_'+us
			a28 = um+ur+ur+'.'+ur
			a29 = um+ur+ur+'_'+ur
			a30 = um+ur+ur+ur+ur
			a31 = um+ur+ur+ur+um
			a32 = us+ur+ur+ur+us
			a33 = um+um+ur+ur+ur
			a34 = us+us+ur+ur+ur
			a35 = ur+us+ur+us+ur
			a36 = '_'+ur+ur+ur+'_'
			a37 = '.'+ur+ur+ur+'.'
			a38 = '.'+um+um+um+'.'
			a39 = ur+us+'_'+um
			a40 = ur+ur+us+um
			abd = (a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15, a16, a17, a18, a19, a20, a21, a22, a23, a24, a25, a26, a27, a28, a29, a30, a31, a32, a33, a34, a35, a36, a37, a38, a39, a40)
			usery = random.choice(abd)
	 	url = 'https://i.instagram.com/api/v1/accounts/create/'
	 	he = {
	'Content-Length': '437',
	'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
	'Host': 'i.instagram.com',
	'Connection': 'Keep-Alive',
	'User-Agent': 'Instagram 6.12.1 Android (30/11; 480dpi; 1080x2298; HONOR; ANY-LX2; HNANY-Q1; qcom; en_IQ)',
	'Cookie': 'mid=Y16iBgABAAFggfUYwajggkGFz-hs',
	'Cookie2': '$Version=1',
	'Accept-Language': 'en-IQ, en-US',
	'X-IG-Connection-Type': 'WIFI',
	'X-IG-Capabilities': 'AQ==',
	'Accept-Encoding': 'gzip',}
		
	 	from uuid import uuid4
	 	da = {
	 	"email":"zodhok@gmail.com",
	 	"username":f"{usery}",
	 	"password":"zxcvbm1@"+usery,
	 	"device_id":"android-"+str(uuid4()),
	 	"guid":str(uuid4()),
	 	}		
	 	rr = requests.post(url,headers=he,data=da).text
	 	#print(rr)
	 	#exit()
	 	if "username" in rr:
	 		zok+=1
	 		print(f' {zok} : BaD uSeR : {usery}')
	 	elif 'email_is_taken' in rr:
	 		
	 		zok+=1
	 		print(rr)
	 		print(f' {zok} : DoNe uSeR : {usery}')
	       abood = """
𝖽𝗈𝗇𝖾 𝗎𝗌𝖾𝗋 𝖼𝗅𝗂𝗆𝖾𝖽 </>
⦗ 𝗎𝗌𝖾𝗋 ⦘ | ⦗ @{usery} ⦘
⦗ 𝗉𝗋𝗈𝗀𝗋𝖺𝗆𝗆𝖾𝗋 ⦘ | ⦗ @kckkkkc ⦘
"""
	 		requests.post(f"https://api.telegram.org/bot{token}/sendvideo?chat_id={iD}&video=https://t.me/m_aBd/14&caption="+str(abood))
	 	else:
	 		zok+=1
	 		print(f' {zok} : Bad User : {usery}')
 		
 	except:
 		zz()
 
while True:
	zz()