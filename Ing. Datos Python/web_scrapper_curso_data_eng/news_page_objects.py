importrequests
importbs4
fromcommonimportconfig

classNewsPage:
def__init__(self,news_site_uid,url):
self._config=config()['news_sites'][news_site_uid]
self._queries=self._config['queries']
self._html=None

self._visit(url)

def_select(self,query_string):returnself._html.select(query_string)

def_visit(self,url):
response=requests.get(url)
response.raise_for_status()

self._html=bs4.BeautifulSoup(response.text,'html.parser')

classHomePage(NewsPage):

def__init__(self,news_site_uid,url):
super().__init__(news_site_uid,url)

self._visit(url)


@property
defarticle_links(self):
link_list=[]
forlinkinself._select(self._queries['homepage_article_links']):
iflinkandlink.has_attr('href'):
link_list.append(link)

returnset(link['href']forlinkinlink_list)

classArticlePage(NewsPage):
def__init__(self,news_site_uid,url):
super().__init__(news_site_uid,url)

@property
defbody(self):
result=self._select(self._queries['article_body'])

returnresult[0].textiflen(result)else''

@property
deftitle(self):
result=self._select(self._queries['article_title'])

returnresult[0].textiflen(result)else''