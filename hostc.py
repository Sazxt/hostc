#!/usr/bin/python2
# | Coding By SazxT Team Black Coder crush #
# -*- coding: UTF-8 -*-.
# Yang Recode Mati !!! , Recode Ga BaKal jadiin Lu mAstah Ajg 
# Masa Bikin Tools kaya gini aja ga bisa ?
from bs4 import BeautifulSoup as bs
import requests as req
from requests.exceptions import ConnectionError
import os as ce
a = []
def jz():
	try:
		
		global a
		ce.system("clear")
		print "\n         \x1b[34m\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97\n           \x1b[31m\xe2\x8f\xa3 \x1b[32mAuthor   \x1b[37m: Sazxt\n           \x1b[31m\xe2\x8f\xa3 \x1b[32mMy Team  \x1b[37m: Black Coder Crush\n           \x1b[31m\xe2\x8f\xa3 \x1b[32mwhatsapp \x1b[37m: 083892081021\n           \x1b[31m\xe2\x8f\xa3 \x1b[32mCodeName \x1b[37m: \x1b[36mHostc \x1b[0;1mv1.1\n         \x1b[34m\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\n"
		x = lambda _:"\x1b[0m[+] "+_
		_link = "https://www.ultratools.com/tools/httpHeaderResult?domainName={}"
		_AnWer = str(raw_input(x("Masukan Link : ")))
		_re = req.get(_link.format(_AnWer))
		#<---scraping-->
		soup = bs(_re.text,"html.parser")
		for x in  soup.find_all('div'):
			a.append(x.findAll("span",{"class":"value"}))
		_sct_Data_ = bs(str(a[31]),"html.parser")
		_sct_trasFerEnc_ = bs(str(a[32]),"html.parser")
		_sct_Connevt_ = bs(str(a[33]),"html.parser")
		_sct_CacheCont_ = bs(str(a[34]),"html.parser")
		_sct_Expret_ = bs(str(a[35]),"html.parser")
		_sct_LocAl_ = bs(str(a[36]),"html.parser")
		_sct_VarY_ = bs(str(a[37]),"html.parser")
		_sct_Server_ = bs(str(a[38]),"html.parser")
		_sct_CfrAy_ = bs(str(a[39]),"html.parser")
		#<tampilkan>
		print '\xe2\x96\x82'*40
		print "[+] Data : %s"%(_sct_Data_.get_text())
		print "[+] Transfer-Encoding : %s"%(_sct_trasFerEnc_.get_text())
		print "[+] Connection : %s"%(_sct_Connevt_.get_text())
		print "[+] Cache-Control : %s"%(_sct_CacheCont_.get_text())
		print "[+] Expires : %s"%(_sct_Expret_.get_text())
		print "[+] Location : %s"%(_sct_LocAl_.get_text())
		print "[+] Vary : %s"%(_sct_VarY_.get_text())
		print "[+] Server : %s"%(_sct_Server_.get_text())
		print "[+] CF-RAY : %s"%(_sct_CfrAy_.get_text())
		print '\xe2\x96\x82'*40
	except KeyboardInterrupt:
		print x("Exit...")
	except EOFError:
		print x("Exit...")
	except ConnectionError:
		print x("Tidak Ada Koneksi !")
if __name__ == "__main__":
	jz()