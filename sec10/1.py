import urllib.request
from bs4 import BeautifulSoup

class Scraper:
    def __init__(self, site):
        self.site = site
    
    def scrape(self):
        #urlopen関数はウェブサイトへのリクエストを行う
        """
        HTMLと追加情報が格納される。
        """
        r = urllib.request.urlopen(self.site)
        html = r.read()

        #HTMLをパースして欲しいことを伝える"html.parser"という文字列を入れる
        parser = "html.parser"
        sp = BeautifulSoup(html, parser)

        #"a"を引数に
        for tag in sp.find_all("a"):
            url = tag.get("href")
            if url is None:
                continue
            if "html" in url:
                print("\n" + url)

news = "http://news.google.com/"
Scraper(news).scrape()




