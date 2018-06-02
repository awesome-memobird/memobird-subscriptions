import random
import logging
from memobird.libs import http
from memobird.libs.quote import Quote

SERVER = "https://quotes.rest"
QOD = "/qod"
QOD_CATS = QOD + "/categories"


def _fetch_cats():
    url = SERVER + QOD_CATS
    res = http.fetch_json(url)
    cats = res['contents']['categories']
    return list(cats.keys())

def _fetch_qod_by_cat(cat) -> Quote:
    url = SERVER + QOD + '?category=%s' % cat
    res = http.fetch_json(url)
    logging.info(res)
    q = res['contents']['quotes'][0]
    # qod={"quote":"Art, like morality, consists in drawing the line...",
    #      "author":'Gilbert K. Chesterton',
    #      "title":"Art quote of the day"}
    return Quote(quote=q['quote'],
                 author=q['author'],
                 title=q['title'])

def fetch_qod() -> Quote:
    cats = _fetch_cats()
    logging.info("available CATs: %s", cats)
    cat = random.choice(cats)
    logging.info("random CAT: %s", cat)
    qod = _fetch_qod_by_cat(cat)
    logging.info("QOD: %s", qod)
    return qod
