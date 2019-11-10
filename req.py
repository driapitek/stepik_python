import requests
url = 'http://example.com'
par = {'key1': 'value1', 'key2': 'value2'}
r = requests.get(url, params = par) # Передача параметров в запрос
print(r.url) # сформированный url-адрес с учетом параметров гет-запроса
