import json
from bs4 import BeautifulSoup

#############################
#
# Functions to Parse formatted text
#
#############################

def html_parse(html, selector, rformat):
	#### rformat ####
	# qlist: Quoted comma separated list, best for flat csv files
	# json: Stringified JSON
	# list: list variable
	soup = BeautifulSoup(html)
	items = soup.find_all(selector)
	clean = []
	for i in items:
		clean.append(i.get_text().strip())
	if rformat == 'qlist':
		return ', '.join(clean)
	elif rformat == 'json':
		return json.loads(clean)
	else:
		return clean