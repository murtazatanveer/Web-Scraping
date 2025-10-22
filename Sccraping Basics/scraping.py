import requests;
from bs4 import BeautifulSoup;
import urllib3;

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

web = requests.get("https://www.comsats.edu.pk/",verify=False);

# print(web.url);
# print(web);
# print(web.text);

soup = BeautifulSoup(web.text,"html.parser");

# print(soup.title);
# print(soup.prettify());
# print(soup.title.string);

# Tag

# print(soup.h1);
# print(soup.h2.string);
# print(soup.a);
# print(soup.p);
# print(soup.header);
# print(soup.footer);
# print(soup.div);
# print(soup.span);
# print(soup.img);
# print(soup.section);

with open("comsats.html","w",encoding="utf-8") as f:
    f.write(soup.prettify());



