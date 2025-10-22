from bs4 import BeautifulSoup;
import requests;

web = requests.get("https://www.geeksforgeeks.org/python/implementing-web-scraping-python-beautiful-soup/");

print(web.status_code);

soup=BeautifulSoup(web.text,"html.parser");

print(soup.title.string);

print(soup.find('a').get('href'));
