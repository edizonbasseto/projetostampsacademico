__author__ = 'fkfouri'

import goslate
import urllib.request as rq


def translate(text):
    proxy_handler = rq.ProxyHandler({"http": "http://login:pwd@lnx237in.sjk.emb:9090"})
    proxy_opener = rq.build_opener(proxy_handler)
    # gs = goslate.Goslate()
    gs = goslate.Goslate(opener=proxy_opener)
    return gs.translate('give me some love', 'pt-br')


print(translate('dd'))