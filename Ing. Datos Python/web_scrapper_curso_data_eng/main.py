importargparse
importlogging
logging.basicConfig(level=logging.INFO)

importnews_page_objectsasnews
fromcommonimportconfig

logger=logging.getLogger(__name__)

def_news_scraper(news_site_uid):
host=config()['news_sites'][news_site_uid]['url']
logging.info("Beginningscraperfor{}".format(host))
homepage=news.HomePage(news_site_uid,host)
forlinkinhomepage.article_links:
print(link)

if__name__=="__main__":
parser=argparse.ArgumentParser()

news_site_choices=list(config()['news_sites'].keys())
parser.add_argument('news_site',help='Thenewssitethatyouwanttoscrape'
,type=str,choices=news_site_choices)

args=parser.parse_args()
_news_scraper(args.news_site)