import urllib.request

try:
    urllib.request.urlopen("http://pudim.com.br/").getcode()
except:
    print('O site Pudim não está acessível no momento.')
else:
    print('O site Pudim está acessível.')
