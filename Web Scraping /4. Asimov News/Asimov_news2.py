import requests
from bs4 import BeautifulSoup

class Site:
    def __init__(self, site):
        self.site = site 
        self.news = []
    def update_news(self):
        if self.site.lower() =="globo":

            globo_url = 'https://www.globo.com/'
            page = requests.get(globo_url)
            resposta = page.text
            soup = BeautifulSoup(resposta, 'html.parser')
            noticias = soup.find_all("a")
            tg_class1 ="post__link"
            tg_class2 = "post-multicontent_link--title_text"
            news_dict = {}
            for noticia in noticias:
                # print(noticia)
                if noticia.h2 != None:
                    # print(noticia)
                    
                    if tg_class1 in noticia.h2.get("class") or tg_class2 in  noticia.h2.get("class") :
                        print(noticia)
                    #     print(noticia.h2.text)
                        
                        news_dict[noticia.h2.text] = noticia.get("href")
            self.news = news_dict
    
    
# if __name__ == "__main__":
self = Site('globo')