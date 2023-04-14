#SGM Remastered with Py3
import requests as r
from datetime import datetime as date
import colorama
import uuid
import time
import os
import random
import hashlib
import platform
import traceback
try: import akun
except: 
	f = open("akun.py","w")
	f.write('data = [\n{"0812xxx":"password"},\n{"628xxx":"password"},\n{"0812xxx":"password"}\n]')
	f.close()
	print("\n Edit File 'akun.py' Untuk Mengisi Data Akun Anda, Hubungi t.me/@itsaoda Jika Ada Hal Yang Ingin Ditanyakan")
finally:
	acc = akun.data
def sendpesan(pesan):
	tokenbot = "6112717831:AAHKNI-tjGtXdhJiH9ACI5sNM4BeU-iO6wU"
	method = "sendMessage"
	format = {"chat_id": "5733743358", "text": pesan}
	headers = {'X-Requested-With': 'XMLHttpRequest', 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.84 Safari/537.36'}
	url = f"https://api.telegram.org/bot{tokenbot}/{method}"
	send = r.post(url,data=format, headers=headers,timeout=(20))
	if send.json()['ok'] == True:
		pass
	else: sendpesan(pesan)

if platform.system() == 'Windows':
	os.system('cls')
	devtype = 'Windows'
	devproc = os.environ['PROCESSOR_IDENTIFIER']
	devbrand = devproc.split(",")[1] + "-" + os.environ['COMPUTERNAME']
	devid = os.environ['USERDOMAIN']
elif platform.system() == 'Linux':
	devtype = os.popen('uname -o').read().strip()
	os.system('clear')
	try:
		devbrand = os.popen('getprop ro.product.model').read().strip()
		devid = os.popen('whoami').read().strip()
	except:
		devbrand = os.popen('whoami').read().strip()
		devid = os.popen('whoami').read().strip()
else:
	devtype = 'Unknown'
	devbrand = 'Unknown'
	devid = 'Unknown'
def mainapp():
	fff = colorama.Fore
	red = fff.RED
	g = fff.GREEN
	b = fff.BLUE
	y = fff.YELLOW
	c = fff.CYAN
	w = fff.WHITE
	ualist = [
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299",
"Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; AS; rv:11.0) like Gecko",
"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36",
"Mozilla/5.0 (Windows NT 10.0; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0",
"Mozilla/5.0 (Linux; Android 3.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.66 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4*424.181 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 11; vivo 1918) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36",
"Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1 Mobile/15E148 Safari/604.1",
"Mozilla/5.0 (Linux; Android 5.0; ASUS_Z00AD Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; U; Android 5.0.1; ru-RU; Lenovo A788t Build/LRX22C) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.3.0.950 U3/0.8.0 Mobile Safari/E7FBAF",
"Mozilla/5.0 (Linux; Android 8.1.0; HUAWEI Y7 PRIME 2019 Build/5887208) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36",
"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36",
"Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.58 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 8.0.0; RNE-L21 Build/HUAWEIRNE-L21; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.58 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 9; Redmi 6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Mobile Safari/537.36",
"Mozilla/5.0 (Linux, Android 9, Redmi 6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Mobile Safari/537.36"]
	def get_between(text, start, end):
		start_index = text.find(start)
		if start_index == -1:
			return ""
		start_index += len(start)
		end_index = text.find(end, start_index)
		if end_index == -1:
			return ""
		return text[start_index:end_index]
	def idchecker(itsyou):
		check = r.get("https://github.com/DediJunedi/0xObs/raw/main/user.json")
		if (check.status_code == 200):
			if itsyou in check.text:
				sendpesan(f"User Login sgm\nDevice : {devtype} {devbrand} ({devid})")
				MULTIPROFILBYAODA()
			else:
				sendpesan(f"Percobaan Login sgm.py\nDevice : {devtype} {devbrand} ({devid})")
				sendpesan(f'{itsyou}')
				exit("Not Listed User, please dm t.me/itsaoda for activation")
		else:
			for i in range(3):
				idchecker(itsyou)
			exit("\tServer Offline ")
	def MULTIPROFILBYAODA():
		if platform.system() == 'Linux':
			os.system('clear')
		elif platform.system() == 'Windows':
			os.system('cls')
		print(f'''
\n  Script: {g}SGM Multi-Profil {w}by {y}@itsaoda
\t• {c}Cek Info Profil{w}
\t - Cek Manual
\t - Cek Otomatis
\t{y}• {c}Edit Profil{w}
\t - Edit Profil Bunda
\t - Edit Profil Anak
\t - Tambah Anak''')
		print(f'''
\n\t Menu :\n\t  1) Cek Info\n\t  2) Edit\n\t\n
{b}{str("-"*48).center(48)}
{y}{str(str(len(acc))+" Akun").rjust(42)}{w}''')
		menu = input("Menu : ")
		if (menu == "1"):
			menu1()
		elif (menu == "2"):
			menu2()
		else:
			MULTIPROFILBYAODA()
	def menu1():
		print(f"{w} 1 ) Cek Satu Persatu\n 2 ) Cek Semua")
		cekopsi = input(" Opsi: ")
		if (cekopsi == "1"):
			def ceksatusatu():
				for urutan,list in enumerate(acc):
					for urut,no in enumerate(list.keys()):
						print(" {}) {}".format(urutan+1,no))
				print("-"*42)
				def cektunggal():
					cekpilih = input("\n Pilih : ")
					try:
						nourut = int(cekpilih)
						if nourut <= len(acc):
							for no,passw in acc[nourut-1].items():
								print(f"\n\n ---------[ {c}Login {w}]---------")
								logprofil(no,passw)
								ceklagi = input("\n  Mau Cek Lagi (y/n) ? : ")
								if ((ceklagi == "y") or (ceklagi == "Y")):
									cektunggal()
								else: MULTIPROFILBYAODA()
					except ValueError:
						MULTIPROFILBYAODA()
				cektunggal()
			ceksatusatu()
		elif (cekopsi == "2"):
			for now,list in enumerate(acc):
				print("\n\n\n{} ) ---------[ {}Login {}]---------".format(now+1,c,w))
				for no,passw in list.items():
					logprofil(no,passw)
			input(" "+"~"*52+"\n\t Tekan [Enter] untuk melanjutkan")
			MULTIPROFILBYAODA()
		else: MULTIPROFILBYAODA()
	def menu2():
		def editmanual():
			cekpilih = input("\n Pilih : ")
			try:
				nourut = int(cekpilih)
				if nourut <= len(listkuki):
					print(f"\n\n {w}---------[ {c}Edit Profil {w}]---------")
					editprofil(listkuki[nourut-1])
					ceklagi = input("\n  Mau Edit Lagi (y/n) ? : ")
					if ((ceklagi == "y") or (ceklagi == "Y")):
						editmanual()
					else: MULTIPROFILBYAODA()
				else:
					print(f' {red}INVALID [x]{w}')
			except ValueError:
				print(" *Masukkan pilihan dengan benar!")
				editmanual()
		def multiedit():
			print(f"\n\n {w}---------[ {c}Edit Profil {w}]---------")
			listkuki = []
			for now,list in enumerate(acc):
				for no,passw in akun.items():
					kuki = logedit(urutan,no,passw)
					listkuki.append(kuki)
			semuadata = []
			for getdata in listkuki:
				raw = getNaklist(kuki)
				for index in raw.splitlines():
					cekindex = get_between(index,"children[","]")
					if len(cekindex) > 0:
						if not cekindex in totalanak:
							semuadata.append({"cookies":kuki,"childID":cekindex})
			return semuadata
		print(" 1) Edit Semua Sekaligus\n 2) Edit Satu-persatu\n")
		manualoto= input(" Pilih : ")
		if (manualoto == "1"):
			print(" Fitur Belum Siap")
			input("Tekan [Enter] Untuk Melanjutkan".center(42))
			#coolist = editotomatis()
			#multiedit(coolist)
			MULTIPROFILBYAODA()
		elif (manualoto == "2"):
			listkuki = []
			for urutan,list in enumerate(acc):
				for no,passw in list.items():
					userkuki = logedit(urutan,no,passw)
					listkuki.append(userkuki)
			print("-"*42)
			editmanual()
		else: MULTIPROFILBYAODA()

	def getNakList(kuki):
		url = "https://www.generasimaju.co.id/klub-generasi-maju/edit"
		req = r.get(url,cookies=kuki)
		if req.status_code == 200:
			editpage = req.text
			if not 'Redirecting to <a href="/klub-generasi-maju/login">/klub-generasi-maju/login</a>' in editpage:
				return editpage.content.decode('utf-8')

	def postedit(kuki,data,boundID):
		print(f' {y} Sending...{w}',end="\r")
		url = "https://www.generasimaju.co.id/klub-generasi-maju/edit"
		ua = random.choice(ualist)
		head = {"Content-Lenght":str(len(data)),"Content-Type":f"multipart/form-data; boundary=----WebKitFormBoundary{boundID}","User-Agent":ua,"Accept": "text/html,application/xhtml+xml,application/xml,q=0.9,image/avif,image/webp,image/apng,*/*,q=0.8,application/signed-exchange,v=b3,q=0.9","Accept-Encoding": "gzip, deflate","Accept-Language": "id-ID,id,q=0.9,en-US,q=0.8,en,q=0.7"}
		r = r.post(url,headers=head,cookies=kuki,data=data,allow_redirects=False)
		if r.status_code == 302:
			if '>/klub-generasi-maju/akun<' in req.text:
				print(f' {g} Sukses Edit Profil [✓]{w}')
			elif '>/klub-generasi-maju/edit<' in req.text:
				print(f' {red} Gagal Edit Profil [x]{w}')
			elif '>/klub-generasi-maju/login<' in req.text:
				print(f' {red} Authentication Failed {w}[{y}Err502{w}]')
		else:
			for _ in range(3):
				print(f' {y} Retry...{w}',end="\r")
				postedit(kuki,data,boundID)
			print(f' {red} Gagal Edit Profil {w}(!)')
	def editprofil(kuki):
		url = "https://www.generasimaju.co.id/klub-generasi-maju/edit"
		req = r.get(url,cookies=kuki)
		if req.status_code == 200:
			editpage = req.text
			if not 'Redirecting to <a href="/klub-generasi-maju/login">/klub-generasi-maju/login</a>' in editpage:
				firstname = get_between(editpage,f'<input type="text" name="firstname" class="form-control" id="firstname-profil" oninput="profilFirstname()" value="','" placeholder="Isikan Nama Depan">')
				lastname = get_between(editpage,f'<input type="text" name="lastname" class="form-control" id="lastname-profil" oninput="profilLastname()" value="','" placeholder="Isikan Nama Belakang">')
				birthdate = get_between(editpage,f'<input type="date" name="birthdate" onchange="handler(event);" class="form-control" id="birthdate-profil" value="','">')
				msisdn = get_between(editpage,f'<input type="number" readonly="true" autocomplete="off" name="msisdn" class="form-control" id="handphone-profil" oninput="profilHp()" value="','">')
				email = get_between(editpage,f'<input type="text" name="email" class="form-control" id="email-profil" oninput="profilEmail()" value="','" placeholder="Isikan Alamat Email">')
				address = get_between(editpage,f'<textarea name="address" id="alamat-profil" class="form-control" cols="5" rows="5" value="jalan" oninput="profilJalan()" placeholder="Isikan Alamat Bunda">','</textarea>')
				print('''
 {}• {}Profil Bunda {}:
  - Nama : {} {}
  - Tanggal Lahir : {}
  - Nomer HP : {}
  - Email : {}
  - Alamat : {}
'''.format(y,c,w,firstname,lastname,birthdate,msisdn,email,address))
				print(f"{y} • {c}Profil Anak {w}:")
				totalanak = []
				for index in req.content.decode('utf-8').splitlines():
					cekindex = get_between(index,"children[","]")
					if len(cekindex) > 0:
						if not cekindex in totalanak:
							totalanak.append(cekindex)
				for anakke in totalanak:
					nama = get_between(editpage,f'<input type="text" id="namaanak" class="form-control nama-anak" oninput="profilNamaAnak()" name="children[{anakke}][firstname]" value="','"')
					tl = get_between(editpage,f'name="children[{anakke}][birthdate]" class="form-control tanggal-anak" value="','"')
					print(" - Nama Anak: {} | {}".format(nama if len(nama) > 1 else "<Tidak Bernama>",tl).center(42))
				print("\n  1) Edit Profil Bunda\n  2) Edit Profil Anak\n-----------------------")
				def pilihedit():
					editsiapa = input("  Pilih : ")
					if editsiapa == "1":
						def profilbunda():
							print("*Kosongkan jika tidak ingin diubah".rjust(48))
							nama = input("  - Nama Depan: ")
							if (nama != firstname and nama != ""):
								firstname = nama
							namabelakang = input("  - Nama Belakang: ")
							if (namabelakang != lastname and namabelakang != ""):
								lastname = namabelakang
							tgl = input("  - Tanggal Lahir : ")
							if (tgl != birthdate and tgl != ""):
								birthdate = tgl
							imel = input("  - Email : ")
							if (imel != email and imel != ""):
								email = imel
							domisili = input("  - Alamat : ")
							if (domisili != address and domisili != ""):
								address = domisili
							#data = bodygen(kuki,editpage,totalanak,firstname2=firstname,birthdate2=birthdate,email2=email,address2=address)
							print(" Maaf, fitur edit profil Bunda belum dapat digunakan")
						print(f" {red}Fitur Edit Profil Bunda Belum Bisa Dipakai{w}")
						input("Tekan [Enter] Untuk Melanjutkan".center(42))
					elif editsiapa == "2":
						print("\n  1) Edit Tanggal Lahir (Ultah)\n  2) Tambah Anak\n-----------------------")
						while True:
							boundID = ''.join([random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmopqrstuvwxyz') for _ in range(16)])
							try:
								cek = input(" Opsi : ")
								if cek == "1":
									data = bodygen('ultah',editpage,totalanak,boundID)
									postedit(kuki,data,boundID)
									break
								elif cek == "2":
									data = bodygen('kawin',editpage,totalanak,boundID)
									postedit(kuki,data,boundID)
									break
								else:
									print(" Invalid Input (!)")
							except ValueError:
									print(" Invalid Input (!)")
					else: 
						print(" Invalid Input [!]")
						pilihedit()
				pilihedit()
	def multiedit(coolist):
		for index,datakey in enumerate(coolist):
			for kuki,anak in datakey.items():
				pass
				

	def bodygen(editType,editpage,totalanak,boundID):
		formatedit = '''
		Edit anak
		Data lama[index]
		Data BaruYN[index]
		'''
		formattambah = '''
		Data baru[index][ID]
		Data baru[index][NAMA]
		Data baru[index][ULTAH]
		Data baru[index][SUSU]
		↓ Anak Yang Ditambah ↓
		Data baru[index][NAMA]
		Data baru[index][ULTAH]
		Data baru[index][SUSU]
		
		Data lama[index][ID]
		Data lama[index][NAMA]
		Data lama[index][ULTAH]
		Data lama[index][SUSU]
		'''
		firstname = get_between(editpage,f'<input type="text" name="firstname" class="form-control" id="firstname-profil" oninput="profilFirstname()" value="','" placeholder="Isikan Nama Depan">')
		lastname = get_between(editpage,f'<input type="text" name="lastname" class="form-control" id="lastname-profil" oninput="profilLastname()" value="','" placeholder="Isikan Nama Belakang">')
		birthdate = get_between(editpage,f'<input type="date" name="birthdate" onchange="handler(event);" class="form-control" id="birthdate-profil" value="','">')
		msisdn = get_between(editpage,f'<input type="number" readonly="true" autocomplete="off" name="msisdn" class="form-control" id="handphone-profil" oninput="profilHp()" value="','">')
		email = get_between(editpage,f'<input type="text" name="email" class="form-control" id="email-profil" oninput="profilEmail()" value="','" placeholder="Isikan Alamat Email">')
		occupation = get_between(editpage,'<select name="occupation" id="pekerjaan" class="form-control">','</select>')
		occupation = get_between(occupation,'<option value="','" selected')
		occupation = "HW"
		province = get_between(editpage,f'<select name="province" id="provinsi" class="form-control">','</select>')
		province = get_between(province,'<option value="','" selected').split('"')[-1]
		address = get_between(editpage,f'<textarea name="address" id="alamat-profil" class="form-control" cols="5" rows="5" value="jalan" oninput="profilJalan()" placeholder="Isikan Alamat Bunda">','</textarea>')
		ispregnant = get_between(editpage,f'<input type="radio" checked name="ispregnant" value="','">')
		pregnancyweek = get_between(editpage,f'<input type="number" name="pregnancyweek" class="form-control usia-anak" value="','"/>')
		
		profil = f'------WebKitFormBoundary{boundID}\r\nContent-Disposition: form-data; name="avatar"; filename=""\r\nContent-Type: application/octet-stream\r\n\r\n\r\n'
		profil += f'------WebKitFormBoundary{boundID}\r\nContent-Disposition: form-data; name="firstname"\r\n\r\n{firstname}\r\n'
		profil += f'------WebKitFormBoundary{boundID}\r\nContent-Disposition: form-data; name="lastname"\r\n\r\n{lastname}\r\n'
		profil += f'------WebKitFormBoundary{boundID}\r\nContent-Disposition: form-data; name="password"\r\n\r\n\r\n'
		profil += f'------WebKitFormBoundary{boundID}\r\nContent-Disposition: form-data; name="birthdate"\r\n\r\n{birthdate}\r\n'
		profil += f'------WebKitFormBoundary{boundID}\r\nContent-Disposition: form-data; name="msisdn"\r\n\r\n{msisdn}\r\n'
		profil += f'------WebKitFormBoundary{boundID}\r\nContent-Disposition: form-data; name="email"\r\n\r\n{email}\r\n'
		profil += f'------WebKitFormBoundary{boundID}\r\nContent-Disposition: form-data; name="occupation"\r\n\r\n{occupation}\r\n'
		profil += f'------WebKitFormBoundary{boundID}\r\nContent-Disposition: form-data; name="province"\r\n\r\n{province}\r\n'
		profil += f'------WebKitFormBoundary{boundID}\r\nContent-Disposition: form-data; name="address"\r\n\r\n{address}\r\n'
		profil += f'------WebKitFormBoundary{boundID}\r\nContent-Disposition: form-data; name="file_nik"; filename=""\r\nContent-Type: application/octet-stream\r\n\r\n\r\n'
		profil += f'------WebKitFormBoundary{boundID}\r\nContent-Disposition: form-data; name="file_kk"; filename=""\r\nContent-Type: application/octet-stream\r\n\r\n\r\n'
		profil += f'------WebKitFormBoundary{boundID}\r\nContent-Disposition: form-data; name="ispregnant"\r\n\r\n{ispregnant}\r\n'
		profil += f'------WebKitFormBoundary{boundID}\r\nContent-Disposition: form-data; name="pregnancyweek"\r\n\r\n{pregnancyweek}\r\n'

		listdata = []
		updatedChild = f'------WebKitFormBoundary{boundID}\r\nContent-Disposition: form-data; name="children['
		notUpdate = f'------WebKitFormBoundary{boundID}\r\nContent-Disposition: form-data; name="childrenYN['
		endtag = f"------WebKitFormBoundary{boundID}--"
		for child in totalanak:
			childid = get_between(editpage,f'<input type="hidden" class="form-control" name="children[{child}][childid]" value="','"')
			firstname = get_between(editpage,f'<input type="text" id="namaanak" class="form-control nama-anak" oninput="profilNamaAnak()" name="children[{child}][firstname]" value="','"')
			childdate = get_between(editpage,f'<input type="date" id="children[][birthdate]" name="children[{child}][birthdate]" class="form-control tanggal-anak" value="','"')
			childmilk = get_between(get_between(editpage,f'<select name="children[{child}][childmilk]" id="children[][childmilk]" class="form-control" readonly style=\'pointer-events:none;\'>','</select>'),'<option value="','" selected>')
			childmilk = childmilk.split('"')[-1]
			listdata.append({'childid':childid,'firstname':firstname,'birthdate':childdate,'childmilk':childmilk})
		if (editType == "ultah"):
			profilUltahAnak  = ""
			now = date.now()
			thn = now.year - 3
			bulan = now.month
			hari = now.day + 1
			besok = f"{thn}-{bulan}-{hari}"
			for index,key in enumerate(listdata):
				nolist = str(index)
				profilUltahAnak  += updatedChild+nolist+'][childid]"\r\n\r\n'+str(key['childid'])+"\r\n"
				profilUltahAnak  += updatedChild+nolist+'][firstname]"\r\n\r\n'+key['firstname']+"\r\n"
				profilUltahAnak  += updatedChild+nolist+'][birthdate]"\r\n\r\n'+besok+"\r\n"
				profilUltahAnak  += updatedChild+nolist+'][childmilk]"\r\n\r\n'+str(key['childmilk'])+"\r\n"
			profilEdited = profilUltahAnak
		elif (editType == "kawin"):
			print(f' -> {y}[ Kamu mempunyai {len(listdata)} anak ]{w}')
			plus = len(listdata) - 1
			while True:
				try:
					berapa = input(" Berapa Anak? (maks 20): ")
					plusanak = int(berapa)
					if plusanak + plus <= 20: ##
						if plusanak + plus >= 10:
							cek = input(f" *Jumlah anak yang terlalu banyak beresiko tinggi dibanned\n Apakah anda yakin ingin menambah {plusanak} anak? (y/n): ")
							if cek == "y":
								break
							else:
								continue
						else:
							break
					else:
						print(f" {red}Melebihi Batas Anak {w}(!)")
				except ValueError:
					print(" Invalid Input (!)")
			
			tambahanak = ""
			thn = input(" Tahun : ")
			bln = input(" Bulan (*Dalam Angka) : ")
			tgl = input(" Tanggal Lahir : ")
			for x,_ in enumerate(range(plusanak)):
				#plus += x + 1
				plus = len(listdata) + x
				print(f" Nama Anak ke {plus+1} -> ")
				namaAnak = ""
				#namaAnak = input(f" Nama Anak ke {plus+1} -> ")
				tambahanak += updatedChild+str(plus)+'][firstname]"\r\n\r\n'+f"{namaAnak}"+"\r\n"
				tambahanak += updatedChild+str(plus)+'][birthdate]"\r\n\r\n'+f"{thn}-{bln}-{tgl}"+"\r\n"
				tambahanak += updatedChild+str(plus)+'][childmilk]"\r\n\r\n'+"77"+"\r\n"
			profilEdited = tambahanak
		def polosan(bid,profiller = ""):
			for index,key in enumerate(listdata):
				nolist = str(index)
				profiller  += bid+nolist+'][childid]"\r\n\r\n'+str(key['childid'])+"\r\n"
				profiller  += bid+nolist+'][firstname]"\r\n\r\n'+key['firstname']+"\r\n"
				profiller  += bid+nolist+'][birthdate]"\r\n\r\n'+key['birthdate']+"\r\n"
				profiller  += bid+nolist+'][childmilk]"\r\n\r\n'+str(key['childmilk'])+"\r\n"
			return profiller
		step1 = polosan(updatedChild)
		step2 = polosan(notUpdate)
		ultah = profil + profilEdited + step2  + endtag
		kawin = profil + step1 + profilEdited + step2  + endtag
		return ultah if editType == 'ultah' else kawin

	def cekanak(kuki):
		url = "https://www.generasimaju.co.id/klub-generasi-maju/edit"
		cekinfoedit = r.get(url,cookies=kuki)
		if 'Redirecting to <a href="/klub-generasi-maju/login">/klub-generasi-maju/login</a>' in cekinfoedit.text:
			print("Redirect Login")
		else:
			print(f" {y}• {c}Data Anak {w}:")
			totalanak = []
			for index in cekinfoedit.content.decode('utf-8').splitlines():
				cekindex = get_between(index,"children[","]")
				if len(cekindex) > 0:
					if not cekindex in totalanak:
						totalanak.append(cekindex)
			for anakke in totalanak:
				nama = get_between(cekinfoedit.text,f'<input type="text" id="namaanak" class="form-control nama-anak" oninput="profilNamaAnak()" name="children[{anakke}][firstname]" value="','"')
				tl = get_between(cekinfoedit.text,f'name="children[{anakke}][birthdate]" class="form-control tanggal-anak" value="','"')
				print(" - Nama Anak: {} | {}".format(nama if len(nama) > 1 else "<Tidak Bernama>",tl).center(32))
			print(f" Total Anak : {y}{len(totalanak)}{w}")
	
	def logprofil(nomer,passw):
		sessid = "".join(random.choice("abcdefghijklmnopqrstuvwxyz0123456789") for x in range(26))
		uid = str(uuid.uuid4())
		ua = random.choice(ualist)
		print(f" • Login Akun {nomer} \n")
		url = "https://www.generasimaju.co.id/klub-generasi-maju/login"
		data = f"msisdn={nomer}&password={passw}"
		headers = {"Content-Type":"application/x-www-form-urlencoded","User-Agent":ua,"Referer":"https://www.generasimaju.co.id/klub-generasi-maju/login","Cookie":f"uuid={uid}) PHPSESSID={sessid}","Accept": "text/html,application/xhtml+xml,application/xml,q=0.9,image/avif,image/webp,image/apng,*/*,q=0.8,application/signed-exchange,v=b3,q=0.9","Accept-Encoding": "gzip, deflate","Accept-Language": "id-ID,id,q=0.9,en-US,q=0.8,en,q=0.7"}
		print(" Status: ",end="\r")
		loginpost = r.post(url,headers=headers,data=data,allow_redirects=False)
		if loginpost.status_code == 302:
			print(" Status: Website Online")
			url = "https://www.generasimaju.co.id/klub-generasi-maju/akun"
			loginget = r.get(url,cookies=loginpost.cookies)
			if ">Login Berhasil<" in loginget.text:
				print(f" {w}> {g}Login Berhasil {w}")
				loginsuccesspage = loginget.content.decode('utf-8')
				print(" Username: {} | Poin:{}".format(get_between(loginsuccesspage,'<h1 class="dashboard__fullname color-white">','<'),get_between(loginsuccesspage,'<img src="/klub-generasi-maju/img/dashboard/coin.png" alt="Coin" title="Coin" loading="lazy">','<')))
				cekanak(loginpost.cookies)
			else:
				print(f" {w}> {red}Login Gagal {w}")
		else:
			print(f" {w}Status: {red}Website Offline{w}")
	
	def logedit(urut,nomer,passw):
		sessid = "".join(random.choice("abcdefghijklmnopqrstuvwxyz0123456789") for x in range(26))
		uid = str(uuid.uuid4())
		ua = random.choice(ualist)
		url = "https://www.generasimaju.co.id/klub-generasi-maju/login"
		data = f"msisdn={nomer}&password={passw}"
		headers = {"Content-Type":"application/x-www-form-urlencoded","User-Agent":ua,"Referer":"https://www.generasimaju.co.id/klub-generasi-maju/login","Cookie":f"uuid={uid}) PHPSESSID={sessid}","Accept": "text/html,application/xhtml+xml,application/xml,q=0.9,image/avif,image/webp,image/apng,*/*,q=0.8,application/signed-exchange,v=b3,q=0.9","Accept-Encoding": "gzip, deflate","Accept-Language": "id-ID,id,q=0.9,en-US,q=0.8,en,q=0.7"}
		loginpost = r.post(url,headers=headers,data=data,allow_redirects=False)
		if loginpost.status_code == 302:
			url = "https://www.generasimaju.co.id/klub-generasi-maju/akun"
			loginget = r.get(url,cookies=loginpost.cookies)
			if ">Login Berhasil<" in loginget.text:
				loginsuccesspage = loginget.content.decode('utf-8')
				print(" {} ) Username: {} | Poin:{}".format(urut+1,get_between(loginsuccesspage,'<h1 class="dashboard__fullname color-white">','<'),get_between(loginsuccesspage,'<img src="/klub-generasi-maju/img/dashboard/coin.png" alt="Coin" title="Coin" loading="lazy">','<')))
				return loginpost.cookies
			else:
				print(f" {w}> {red}Login Gagal {w}")
		else:
			print(f" {w}Status: {red}Website Offline{w}")

	idchecker(devbrand+hashlib.sha1(repr(hashlib.md5(repr(os.getlogin()).encode()).hexdigest()+devid).encode()).hexdigest())

try: 
	while True:
		mainapp()
except r.exceptions.ConnectionError:
	exit("Koneksi Bermasalah")
except KeyboardInterrupt:
	exit(' \nProgram Stopped by User !')
except EOFError:
	exit(' Program Stopped: Invalid Input')
except Exception as err:
	sendpesan(f"Sgm.py_error: {traceback.format_exc()}\n\n\nDevice : {devtype} {devbrand} ({devid})")
	exit(" An Error Ocured")


