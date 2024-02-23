import requests

logo =f""" 
          <Welcome To Session Tool>             ╔════════════════════════════════════════╗
║      <\> Programmer : @kckkkkc         ║
║      <\> iG : @kkkcckc                 ║         ╚════════════════════════════════════════╝
""" ; print(logo)

user = input("EnTeR uSer : ")
pess = input("EnTeR Pass : ")

url='https://www.instagram.com/accounts/login/ajax/'
h={
	'accept': '*/*',
	'accept-encoding': 'gzip, deflate, br',
	'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
	'content-length': '291',
	'content-type': 'application/x-www-form-urlencoded',
	'cookie': 'ig_did=3E70DB93-4A27-43EB-8463-E0BFC9B02AE1; mid=YCAadAALAAH35g_7e7h0SwBbFzBt; ig_nrcb=1; csrftoken=COmXgzKurrq8awSnRS1xf3u9rL6QsGZI',
	'origin': 'https://www.instagram.com',
	'referer': 'https://www.instagram.com/',
	'sec-fetch-dest': 'empty',
	'sec-fetch-mode': 'cors',
	'sec-fetch-site': 'same-origin',
	'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
	'x-csrftoken': 'COmXgzKurrq8awSnRS1xf3u9rL6QsGZI',
	'x-ig-app-id': '936619743392459',
	'x-ig-www-claim': '0',
	'x-instagram-ajax': '1cb44f68ffec',
	'x-requested-with': 'XMLHttpRequest'}
data={
	'username': user,
	'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:1613414957:{pess}', 
	'queryParams': '{}',
	'optIntoOneTap': 'false'}
    
req=requests.post(url,headers=h,data=data)
	
if '"authenticated":true' in req.text:
	print('Done login')
	sessd=req.cookies['sessionid']
	print(sessd)

else:
	print("error login check password or user ?")
	