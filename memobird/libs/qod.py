from collections import namedtuple
from memobird.libs import http
from memobird.libs.quote import Quote

xml_url = 'https://pfeeds.tevinzhang.com/quotationspage/qotd'

KEY_TITLE = 'title'
KEY_DESCRIPTION = 'description'
KEY_START = '<feedburner'

def _get_values(xml, **keys):
    d = {}
    xml = xml[xml.find(KEY_START):]  # skip meta information
    for key, raw_key in keys.items():
        opening = "<%s>" % raw_key
        closing = "</%s>" % raw_key
        st = xml.find(opening) + len(opening)
        ed = xml.find(closing, st)
        d[key] = xml[st:ed].strip('"')
    return d


def fetch_qod() -> Quote:
    xml_str = http.fetch_text(xml_url)
    vals = _get_values(xml_str, title=KEY_TITLE, quote=KEY_DESCRIPTION)
    return Quote(title=vals['title'], quote=vals['quote'], author='')
