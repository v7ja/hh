import telebot,random,requests
from telebot import types


TELEGRAM_TOKEN = "6850670800:AAFZfcHNyobbCPmreG4GPPs63mjBl_YxuuI"
bot = telebot.TeleBot(TELEGRAM_TOKEN, threaded=False)




def os_id(id):
	res = False
	fiel = open("ids.txt","r")
	for lien in fiel:
		if lien.strip()==id:
			res =True
	fiel.close()
	return res

@bot.message_handler(commands=['start'])
def send_welcome(message):
	idu = message.from_user.id
	nam = message.from_user.first_name
	us = message.from_user.username
	f = open("ids.txt","a")
	if (not os_id(str(idu))):
		try:
			co2 = open("idco.txt","r").read()
		except:
			co2 ='1'
			with open('idco.txt', 'w') as x:
				x.write("1")
		with open('idco.txt', 'w') as x:
			if co2 == '':
				 x.write("1")
			else:
				co1 =int(co2)
				co1+=1
				x.write(str(co1))
		f.write(f'{idu}\n')
		f.close()
		ide = '1395609507'
		co3 = open("idco.txt","r").read()
		fg = bot.send_message(ide,f"""تم دخول شخص جديد :{co3}
	        ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉
	        ❂ - 𝚄𝚂𝙴𝚁 ⟿ @{us} 🤍..
	        ❂ - 𝙸𝙳 𝚂𝚃𝙰 ⟿ {idu} 🤍.  
	        ❂ - NAME 𝚂𝚃𝙰 ⟿ {nam} 🤍.  
	        ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉	        
	        """)		
	cec = f'https://api.telegram.org/bot[Token]/getChatMember?chat_id=@DIBIBl&user_id={idu}'
	status = requests.get(cec).json()["result"]["status"]
	if status =="member" or status =="creator" or status =="administrator":
		cec2 = f'https://api.telegram.org/bot[Token]/getChatMember?chat_id=@TDTDI&user_id={idu}'
		status2 = requests.get(cec2).json()["result"]["status"]
		if status2 =="member" or status2 =="creator" or status2 =="administrator": 
			mas = types.InlineKeyboardMarkup(row_width=1)
			F = types.InlineKeyboardButton("اضغط هنا للأشتراك", url='https://youtube.com/channel/UCUNbzQRjfAXGCKI1LY72DTA')
			mas.add(F)
			hh=bot.reply_to(message,"""- عَليڪ ﺄلاشتراك بقناة ﺂلبوت الاولى لڪِي يَعـمل البوت ⤹
	
	⟨ https://youtube.com/channel/UCUNbzQRjfAXGCKI1LY72DTA ⟩
	
	اشترك ثم اضغط /start من جَديد""",reply_markup=mas)
			bot.register_next_step_handler(hh,boten)
		else:
			mas = types.InlineKeyboardMarkup(row_width=1)
			F = types.InlineKeyboardButton("اضغط هنا للأشتراك", url='https://t.me/TDTDI')
			mas.add(F)
			bot.reply_to(message,"""- عَليڪ ﺄلاشتراك بقناة ﺂلبوت الاولى لڪِي يَعـمل البوت ⤹
	
	⟨ @TDTDI ⟩
	
	اشترك ثم اضغط /start من جَديد""",reply_markup=mas)							
	elif status =="left":
		mas = types.InlineKeyboardMarkup(row_width=1)
		F = types.InlineKeyboardButton("اضغط هنا للأشتراك", url='https://t.me/DIBIBl')
		mas.add(F)
		bot.reply_to(message,"""- عَليڪ ﺄلاشتراك بقناة ﺂلبوت الاولى لڪِي يَعـمل البوت ⤹

⟨ @DIBIBl ⟩

اشترك ثم اضغط /start من جَديد""",reply_markup=mas)
		
def boten(message):
	nam = message.from_user.first_name
	mas = types.InlineKeyboardMarkup(row_width=1)
	A = types.InlineKeyboardButton("ѕᴛᴀʀᴛ ", callback_data="F1")
	B = types.InlineKeyboardButton("𝖽𝖾𝗏𝖾𝗅𝗈𝗉𝖾𝗋 𖠛", url='https://t.me/DIBIBl')
	mas.add(A,B)
	bot.send_message(message.chat.id, f"""⧐ اهلا بڪ َ{nam} في بوت  𝗹𝗶𝘀𝘁 𝗺𝗮𝗸𝗲𝗿 .
		⧐ يمكنك تحميل لستات بكل سهولة .
		⧐ المبرمج (@ruks3) (@DIBIBl) .""",reply_markup=mas)
@bot.callback_query_handler(func=lambda call:True )    
def sdd(call):	
	if call.data =='F1':
		mas = types.InlineKeyboardMarkup(row_width=2)
		A = types.InlineKeyboardButton("𝗹𝗶𝘀𝘁 𝘂𝘀𝗲𝗿", callback_data="F")
		B = types.InlineKeyboardButton("𝗹𝗶𝘀𝘁 𝗲𝗺𝗮𝗶𝗹", callback_data="F2")
		C = types.InlineKeyboardButton("𝗰𝗼𝗺𝗯𝗼 𝘂𝘀𝗲𝗿", callback_data="F3")
		D = types.InlineKeyboardButton("𝗰𝗼𝗺𝗯𝗼 𝗲𝗺𝗮𝗶𝗹", callback_data="F4")
		F = types.InlineKeyboardButton("𝖽𝖾𝗏𝖾𝗅𝗈𝗉𝖾𝗋 𖠛", url='https://t.me/DIBIBl')
		mas.add(A,B,C,D,F)
		bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="𝐜𝐡𝐨𝐨𝐬𝐞 𝐨𝐧𝐞 𝐨𝐟 𝐭𝐡𝐞 𝐛𝐮𝐭𝐭𝐨𝐧𝐬 𝄵",reply_markup=mas)		
		pass
	elif call.data =="F4":
		mas = types.InlineKeyboardMarkup(row_width=2)
		A = types.InlineKeyboardButton("𝗴𝗺𝗮𝗶𝗹", callback_data="Dg")
		B = types.InlineKeyboardButton("𝗵𝗼𝘁𝗺𝗮𝗶𝗹", callback_data="Dh")
		C = types.InlineKeyboardButton("𝗼𝘂𝘁𝗹𝗼𝗼𝗸", callback_data="Do")
		D = types.InlineKeyboardButton("𝘆𝗮𝗵𝗼𝗼", callback_data="Dy")
		H = types.InlineKeyboardButton("𝗺𝗮𝗶𝗹.𝗿𝘂", callback_data="Dm")
		G = types.InlineKeyboardButton("𝗿𝗮𝗻𝗱𝗼𝗺", callback_data="Dr")		
		F = types.InlineKeyboardButton("𝗯𝗮𝗰𝗸 𝆹𝅥𝅮", callback_data="F1")
		mas.add(A,B,C,D,H,G,F)
		bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="𝐜𝐡𝐨𝐨𝐬𝐞 𝐨𝐧𝐞 𝐨𝐟 𝐭𝐡𝐞 𝐛𝐮𝐭𝐭𝐨𝐧𝐬 𝄵",reply_markup=mas)
	elif call.data =="Dg" or call.data =="Dh" or call.data =="Do" or call.data =="Dy" or call.data =="Dm" or call.data =="Dr":
		rr=('5','6','7','8','9','10','11','12','13','14')
		pp=('5','6','7','8','9','10',)
		rdom=('@gmail.com','@hotmail.com','@outlook.com','@yahoo.com','mail.ru')
		dome1 =""
		if call.data =="Dg":
			dome= '@gmail.com'
		elif call.data =="Dh":
			dome='@hotmail.com'
		elif call.data =="Do":
			dome='@outlook.com'
		elif call.data =="Dy":
			dome='@yahoo.com'
		elif call.data =="Dm":
			dome='mail.ru'
		elif call.data =="Dr":
			dome1='ren'
		for i in range(1000):
			if dome1 =='ren':
				dome = str("".join(random.choice(rdom)for i in range(1)))
			ruku = str("".join(random.choice(rr)for i in range(1)))
			rukus = str("".join(random.choice('1234567890qwertyuiopasdfghjklmnbvcxz')for i in range(int(ruku))))
			rupa = str("".join(random.choice(pp)for i in range(1)))
			pas =str("".join(random.choice('1234567890qwertyuiopasdfghjklmnbvcxz')for i in range(int(rupa))))
			email =(f"{rukus}{dome}:{pas}")
			with open('email-combo12-ruks.txt', 'a') as x:
				x.write(email+ '\n')
		bot.send_document(call.message.chat.id,open('email-combo12-ruks.txt', 'rb'))
		with open('email-combo12-ruks.txt', 'w') as x:
			x.write("")
		mas = types.InlineKeyboardMarkup(row_width=1)
		A = types.InlineKeyboardButton("𝗯𝗮𝗰𝗸 𝆹𝅥𝅮", callback_data="F1")			
		F = types.InlineKeyboardButton("𝖽𝖾𝗏𝖾𝗅𝗈𝗉𝖾𝗋 𖠛", url='https://t.me/DIBIBl')
		mas.add(A,F)
		bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="𝘁𝗵𝗮𝗻𝗸 𝘆𝗼𝘂 𝗳𝗼𝗿 𝘂𝘀𝗶𝗻𝗴 𝘆𝗼𝘂 𝗰𝗮𝗻 𝗰𝗼𝗺𝗲 𝗯𝗮𝗰𝗸 𖤍",reply_markup=mas)
		pass
	elif call.data =="F3":
		mas = types.InlineKeyboardMarkup(row_width=2)
		A = types.InlineKeyboardButton("𝗰𝗵𝗮𝗿𝗮𝗰𝘁𝗲𝗿 𝗰𝗼𝘂𝗻𝘁 2", callback_data="c2")
		B = types.InlineKeyboardButton("𝗰𝗵𝗮𝗿𝗮𝗰𝘁𝗲𝗿 𝗰𝗼𝘂𝗻𝘁 3", callback_data="c3")
		C = types.InlineKeyboardButton("𝗰𝗵𝗮𝗿𝗮𝗰𝘁𝗲𝗿 𝗰𝗼𝘂𝗻𝘁 4", callback_data="c4")
		D = types.InlineKeyboardButton("𝗰𝗵𝗮𝗿𝗮𝗰𝘁𝗲𝗿 𝗰𝗼𝘂𝗻𝘁 5", callback_data="c5")
		F = types.InlineKeyboardButton("𝗯𝗮𝗰𝗸 𝆹𝅥𝅮", callback_data="F1")
		mas.add(A,B,C,D,F)
		bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="𝐜𝐡𝐨𝐨𝐬𝐞 𝐨𝐧𝐞 𝐨𝐟 𝐭𝐡𝐞 𝐛𝐮𝐭𝐭𝐨𝐧𝐬 𝄵",reply_markup=mas)
	elif call.data =="c2" or call.data =="c3" or call.data =="c4" or call.data =="c4" or call.data =="c5":
		if call.data =="c2":
			rr=('5','6','7','8','9','10','11','12','13','14')
			for i in range(1000):
				us=str("".join(random.choice('1234567890qwertyuiopasdfghjklmnbvcxz')for i in range(2)))
				ra =str("".join(random.choice(rr)for i in range(1)))
				pas =str("".join(random.choice('1234567890qwertyuiopasdfghjklmnbvcxz')for i in range(int(ra))))
				user=(f"{us}:{pas}")
				with open('user-combo2-ruks.txt', 'a') as x:
					x.write(user+ '\n')
			bot.send_document(call.message.chat.id,open('user-combo2-ruks.txt', 'rb'))
			with open('user-combo2-ruks.txt', 'w') as x:
				x.write('')
			mas = types.InlineKeyboardMarkup(row_width=1)
			A = types.InlineKeyboardButton("𝗯𝗮𝗰𝗸 𝆹𝅥𝅮", callback_data="F1")			
			F = types.InlineKeyboardButton("𝖽𝖾𝗏𝖾𝗅𝗈𝗉𝖾𝗋 𖠛", url='https://t.me/DIBIBl')
			mas.add(A,F)
			bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="𝘁𝗵𝗮𝗻𝗸 𝘆𝗼𝘂 𝗳𝗼𝗿 𝘂𝘀𝗶𝗻𝗴 𝘆𝗼𝘂 𝗰𝗮𝗻 𝗰𝗼𝗺𝗲 𝗯𝗮𝗰𝗸 𖤍",reply_markup=mas)			
		if call.data =="c3":
			rr=('5','6','7','8','9','10','11','12','13','14')
			for i in range(1000):
				us=str("".join(random.choice('1234567890qwertyuiopasdfghjklmnbvcxz')for i in range(3)))
				ra=str("".join(random.choice(rr)for i in range(1)))
				pas =str("".join(random.choice('1234567890qwertyuiopasdfghjklmnbvcxz')for i in range(int(ra))))
				user=(f"{us}:{pas}")
				with open('user-combo3-ruks.txt', 'a') as x:
					x.write(user+ '\n')				
			bot.send_document(call.message.chat.id,open('user-combo3-ruks.txt', 'rb'))
			with open('user-combo3-ruks.txt', 'w') as x:
				x.write('')
			mas = types.InlineKeyboardMarkup(row_width=1)
			A = types.InlineKeyboardButton("𝗯𝗮𝗰𝗸 𝆹𝅥𝅮", callback_data="F1")			
			F = types.InlineKeyboardButton("𝖽𝖾𝗏𝖾𝗅𝗈𝗉𝖾𝗋 𖠛", url='https://t.me/DIBIBl')
			mas.add(A,F)
			bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="𝘁𝗵𝗮𝗻𝗸 𝘆𝗼𝘂 𝗳𝗼𝗿 𝘂𝘀𝗶𝗻𝗴 𝘆𝗼𝘂 𝗰𝗮𝗻 𝗰𝗼𝗺𝗲 𝗯𝗮𝗰𝗸 𖤍",reply_markup=mas)				
		if call.data =="c4":
			rr=('5','6','7','8','9','10','11','12','13','14')
			for i in range(1000):
				us=str("".join(random.choice('1234567890qwertyuiopasdfghjklmnbvcxz')for i in range(4)))
				ra=str("".join(random.choice(rr)for i in range(1)))
				pas= str("".join(random.choice('1234567890qwertyuiopasdfghjklmnbvcxz')for i in range(int(ra))))
				user=(f"{us}:{pas}")
				with open('user-combo4-ruks.txt', 'a') as x:
					x.write(user+ '\n')
			bot.send_document(call.message.chat.id,open('user-combo4-ruks.txt', 'rb'))
			with open('user-combo4-ruks.txt', 'w') as x:
				x.write('')
			mas = types.InlineKeyboardMarkup(row_width=1)
			A = types.InlineKeyboardButton("𝗯𝗮𝗰𝗸 𝆹𝅥𝅮", callback_data="F1")			
			F = types.InlineKeyboardButton("𝖽𝖾𝗏𝖾𝗅𝗈𝗉𝖾𝗋 𖠛", url='https://t.me/DIBIBl')
			mas.add(A,F)
			bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="𝘁𝗵𝗮𝗻𝗸 𝘆𝗼𝘂 𝗳𝗼𝗿 𝘂𝘀𝗶𝗻𝗴 𝘆𝗼𝘂 𝗰𝗮𝗻 𝗰𝗼𝗺𝗲 𝗯𝗮𝗰𝗸 𖤍",reply_markup=mas)			
		if call.data =="c5":
			rr=('5','6','7','8','9','10','11','12','13','14')
			for i in range(1000):
				us=str("".join(random.choice('1234567890qwertyuiopasdfghjklmnbvcxz')for i in range(5)))
				ra=str("".join(random.choice(rr)for i in range(1)))
				pas =str("".join(random.choice('1234567890qwertyuiopasdfghjklmnbvcxz')for i in range(int(ra))))
				user=(f"{us}:{pas}")
				with open('user-combo5-ruks.txt', 'a') as x:
					x.write(user+ '\n')
			bot.send_document(call.message.chat.id,open('user-combo5-ruks.txt', 'rb'))
			with open('user-combo5-ruks.txt', 'w') as x:
				x.write('')
			mas = types.InlineKeyboardMarkup(row_width=1)
			A = types.InlineKeyboardButton("𝗯𝗮𝗰𝗸 𝆹𝅥𝅮", callback_data="F1")			
			F = types.InlineKeyboardButton("𝖽𝖾𝗏𝖾𝗅𝗈𝗉𝖾𝗋 𖠛", url='https://t.me/DIBIBl')
			mas.add(A,F)
			bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="𝘁𝗵𝗮𝗻𝗸 𝘆𝗼𝘂 𝗳𝗼𝗿 𝘂𝘀𝗶𝗻𝗴 𝘆𝗼𝘂 𝗰𝗮𝗻 𝗰𝗼𝗺𝗲 𝗯𝗮𝗰𝗸 𖤍",reply_markup=mas)
				
	elif call.data =="F2":
		mas = types.InlineKeyboardMarkup(row_width=2)
		A = types.InlineKeyboardButton("𝗴𝗺𝗮𝗶𝗹", callback_data="EMLg")
		B = types.InlineKeyboardButton("𝗵𝗼𝘁𝗺𝗮𝗶𝗹", callback_data="EMLh")
		C = types.InlineKeyboardButton("𝗼𝘂𝘁𝗹𝗼𝗼𝗸", callback_data="EMLo")
		D = types.InlineKeyboardButton("𝘆𝗮𝗵𝗼𝗼", callback_data="EMLy")
		H = types.InlineKeyboardButton("𝗺𝗮𝗶𝗹.𝗿𝘂", callback_data="EMLm")
		G = types.InlineKeyboardButton("𝗿𝗮𝗻𝗱𝗼𝗺", callback_data="rendom")		
		F = types.InlineKeyboardButton("𝗯𝗮𝗰𝗸 𝆹𝅥𝅮", callback_data="F1")
		mas.add(A,B,C,D,H,G,F)
		bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="𝐜𝐡𝐨𝐨𝐬𝐞 𝐨𝐧𝐞 𝐨𝐟 𝐭𝐡𝐞 𝐛𝐮𝐭𝐭𝐨𝐧𝐬 𝄵",reply_markup=mas)
	if call.data =="EMLg" or call.data =="EMLh" or call.data =="EMLo" or call.data =="EMLy" or call.data =="EMLm" or call.data =="rendom":
		rr=('5','6','7','8','9','10','11','12','13','14')
		rdom=('@gmail.com','@hotmail.com','@outlook.com','@yahoo.com','mail.ru')
		dom1=""	
		if call.data =="EMLg":
			dom ='@gmail.com'			
		elif call.data =="EMLh":
			dom ='@hotmail.com'
		elif call.data =="EMLo":
			dom='@outlook.com'
		elif call.data =="EMLy":
			dom='@yahoo.com'			
		elif call.data =="EMLm":
			dom ='mail.ru'			
		elif call.data =="rendom":
			dom1 ='re'		
		for i in range(1000):
			if dom1 =='re':				
				dom = str("".join(random.choice(rdom)for i in range(1)))
			ruku = str("".join(random.choice(rr)for i in range(1)))
			rukus = str("".join(random.choice('1234567890qwertyuiopasdfghjklmnbvcxz')for i in range(int(ruku))))
			mail = (f"{rukus}{dom}")
			with open('email-list-ruks.txt', 'a') as x:
				x.write(mail+ '\n')
		bot.send_document(call.message.chat.id,open('email-list-ruks.txt', 'rb'))
		with open('email-list-ruks.txt', 'w') as x:
			x.write("ruks")
		mas = types.InlineKeyboardMarkup(row_width=1)
		A = types.InlineKeyboardButton("𝗯𝗮𝗰𝗸 𝆹𝅥𝅮", callback_data="F1")			
		F = types.InlineKeyboardButton("𝖽𝖾𝗏𝖾𝗅𝗈𝗉𝖾𝗋 𖠛", url='https://t.me/DIBIBl')
		mas.add(A,F)
		bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="𝘁𝗵𝗮𝗻𝗸 𝘆𝗼𝘂 𝗳𝗼𝗿 𝘂𝘀𝗶𝗻𝗴 𝘆𝗼𝘂 𝗰𝗮𝗻 𝗰𝗼𝗺𝗲 𝗯𝗮𝗰𝗸 𖤍",reply_markup=mas)		
					
	elif call.data =="F":
		mas = types.InlineKeyboardMarkup(row_width=2)
		A = types.InlineKeyboardButton("𝗰𝗵𝗮𝗿𝗮𝗰𝘁𝗲𝗿 𝗰𝗼𝘂𝗻𝘁 2", callback_data="L2")
		B = types.InlineKeyboardButton("𝗰𝗵𝗮𝗿𝗮𝗰𝘁𝗲𝗿 𝗰𝗼𝘂𝗻𝘁 3", callback_data="L3")
		C = types.InlineKeyboardButton("𝗰𝗵𝗮𝗿𝗮𝗰𝘁𝗲𝗿 𝗰𝗼𝘂𝗻𝘁 4", callback_data="L4")
		D = types.InlineKeyboardButton("𝗰𝗵𝗮𝗿𝗮𝗰𝘁𝗲𝗿 𝗰𝗼𝘂𝗻𝘁 5", callback_data="L5")
		F = types.InlineKeyboardButton("𝗯𝗮𝗰𝗸 𝆹𝅥𝅮", callback_data="F1")
		mas.add(A,B,C,D,F)
		bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="𝐜𝐡𝐨𝐨𝐬𝐞 𝐨𝐧𝐞 𝐨𝐟 𝐭𝐡𝐞 𝐛𝐮𝐭𝐭𝐨𝐧𝐬 𝄵",reply_markup=mas)
	if call.data =="L2" or call.data =="L3" or call.data =="L4" or call.data =="L5":
		if call.data =="L2":
			for i in range(1000):
				user = str("".join(random.choice("qwertyuiopasdfghjklzxcvbnm1234567890")for i in range(2)))
				with open('user-list2-ruks.txt', 'a') as x:
					x.write(user+ '\n')
			bot.send_document(call.message.chat.id,open('user-list2-ruks.txt', 'rb'))
			with open('user-list2-ruks.txt', 'w') as x:
				x.write("")
			mas = types.InlineKeyboardMarkup(row_width=1)
			A = types.InlineKeyboardButton("𝗯𝗮𝗰𝗸 𝆹𝅥𝅮", callback_data="F1")			
			F = types.InlineKeyboardButton("𝖽𝖾𝗏𝖾𝗅𝗈𝗉𝖾𝗋 𖠛", url='https://t.me/DIBIBl')
			mas.add(A,F)
			bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="𝘁𝗵𝗮𝗻𝗸 𝘆𝗼𝘂 𝗳𝗼𝗿 𝘂𝘀𝗶𝗻𝗴 𝘆𝗼𝘂 𝗰𝗮𝗻 𝗰𝗼𝗺𝗲 𝗯𝗮𝗰𝗸 𖤍",reply_markup=mas)		
			
		elif call.data =="L3":
			for i in range(1000):
				user = str("".join(random.choice("qwertyuiopasdfghjklzxcvbnm1234567890")for i in range(3)))
				with open('user-list3-ruks.txt', 'a') as x:
					x.write(user+ '\n')
			bot.send_document(call.message.chat.id,open('user-list3-ruks.txt', 'rb'))
			with open('user-list3-ruks.txt', 'w') as x:
				x.write('ruks')
			mas = types.InlineKeyboardMarkup(row_width=1)
			A = types.InlineKeyboardButton("𝗯𝗮𝗰𝗸 𝆹𝅥𝅮", callback_data="F1")			
			F = types.InlineKeyboardButton("𝖽𝖾𝗏𝖾𝗅𝗈𝗉𝖾𝗋 𖠛", url='https://t.me/DIBIBl')
			mas.add(A,F)
			bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="𝘁𝗵𝗮𝗻𝗸 𝘆𝗼𝘂 𝗳𝗼𝗿 𝘂𝘀𝗶𝗻𝗴 𝘆𝗼𝘂 𝗰𝗮𝗻 𝗰𝗼𝗺𝗲 𝗯𝗮𝗰𝗸 𖤍",reply_markup=mas)		
		elif call.data =="L4":
			for i in range(1000):
				user = str("".join(random.choice("qwertyuiopasdfghjklzxcvbnm1234567890")for i in range(4)))
				with open('user-list4-ruks.txt', 'a') as x:
					x.write(user+ '\n')
			bot.send_document(call.message.chat.id,open('user-list4-ruks.txt', 'rb'))
			with open('user-list4-ruks.txt', 'w') as x:
				x.write("")
			mas = types.InlineKeyboardMarkup(row_width=1)
			A = types.InlineKeyboardButton("𝗯𝗮𝗰𝗸 𝆹𝅥𝅮", callback_data="F1")			
			F = types.InlineKeyboardButton("𝖽𝖾𝗏𝖾𝗅𝗈𝗉𝖾𝗋 𖠛", url='https://t.me/DIBIBl')
			mas.add(A,F)
			bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="𝘁𝗵𝗮𝗻𝗸 𝘆𝗼𝘂 𝗳𝗼𝗿 𝘂𝘀𝗶𝗻𝗴 𝘆𝗼𝘂 𝗰𝗮𝗻 𝗰𝗼𝗺𝗲 𝗯𝗮𝗰𝗸 𖤍",reply_markup=mas)
		elif call.data =="L5":
			for i in range(1000):
				user = str("".join(random.choice("qwertyuiopasdfghjklzxcvbnm1234567890")for i in range(5)))
				with open('user-list5-ruks.txt', 'a') as x:
					x.write(user+ '\n')
			bot.send_document(call.message.chat.id,open('user-list5-ruks.txt', 'rb'))
			with open('user-list5-ruks.txt', 'w') as x:
				x.write("")
			mas = types.InlineKeyboardMarkup(row_width=1)
			A = types.InlineKeyboardButton("𝗯𝗮𝗰𝗸 𝆹𝅥𝅮", callback_data="F1")			
			F = types.InlineKeyboardButton("𝖽𝖾𝗏𝖾𝗅𝗈𝗉𝖾𝗋 𖠛", url='https://t.me/DIBIBl')
			mas.add(A,F)
			bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="𝘁𝗵𝗮𝗻𝗸 𝘆𝗼𝘂 𝗳𝗼𝗿 𝘂𝘀𝗶𝗻𝗴 𝘆𝗼𝘂 𝗰𝗮𝗻 𝗰𝗼𝗺𝗲 𝗯𝗮𝗰𝗸 𖤍",reply_markup=mas)			
if __name__ == '__main__':
	bot.polling(none_stop=True)   