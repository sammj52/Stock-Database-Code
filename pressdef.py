import requests
import bs4


url = 'https://seekingalpha.com/market-news/all'
res = requests.get(url)
print(res)

soup = bs4.BeautifulSoup(res.text, 'lxml')

def get_tick(key):
	sect = soup.find_all('ul',{'class':'mc-list'})
	for name in sect:
		data = name.get_text()
		poss = any(word in data for word in key)
		if poss:
			sym = soup.find_all('a',{'sasource':'ticker_mc_quote'})
			for comp in sym:
				hope = comp.get_text()
				print(hope)
	'''^Because I hope this Works^'''
        
def true_tick(help):
	sect_two = soup.find_all('li',{'class':'mc'})
	for tick in sect_two:
		data_two = tick.get_text()
		boool = any(word in data_two for word in key_word_list)
		print(boool)	

key_word_list = ['positive','received','receives','grant','grants','fda','approval','drug trials','drug trial','cancer','improvements','benefits','benefit','beneficial','agreement','agreements','partnership','partnerships','investors','billionaire','phase','successful','fast track','breakout','increase','increases','acquire','acquires','acquired','accepted','new','contract','awarded','signs','completes','merger','promising','gain','gains','primary','endpoints','achieves','achievement','launches']

get_tick(key_word_list)
true_tick(get_tick)
