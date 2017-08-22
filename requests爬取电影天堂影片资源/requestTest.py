import requests
from bs4 import BeautifulSoup
import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')   #中文特殊字符 windows打印

r = requests.get("http://www.ygdy8.net/html/gndy/oumei/index.html")
r_bytes = r.content
html = r_bytes.decode("gb2312","ignore")        #ignore 忽略非法字符
print(type(html))
soup = BeautifulSoup(html,"html.parser")
movie_list = soup.select("div.co_area2 table.tbspan b")
print(len(movie_list))
f = open("movies.txt","w",encoding="utf-8")
for item in movie_list:
	movie_name = item.select("a")[1].text
	movie_url = "http://www.ygdy8.net/"+item.select("a")[1].get("href")
	print(movie_name)
	print(movie_url)
	f.writelines("movie_name:"+movie_name+ "   "+ "movie_url:"+movie_url)
f.close()
# f = open("movie.html","w",encoding="utf-8")
# f.writelines(html)
# f.close()
