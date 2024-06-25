import requests as re
from bs4 import BeautifulSoup

response = re.get('http://127.0.0.1:6543/welcome')
if response.status_code == 200:
	# print('Server is working!!!')
	# print(response.text)
	soup = BeautifulSoup(response.text, 'html.parser')
	print(soup.prettify())