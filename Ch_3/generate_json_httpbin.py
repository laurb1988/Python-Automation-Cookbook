import requests
from bs4 import BeautifulSoup
import re

response = requests.get('http://httpbin.org/forms/post')
page = BeautifulSoup(response.text)
form.page.find('form')
#{field.get('name') for field in form.find_all(re.compile('input|textarea'))}
#{'delivery', 'topping', 'size', 'custemail', 'comments', 'custtel', 'custname'}
data = {'custname':"Sean O'Connel", 'custtel':'123-456-789', 'custemail':'sean@oconnel.ie', 'size':'small', 'topping':['bacont', 'onion'], 'delivery':'20:30', 'comments':''}
response = requests.post('http://httpbin.org/post', data)
print(response)