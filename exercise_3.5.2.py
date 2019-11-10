import requests
url = 'https://stepic.org/media/attachments/course67/3.6.2/790.txt'
r = requests.get(url) # Передача параметров в запрос
data = r.text.strip()
d = data.splitlines()
print(len(d))
