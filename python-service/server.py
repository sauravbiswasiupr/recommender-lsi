import zerorpc
import json
from time import time
import nltk
from nltk.corpus import brown

from indexer import Indexer

def create_documents():
    brown_paras = brown.paras(categories='news')
    documents = []
    for p in brown_paras:
        for doc in p:
            documents.append(" ".join(doc))

    data = []
    for id, d in enumerate(documents):
        data.append((id, d))
    return data

indexer = Indexer()

class PythonService(object):
    def recommend(self, idx):
        similar_docs = indexer.recommend(str(idx))
        return similar_docs

    def index(self):
        documents = create_documents()
        t0 = time()
        indexer.index(documents)
        t1 = time()
        return "{}".format(t1-t0)

s = zerorpc.Server(PythonService())
s.bind("tcp://0.0.0.0:4242")
s.run()
